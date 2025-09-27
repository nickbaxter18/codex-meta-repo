from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session, select

from ..dependencies import get_current_user, get_session
from ..models import CustomerProfile, User, UserRole
from ..schemas import AuthenticatedUser, TokenResponse, UserCreate
from ..security import create_access_token, hash_password, verify_password
from ..config import settings

router = APIRouter(prefix="/api/auth", tags=["auth"])


@router.post("/register", response_model=TokenResponse, status_code=status.HTTP_201_CREATED)
def register_user(payload: UserCreate, session: Session = Depends(get_session)) -> TokenResponse:
    existing_user = session.exec(select(User).where(User.email == payload.email)).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already registered")

    user = User(
        email=payload.email,
        full_name=payload.full_name,
        hashed_password=hash_password(payload.password),
        role=UserRole.CUSTOMER,
    )
    session.add(user)
    session.commit()
    session.refresh(user)

    if payload.phone_number or payload.company_name:
        profile = CustomerProfile(
            user_id=user.id,
            phone_number=payload.phone_number,
            company_name=payload.company_name,
        )
        session.add(profile)
        session.commit()

    token = create_access_token(user.email)
    return TokenResponse(access_token=token, expires_in=settings.jwt_expires_in_minutes * 60)


@router.post("/login", response_model=TokenResponse)
def login_user(form_data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_session)) -> TokenResponse:
    user = session.exec(select(User).where(User.email == form_data.username)).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")

    token = create_access_token(user.email, {"role": user.role.value})
    return TokenResponse(access_token=token, expires_in=settings.jwt_expires_in_minutes * 60)


@router.get("/me", response_model=AuthenticatedUser)
def get_me(current_user: User = Depends(get_current_user)) -> AuthenticatedUser:
    return AuthenticatedUser.model_validate(current_user)
