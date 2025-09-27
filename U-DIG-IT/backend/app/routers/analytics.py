from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy import func
from sqlalchemy.orm import selectinload
from sqlmodel import Session, select

from ..dependencies import get_current_admin, get_session
from ..models import Equipment, Reservation, Review
from ..schemas import AnalyticsSummary, DashboardSnapshot, TopEquipmentPerformance
from ..services import catalog_service, reservation_service

router = APIRouter(prefix="/api/analytics", tags=["analytics"])


@router.get("/dashboard", response_model=DashboardSnapshot)
def get_dashboard_snapshot(
    session: Session = Depends(get_session),
    _current_admin=Depends(get_current_admin),
) -> DashboardSnapshot:
    recent_reservations = reservation_service.list_recent_reservations(session, limit=10)

    summary_rows = reservation_service.yearly_reservation_summary(session)
    analytics = [
        AnalyticsSummary(
            date=datetime.strptime(f"{row['month']}-01", "%Y-%m-%d").date(),
            total_reservations=row["reservation_count"],
            total_revenue=row["revenue"],
            new_customers=0,
            average_order_value=(row["revenue"] / row["reservation_count"]) if row["reservation_count"] else 0,
            utilization_rate=0.0,
        )
        for row in summary_rows
    ]

    top_equipment_rows = session.exec(
        select(
            Equipment,
            func.sum(Reservation.total_amount).label("revenue"),
            func.count(Reservation.id).label("reservations"),
        )
        .join(Reservation, Reservation.equipment_id == Equipment.id)
        .group_by(Equipment.id)
        .order_by(func.sum(Reservation.total_amount).desc())
        .limit(5)
    ).all()

    top_equipment: list[TopEquipmentPerformance] = []
    for equipment, revenue, reservation_count in top_equipment_rows:
        equipment = session.exec(
            select(Equipment)
            .options(
                selectinload(Equipment.category),
                selectinload(Equipment.media),
                selectinload(Equipment.reviews),
            )
            .where(Equipment.id == equipment.id)
        ).one()
        item = catalog_service.build_equipment_list_item(equipment)
        top_equipment.append(
            TopEquipmentPerformance(
                equipment=item,
                revenue=float(revenue or 0),
                reservation_count=int(reservation_count or 0),
            )
        )

    return DashboardSnapshot(
        reservations=recent_reservations,
        analytics=analytics,
        top_equipment=top_equipment,
    )
