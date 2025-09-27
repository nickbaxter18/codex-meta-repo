from __future__ import annotations

import enum
from datetime import datetime, date
from typing import List, Optional

from sqlalchemy import Column, DateTime, JSON, String, event
from sqlalchemy.sql import func
from sqlmodel import Field, Relationship, SQLModel


# Timestamp fields will be added directly to each model


class UserRole(str, enum.Enum):
    ADMIN = "admin"
    MANAGER = "manager"
    CUSTOMER = "customer"


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: int | None = Field(default=None, primary_key=True)
    email: str = Field(index=True, nullable=False, unique=True)
    full_name: str = Field(nullable=False)
    hashed_password: str = Field(nullable=False)
    role: UserRole = Field(default=UserRole.CUSTOMER)
    is_active: bool = Field(default=True, nullable=False)
    created_at: datetime | None = Field(
        default_factory=datetime.utcnow,
        sa_column=Column(DateTime(timezone=True), server_default=func.now()),
    )
    updated_at: datetime | None = Field(
        default_factory=datetime.utcnow,
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now()),
    )

    customer_profile: Optional[CustomerProfile] = Relationship(back_populates="user")
    reservations: List[Reservation] = Relationship(back_populates="customer")


class CustomerProfile(SQLModel, table=True):
    __tablename__ = "customer_profiles"

    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id", nullable=False)
    phone_number: str | None = Field(default=None)
    company_name: str | None = Field(default=None)
    preferred_contact_method: str | None = Field(default=None)
    loyalty_tier: str = Field(default="Standard")
    created_at: datetime | None = Field(
        default_factory=datetime.utcnow,
        sa_column=Column(DateTime(timezone=True), server_default=func.now()),
    )
    updated_at: datetime | None = Field(
        default_factory=datetime.utcnow,
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now()),
    )

    user: User = Relationship(back_populates="customer_profile")


class Category(SQLModel, table=True):
    __tablename__ = "categories"

    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(nullable=False, unique=True)
    slug: str = Field(nullable=False, unique=True, index=True)
    description: str | None = Field(default=None)
    icon: str | None = Field(default=None)

    equipment: List[Equipment] = Relationship(back_populates="category")


class Location(SQLModel, table=True):
    __tablename__ = "locations"

    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(nullable=False)
    address_line1: str = Field(nullable=False)
    address_line2: str | None = Field(default=None)
    city: str = Field(nullable=False)
    state: str = Field(nullable=False)
    postal_code: str = Field(nullable=False)
    country: str = Field(nullable=False, default="USA")
    latitude: float | None = Field(default=None)
    longitude: float | None = Field(default=None)
    phone_number: str | None = Field(default=None)

    reservations: List[Reservation] = Relationship(back_populates="location")


class Equipment(SQLModel, table=True):
    __tablename__ = "equipment"

    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(nullable=False)
    slug: str = Field(nullable=False, unique=True, index=True)
    summary: str = Field(nullable=False)
    description: str | None = Field(default=None)
    category_id: int = Field(foreign_key="categories.id", nullable=False)
    daily_rate: float = Field(nullable=False)
    deposit_amount: float = Field(default=0.0)
    replacement_cost: float | None = Field(default=None)
    availability_count: int = Field(default=1)
    min_rental_days: int = Field(default=1)
    max_rental_days: int | None = Field(default=None)
    featured: bool = Field(default=False)
    tags: list[str] = Field(default_factory=list, sa_column=Column(JSON))
    specifications: dict | None = Field(default=None, sa_column=Column(JSON))

    category: Category = Relationship(back_populates="equipment")
    media: List[EquipmentMedia] = Relationship(back_populates="equipment")
    reservations: List[Reservation] = Relationship(back_populates="equipment")
    maintenance_logs: List[MaintenanceLog] = Relationship(back_populates="equipment")
    reviews: List[Review] = Relationship(back_populates="equipment")


