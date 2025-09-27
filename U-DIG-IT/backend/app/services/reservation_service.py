from __future__ import annotations

from datetime import date

from fastapi import HTTPException, status
from sqlalchemy.orm import selectinload
from sqlmodel import Session, select

from ..models import Equipment, Reservation, ReservationStatus
from ..schemas import ReservationCreate, ReservationRead, ReservationUpdate
from ..utils.identifiers import generate_reservation_code
from .catalog_service import calculate_availability, build_equipment_list_item


def _validate_dates(start: date, end: date) -> None:
    if start >= end:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="End date must be after start date")


def create_reservation(session: Session, payload: ReservationCreate) -> Reservation:
    equipment = session.exec(select(Equipment).where(Equipment.slug == payload.equipment_slug)).first()
    if not equipment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Equipment not found")

    _validate_dates(payload.start_date, payload.end_date)

    availability = calculate_availability(
        session,
        equipment=equipment,
        start_date=payload.start_date,
        end_date=payload.end_date,
    )

    if not availability.is_available:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Equipment unavailable for selected dates")

    total_days = (payload.end_date - payload.start_date).days

    if total_days < equipment.min_rental_days:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Minimum rental period is {equipment.min_rental_days} days",
        )

    if equipment.max_rental_days and total_days > equipment.max_rental_days:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Maximum rental period is {equipment.max_rental_days} days",
        )

    subtotal = equipment.daily_rate * total_days
    total_amount = subtotal + equipment.deposit_amount

    reservation = Reservation(
        reservation_code=generate_reservation_code(),
        customer_id=payload.customer_id,
        customer_name=payload.customer_name,
        customer_email=payload.customer_email,
        customer_phone=payload.customer_phone,
        equipment_id=equipment.id,
        location_id=payload.location_id,
        start_date=payload.start_date,
        end_date=payload.end_date,
        total_days=total_days,
        subtotal_amount=subtotal,
        deposit_amount=equipment.deposit_amount,
        total_amount=total_amount,
        notes=payload.notes,
        status=ReservationStatus.PENDING,
    )

    session.add(reservation)
    session.commit()
    session.refresh(reservation)

    return reservation


def reservation_to_read_model(reservation: Reservation) -> ReservationRead:
    return ReservationRead(
        reservation_code=reservation.reservation_code,
        status=reservation.status,
        payment_status=reservation.payment_status,
        start_date=reservation.start_date,
        end_date=reservation.end_date,
        total_days=reservation.total_days,
        subtotal_amount=reservation.subtotal_amount,
        deposit_amount=reservation.deposit_amount,
        total_amount=reservation.total_amount,
        equipment=build_equipment_list_item(reservation.equipment),
    )


def get_reservation_by_code(session: Session, reservation_code: str) -> Reservation:
    reservation = session.exec(
        select(Reservation)
        .options(
            selectinload(Reservation.equipment)
            .selectinload(Equipment.category),
            selectinload(Reservation.equipment).selectinload(Equipment.media),
            selectinload(Reservation.equipment).selectinload(Equipment.reviews),
        )
        .where(Reservation.reservation_code == reservation_code)
    ).unique().first()
    if not reservation:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Reservation not found")
    return reservation


def list_recent_reservations(session: Session, limit: int = 5) -> list[ReservationRead]:
    reservations = session.exec(
        select(Reservation)
        .options(
            selectinload(Reservation.equipment)
            .selectinload(Equipment.category),
            selectinload(Reservation.equipment).selectinload(Equipment.media),
            selectinload(Reservation.equipment).selectinload(Equipment.reviews),
        )
        .order_by(Reservation.created_at.desc())
        .limit(limit)
    ).unique().all()
    return [reservation_to_read_model(reservation) for reservation in reservations]


def yearly_reservation_summary(session: Session) -> list[dict[str, float]]:
    reservations = session.exec(select(Reservation)).all()
    bucket: dict[str, dict[str, float]] = {}
    for reservation in reservations:
        month_key = reservation.start_date.strftime("%Y-%m")
        data = bucket.setdefault(month_key, {"reservation_count": 0, "revenue": 0.0})
        data["reservation_count"] += 1
        data["revenue"] += float(reservation.total_amount)

    return [
        {"month": month, "reservation_count": stats["reservation_count"], "revenue": stats["revenue"]}
        for month, stats in sorted(bucket.items())
    ]


def update_reservation(session: Session, reservation: Reservation, payload: ReservationUpdate) -> Reservation:
    if payload.status is not None:
        reservation.status = payload.status
    if payload.payment_status is not None:
        reservation.payment_status = payload.payment_status
    if payload.notes is not None:
        reservation.notes = payload.notes

    reservation.touch()
    session.add(reservation)
    session.commit()
    session.refresh(reservation)
    return reservation
