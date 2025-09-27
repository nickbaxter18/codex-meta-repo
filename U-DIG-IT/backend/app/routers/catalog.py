from datetime import date

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select

from ..dependencies import get_session
from ..models import Equipment
from ..schemas import (
    AvailabilityResponse,
    CatalogResponse,
    CategoryRead,
    EquipmentDetail,
    EquipmentListItem,
    LandingStats,
    LocationRead,
)
from ..services import catalog_service

router = APIRouter(prefix="/api/catalog", tags=["catalog"])


@router.get("", response_model=CatalogResponse)
def get_catalog(
    session: Session = Depends(get_session),
    category: str | None = Query(default=None),
    search: str | None = Query(default=None),
    tag: str | None = Query(default=None),
) -> CatalogResponse:
    categories = catalog_service.list_categories(session)
    equipment_items = catalog_service.list_equipment(session, category_slug=category, search=search)
    available_tags = catalog_service.extract_unique_tags(equipment_items)
    equipment = catalog_service.filter_equipment_by_tag(equipment_items, tag)
    featured_items = catalog_service.get_featured_equipment(session)
    featured = catalog_service.filter_equipment_by_tag(featured_items, tag)

    return CatalogResponse(
        categories=categories,
        featured=featured,
        equipment=equipment,
        available_tags=available_tags,
    )


@router.get("/categories", response_model=list[CategoryRead])
def get_categories(session: Session = Depends(get_session)) -> list[CategoryRead]:
    return catalog_service.list_categories(session)


@router.get("/equipment", response_model=list[EquipmentListItem])
def get_equipment(
    session: Session = Depends(get_session),
    category: str | None = Query(default=None),
    search: str | None = Query(default=None),
    featured: bool = Query(default=False),
    tag: str | None = Query(default=None),
) -> list[EquipmentListItem]:
    equipment_items = catalog_service.list_equipment(
        session,
        category_slug=category,
        search=search,
        featured_only=featured,
    )
    return catalog_service.filter_equipment_by_tag(equipment_items, tag)


@router.get("/equipment/{slug}", response_model=EquipmentDetail)
def get_equipment_detail(slug: str, session: Session = Depends(get_session)) -> EquipmentDetail:
    return catalog_service.get_equipment_detail(session, slug)


@router.get("/equipment/{slug}/availability", response_model=AvailabilityResponse)
def check_availability(
    slug: str,
    start_date: date = Query(..., description="Rental start date"),
    end_date: date = Query(..., description="Rental end date"),
    session: Session = Depends(get_session),
) -> AvailabilityResponse:
    equipment = session.exec(select(Equipment).where(Equipment.slug == slug)).first()
    if not equipment:
        raise HTTPException(status_code=404, detail="Equipment not found")
    if start_date >= end_date:
        raise HTTPException(status_code=400, detail="End date must be after start date")
    return catalog_service.calculate_availability(session, equipment=equipment, start_date=start_date, end_date=end_date)


@router.get("/landing", response_model=LandingStats)
def get_landing_stats(session: Session = Depends(get_session)) -> LandingStats:
    return catalog_service.compute_landing_stats(session)


@router.get("/locations", response_model=list[LocationRead])
def get_locations(session: Session = Depends(get_session)) -> list[LocationRead]:
    return catalog_service.list_locations(session)
