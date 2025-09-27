from __future__ import annotations

from datetime import date, datetime
from typing import List, Optional

from pydantic import BaseModel, EmailStr, Field

from .models import PaymentStatus, ReservationStatus, UserRole


# --------- Auth Schemas ---------


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int


class UserBase(BaseModel):
    email: EmailStr
    full_name: str
    role: UserRole = UserRole.CUSTOMER


class UserPublic(UserBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True


class UserCreate(UserBase):
    password: str = Field(min_length=8)
    phone_number: str | None = None
    company_name: str | None = None


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class CustomerProfilePublic(BaseModel):
    id: int
    phone_number: str | None
    company_name: str | None
    preferred_contact_method: str | None
    loyalty_tier: str

    class Config:
        from_attributes = True


class AuthenticatedUser(UserPublic):
    customer_profile: CustomerProfilePublic | None = None


# --------- Catalog Schemas ---------


class CategoryBase(BaseModel):
    slug: str
    name: str
    description: str | None = None
    icon: str | None = None


class CategoryRead(CategoryBase):
    id: int
    equipment_count: int = 0

    class Config:
        from_attributes = True


class LocationRead(BaseModel):
    id: int
    name: str
    address_line1: str
    address_line2: str | None = None
    city: str
    state: str
    postal_code: str
    country: str
    phone_number: str | None = None

    class Config:
        from_attributes = True


class EquipmentMediaRead(BaseModel):
    id: int
    url: str
    alt_text: str | None = None
    is_primary: bool
    media_type: str

    class Config:
        from_attributes = True


class ReviewRead(BaseModel):
    id: int
    author_name: str
    author_company: str | None = None
    rating: int
    headline: str | None = None
    comment: str | None = None
    published: bool
    created_at: datetime | None = None

    class Config:
        from_attributes = True


class EquipmentListItem(BaseModel):
    id: int
    name: str
    slug: str
    summary: str
    daily_rate: float
    deposit_amount: float
    featured: bool
    tags: list[str]
    primary_image: str | None = None
    average_rating: float | None = None
    review_count: int = 0
    category: CategoryBase


class EquipmentDetail(EquipmentListItem):
    description: str | None = None
    specifications: dict | None = None
    gallery: list[EquipmentMediaRead] = Field(default_factory=list)
    maintenance_statuses: list[str] = Field(default_factory=list)
    reviews: list[ReviewRead] = Field(default_factory=list)


class CatalogResponse(BaseModel):
    categories: list[CategoryRead]
    featured: list[EquipmentListItem]
    equipment: list[EquipmentListItem]
    available_tags: list[str] = Field(default_factory=list)


class AvailabilityResponse(BaseModel):
    equipment_id: int
    equipment_name: str
    available_quantity: int
    is_available: bool


class LandingStats(BaseModel):
    total_inventory: int
    active_customers: int
    locations_served: int
    on_time_delivery_rate: float
    average_rating: float
    featured_testimonials: list[ReviewRead] = Field(default_factory=list)


# --------- Reservation Schemas ---------


class ReservationBase(BaseModel):
    equipment_slug: str
    location_id: int
    start_date: date
    end_date: date
    customer_name: str
    customer_email: EmailStr
    customer_phone: str | None = None
    notes: str | None = None


class ReservationCreate(ReservationBase):
    customer_id: int | None = None


class ReservationRead(BaseModel):
    reservation_code: str
    status: ReservationStatus
    payment_status: PaymentStatus
    start_date: date
    end_date: date
    total_days: int
    subtotal_amount: float
    deposit_amount: float
    total_amount: float
    equipment: EquipmentListItem


class ReservationListItem(BaseModel):
    reservation_code: str
    status: ReservationStatus
    total_amount: float
    start_date: date
    end_date: date
    customer_name: str


class ReservationSuccessResponse(BaseModel):
    reservation: ReservationRead
    message: str


class ReservationUpdate(BaseModel):
    status: ReservationStatus | None = None
    payment_status: PaymentStatus | None = None
    notes: str | None = None


# --------- Analytics ---------


class AnalyticsSummary(BaseModel):
    date: date
    total_reservations: int
    total_revenue: float
    new_customers: int
    average_order_value: float
    utilization_rate: float


class TopEquipmentPerformance(BaseModel):
    equipment: EquipmentListItem
    revenue: float
    reservation_count: int


class DashboardSnapshot(BaseModel):
    reservations: list[ReservationListItem] = Field(default_factory=list)
    analytics: list[AnalyticsSummary] = Field(default_factory=list)
    top_equipment: list[TopEquipmentPerformance] = Field(default_factory=list)
