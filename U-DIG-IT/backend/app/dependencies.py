from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import selectinload
from sqlmodel import Session, select

from .config import settings
from .database import get_session
from .models import User, UserRole
from .security import decode_token


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")


def get_oauth2_scheme() -> OAuth2PasswordBearer:
    return oauth2_scheme


def get_current_user(token: str = Depends(get_oauth2_scheme()), session: Session = Depends(get_session)) -> User:
    try:
        payload = decode_token(token)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials") from exc

    email: str | None = payload.get("sub")
    if not email:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token payload")

    user = session.exec(
        select(User)
        .options(selectinload(User.customer_profile), selectinload(User.reservations))
        .where(User.email == email)
    ).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")

    if not user.is_active:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User disabled")

    return user


def get_current_admin(user: User = Depends(get_current_user)) -> User:
    if user.role not in {UserRole.ADMIN, UserRole.MANAGER}:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin privileges required")
    return user