class EquipmentMedia(SQLModel, table=True):
    __tablename__ = "equipment_media"

    id: int | None = Field(default=None, primary_key=True)
    equipment_id: int = Field(foreign_key="equipment.id", nullable=False)
    url: str = Field(nullable=False)
    alt_text: str | None = Field(default=None)
    is_primary: bool = Field(default=False)
    media_type: str = Field(default="image")

    equipment: Equipment = Relationship(back_populates="media")


class ReservationStatus(str, enum.Enum):
    DRAFT = "draft"
    PENDING = "pending"
    CONFIRMED = "confirmed"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class PaymentStatus(str, enum.Enum):
    UNPAID = "unpaid"
    DEPOSIT_PAID = "deposit_paid"
    PAID_IN_FULL = "paid_in_full"
    REFUNDED = "refunded"


class Reservation(SQLModel, table=True):
    __tablename__ = "reservations"

    id: int | None = Field(default=None, primary_key=True)
    reservation_code: str = Field(nullable=False, unique=True, index=True)
    customer_id: int | None = Field(default=None, foreign_key="users.id")
    customer_name: str = Field(nullable=False)
    customer_email: str = Field(nullable=False)
    customer_phone: str | None = Field(default=None)
    equipment_id: int = Field(foreign_key="equipment.id", nullable=False)
    location_id: int = Field(foreign_key="locations.id", nullable=False)
    start_date: date = Field(nullable=False)
    end_date: date = Field(nullable=False)
    total_days: int = Field(nullable=False)
    subtotal_amount: float = Field(nullable=False)
    deposit_amount: float = Field(default=0.0)
    total_amount: float = Field(nullable=False)
    status: ReservationStatus = Field(default=ReservationStatus.PENDING)
    payment_status: PaymentStatus = Field(default=PaymentStatus.UNPAID)
    notes: str | None = Field(default=None)

    equipment: Equipment = Relationship(back_populates="reservations")
    location: Location = Relationship(back_populates="reservations")
    customer: Optional[User] = Relationship(back_populates="reservations")


class MaintenanceStatus(str, enum.Enum):
    SCHEDULED = "scheduled"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    OUT_OF_SERVICE = "out_of_service"


class MaintenanceLog(SQLModel, table=True):
    __tablename__ = "maintenance_logs"

    id: int | None = Field(default=None, primary_key=True)
    equipment_id: int = Field(foreign_key="equipment.id", nullable=False)
    performed_at: datetime = Field(default_factory=datetime.utcnow)
    status: MaintenanceStatus = Field(default=MaintenanceStatus.SCHEDULED)
    technician_name: str | None = Field(default=None)
    notes: str | None = Field(default=None)

    equipment: Equipment = Relationship(back_populates="maintenance_logs")


class Review(SQLModel, table=True):
    __tablename__ = "reviews"

    id: int | None = Field(default=None, primary_key=True)
    equipment_id: int = Field(foreign_key="equipment.id", nullable=False)
    author_name: str = Field(nullable=False)
    author_company: str | None = Field(default=None)
    rating: int = Field(ge=1, le=5, nullable=False)
    headline: str | None = Field(default=None)
    comment: str | None = Field(default=None)
    published: bool = Field(default=True)

    equipment: Equipment = Relationship(back_populates="reviews")


class AnalyticsDailySummary(SQLModel, table=True):
    __tablename__ = "analytics_daily_summary"

    date: date = Field(primary_key=True)
    total_reservations: int = Field(default=0)
    total_revenue: float = Field(default=0.0)
    new_customers: int = Field(default=0)
    average_order_value: float = Field(default=0.0)
    utilization_rate: float = Field(default=0.0)


# SQLAlchemy event to auto-update timestamps
from sqlalchemy.orm import Mapper  # noqa: E402


def _set_timestamp_before_update(mapper: Mapper, connection, target) -> None:  # type: ignore[override]
    if isinstance(target, TimestampMixin):
        target.touch()


def register_timestamp_events() -> None:
    for model_cls in [User, CustomerProfile, Category, Location, Equipment, EquipmentMedia, Reservation, MaintenanceLog, Review]:
        event.listen(model_cls, "before_update", _set_timestamp_before_update)


register_timestamp_events()
