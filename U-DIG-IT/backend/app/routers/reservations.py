from fastapi import APIRouter, Depends, HTTPException, Path, status
from sqlmodel import Session

from ..dependencies import get_current_admin, get_current_user, get_session
from ..models import Reservation, UserRole
from ..schemas import ReservationCreate, ReservationRead, ReservationSuccessResponse, ReservationUpdate
from ..services import reservation_service

router = APIRouter(prefix="/api/reservations", tags=["reservations"])


@router.post("", response_model=ReservationSuccessResponse, status_code=status.HTTP_201_CREATED)
def create_reservation(
    payload: ReservationCreate,
    session: Session = Depends(get_session),
    current_user=Depends(get_current_user),
) -> ReservationSuccessResponse:
    if payload.customer_id is None:
        payload.customer_id = current_user.id

    reservation = reservation_service.create_reservation(session, payload)
    return ReservationSuccessResponse(
        reservation=reservation_service.reservation_to_read_model(reservation),
        message="Reservation created successfully. Our logistics team will contact you to confirm delivery and pickup windows.",
    )


@router.get("/{reservation_code}", response_model=ReservationRead)
def get_reservation(reservation_code: str = Path(..., min_length=5), session: Session = Depends(get_session), current_user=Depends(get_current_user)) -> ReservationRead:
    reservation = reservation_service.get_reservation_by_code(session, reservation_code)
    if reservation.customer_id and reservation.customer_id != current_user.id and current_user.role not in {UserRole.ADMIN, UserRole.MANAGER}:
        raise HTTPException(status_code=403, detail="You do not have access to this reservation")
    return reservation_service.reservation_to_read_model(reservation)


@router.get("", response_model=list[ReservationRead])
def list_reservations(session: Session = Depends(get_session), _current_admin=Depends(get_current_admin)) -> list[ReservationRead]:
    reservations = reservation_service.list_recent_reservations(session, limit=25)
    return reservations


@router.patch("/{reservation_code}", response_model=ReservationRead)
def update_reservation(
    reservation_code: str,
    payload: ReservationUpdate,
    session: Session = Depends(get_session),
    _current_admin=Depends(get_current_admin),
) -> ReservationRead:
    reservation = reservation_service.get_reservation_by_code(session, reservation_code)
    updated = reservation_service.update_reservation(session, reservation, payload)
    return reservation_service.reservation_to_read_model(updated)
