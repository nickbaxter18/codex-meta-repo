from __future__ import annotations

from collections import defaultdict
from datetime import date
from typing import Iterable

from sqlalchemy import func
from sqlalchemy.orm import selectinload
from sqlmodel import Session, select

from ..models import Category, Equipment, Location, Reservation, ReservationStatus, Review
from ..schemas import (
    AvailabilityResponse,
    CategoryRead,
    EquipmentDetail,
    EquipmentListItem,
    EquipmentMediaRead,
    LandingStats,
    LocationRead,
    ReviewRead,
)


def build_equipment_list_item(equipment: Equipment) -> EquipmentListItem:
    primary_image = next((media.url for media in equipment.media if media.is_primary), None)
    average_rating = None
    review_count = len(equipment.reviews)
    if review_count:
        average_rating = sum(review.rating for review in equipment.reviews) / review_count

    return EquipmentListItem(
        id=equipment.id,
        name=equipment.name,
        slug=equipment.slug,
        summary=equipment.summary,
        daily_rate=equipment.daily_rate,
        deposit_amount=equipment.deposit_amount,
        featured=equipment.featured,
        tags=equipment.tags,
        primary_image=primary_image,
        average_rating=average_rating,
        review_count=review_count,
        category={
            "slug": equipment.category.slug,
            "name": equipment.category.name,
            "description": equipment.category.description,
            "icon": equipment.category.icon,
        },
    )


def list_categories(session: Session) -> list[CategoryRead]:
    category_counts = defaultdict(int)
    rows = session.exec(
        select(Equipment.category_id, func.count(Equipment.id)).group_by(Equipment.category_id)
    ).all()
    for category_id, count in rows:
        category_counts[category_id] = count

    categories = session.exec(select(Category)).all()
    results: list[CategoryRead] = []
    for category in categories:
        results.append(
            CategoryRead(
                id=category.id,
                slug=category.slug,
                name=category.name,
                description=category.description,
                icon=category.icon,
                equipment_count=category_counts.get(category.id, 0),
            )
        )
    return sorted(results, key=lambda cat: cat.name)


def list_equipment(
    session: Session,
    *,
    category_slug: str | None = None,
    search: str | None = None,
    featured_only: bool = False,
) -> list[EquipmentListItem]:
    statement = (
        select(Equipment)
        .options(
            selectinload(Equipment.category),
            selectinload(Equipment.media),
            selectinload(Equipment.reviews),
            selectinload(Equipment.maintenance_logs),
        )
        .order_by(Equipment.featured.desc(), Equipment.name.asc())
    )

    if category_slug:
        statement = statement.where(Equipment.category.has(slug=category_slug))

    if search:
        like_pattern = f"%{search.lower()}%"
        statement = statement.where(
            func.lower(Equipment.name).like(like_pattern)
            | func.lower(Equipment.summary).like(like_pattern)
            | func.lower(Equipment.description).like(like_pattern)
        )

    if featured_only:
        statement = statement.where(Equipment.featured.is_(True))

    equipment_items = session.exec(statement).unique().all()
    return [build_equipment_list_item(equipment) for equipment in equipment_items]


def filter_equipment_by_tag(
    equipment_items: Iterable[EquipmentListItem],
    tag: str | None,
) -> list[EquipmentListItem]:
    if not tag:
        return list(equipment_items)

    tag_lower = tag.lower()
    return [
        item
        for item in equipment_items
        if any(equipment_tag.lower() == tag_lower for equipment_tag in item.tags)
    ]


def extract_unique_tags(equipment_items: Iterable[EquipmentListItem]) -> list[str]:
    unique_tags: set[str] = set()
    for item in equipment_items:
        unique_tags.update(item.tags)
    return sorted(unique_tags, key=lambda value: value.lower())


def get_equipment_detail(session: Session, slug: str) -> EquipmentDetail:
    equipment = session.exec(
        select(Equipment)
        .options(
            selectinload(Equipment.category),
            selectinload(Equipment.media),
            selectinload(Equipment.reviews),
            selectinload(Equipment.maintenance_logs),
        )
        .where(Equipment.slug == slug)
    ).one()
    item = build_equipment_list_item(equipment)
    gallery = [EquipmentMediaRead.model_validate(media) for media in equipment.media]
    reviews = [ReviewRead.model_validate(review) for review in equipment.reviews if review.published]
    maintenance_statuses = [log.status.value for log in equipment.maintenance_logs[:3]]

    return EquipmentDetail(
        **item.model_dump(),
        description=equipment.description,
        specifications=equipment.specifications,
        gallery=gallery,
        maintenance_statuses=maintenance_statuses,
        reviews=reviews,
    )


def get_featured_equipment(session: Session) -> list[EquipmentListItem]:
    featured = session.exec(
        select(Equipment)
        .options(
            selectinload(Equipment.category),
            selectinload(Equipment.media),
            selectinload(Equipment.reviews),
        )
        .where(Equipment.featured.is_(True))
    ).unique().all()
    if featured:
        return [build_equipment_list_item(item) for item in featured]

    # fallback to first few if no explicit featured flag set
    fallback = session.exec(
        select(Equipment)
        .options(
            selectinload(Equipment.category),
            selectinload(Equipment.media),
            selectinload(Equipment.reviews),
        )
        .limit(3)
    ).unique().all()
    return [build_equipment_list_item(item) for item in fallback]


def compute_landing_stats(session: Session) -> LandingStats:
    total_inventory = session.exec(select(func.sum(Equipment.availability_count))).one() or 0
    active_customers = session.exec(select(func.count(Reservation.customer_email).distinct())).one() or 0
    locations_served = session.exec(select(func.count(Reservation.location_id).distinct())).one() or 0

    rating_rows = session.exec(select(func.avg(Review.rating), func.count(Review.id))).one()
    average_rating = float(rating_rows[0]) if rating_rows[0] else 0.0

    testimonials: list[ReviewRead] = [
        ReviewRead.model_validate(review)
        for review in session.exec(select(Review).where(Review.published.is_(True)).limit(3)).all()
    ]

    return LandingStats(
        total_inventory=int(total_inventory or 0),
        active_customers=int(active_customers or 0),
        locations_served=int(locations_served or 0),
        on_time_delivery_rate=98.5,
        average_rating=round(average_rating, 2),
        featured_testimonials=testimonials,
    )


def list_locations(session: Session) -> list[LocationRead]:
    locations = session.exec(select(Location).order_by(Location.name.asc())).all()
    return [LocationRead.model_validate(location) for location in locations]


def calculate_availability(
    session: Session,
    *,
    equipment: Equipment,
    start_date: date,
    end_date: date,
) -> AvailabilityResponse:
    overlap_statement = select(func.count(Reservation.id)).where(
        Reservation.equipment_id == equipment.id,
        Reservation.status != ReservationStatus.CANCELLED,
        Reservation.start_date <= end_date,
        Reservation.end_date >= start_date,
    )
    overlapping_reservations = session.exec(overlap_statement).one() or 0
    available_quantity = max(equipment.availability_count - overlapping_reservations, 0)
    is_available = available_quantity > 0

    return AvailabilityResponse(
        equipment_id=equipment.id,
        equipment_name=equipment.name,
        available_quantity=available_quantity,
        is_available=is_available,
    )
