from __future__ import annotations

import enum
from datetime import datetime, date
from typing import List, Optional

from sqlalchemy import Column, DateTime
from sqlalchemy.sql import func
from sqlmodel import Field, Relationship, SQLModel


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
    created_at: datetime | None = Field(
        default_factory=datetime.utcnow,
        sa_column=Column(DateTime(timezone=True), server_default=func.now()),
    )
    updated_at: datetime | None = Field(
        default_factory=datetime.utcnow,
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now()),
    )

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
    country: str = Field(default="US")
    phone_number: str | None = Field(default=None)
    created_at: datetime | None = Field(
        default_factory=datetime.utcnow,
        sa_column=Column(DateTime(timezone=True), server_default=func.now()),
    )
    updated_at: datetime | None = Field(
        default_factory=datetime.utcnow,
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now()),
    )

    reservations: List[Reservation] = Relationship(back_populates="location")


class Equipment(SQLModel, table=True):
    __tablename__ = "equipment"

    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(nullable=False)
    slug: str = Field(nullable=False, unique=True, index=True)
    description: str | None = Field(default=None)
    category_id: int = Field(foreign_key="categories.id", nullable=False)
    daily_rate: float = Field(nullable=False)
    is_available: bool = Field(default=True, nullable=False)
    created_at: datetime | None = Field(
        default_factory=datetime.utcnow,
        sa_column=Column(DateTime(timezone=True), server_default=func.now()),
    )
    updated_at: datetime | None = Field(
        default_factory=datetime.utcnow,
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now()),
    )

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
    created_at: datetime | None = Field(
        default_factory=datetime.utcnow,
        sa_column=Column(DateTime(timezone=True), server_default=func.now()),
    )
    updated_at: datetime | None = Field(
        default_factory=datetime.utcnow,
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now()),
    )

    equipment: Equipment = Relationship(back_populates="media")


class ReservationStatus(str, enum.Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class PaymentStatus(str, enum.Enum):
    PENDING = "pending"
    DEPOSIT_PAID = "deposit_paid"
    PAID_IN_FULL = "paid_in_full"
    REFUNDED = "refunded"


class Reservation(SQLModel, table=True):
    __tablename__ = "reservations"

    id: int | None = Field(default=None, primary_key=True)
    reservation_code: str = Field(nullable=False, unique=True, index=True)
    customer_id: int | None = Field(default=None, foreign_key="users.id")
    equipment_id: int = Field(foreign_key="equipment.id", nullable=False)
    location_id: int = Field(foreign_key="locations.id", nullable=False)
    start_date: date = Field(nullable=False)
    end_date: date = Field(nullable=False)
    total_cost: float = Field(nullable=False)
    status: ReservationStatus = Field(default=ReservationStatus.PENDING)
    payment_status: PaymentStatus = Field(default=PaymentStatus.PENDING)
    notes: str | None = Field(default=None)
    created_at: datetime | None = Field(
        default_factory=datetime.utcnow,
        sa_column=Column(DateTime(timezone=True), server_default=func.now()),
    )
    updated_at: datetime | None = Field(
        default_factory=datetime.utcnow,
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now()),
    )

    customer: Optional[User] = Relationship(back_populates="reservations")
    equipment: Equipment = Relationship(back_populates="reservations")
    location: Location = Relationship(back_populates="reservations")


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
    notes: str | None = Field(default=None)
    created_at: datetime | None = Field(
        default_factory=datetime.utcnow,
        sa_column=Column(DateTime(timezone=True), server_default=func.now()),
    )
    updated_at: datetime | None = Field(
        default_factory=datetime.utcnow,
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now()),
    )

    equipment: Equipment = Relationship(back_populates="maintenance_logs")


class Review(SQLModel, table=True):
    __tablename__ = "reviews"

    id: int | None = Field(default=None, primary_key=True)
    equipment_id: int = Field(foreign_key="equipment.id", nullable=False)
    author_name: str = Field(nullable=False)
    rating: int = Field(nullable=False, ge=1, le=5)
    comment: str | None = Field(default=None)
    created_at: datetime | None = Field(
        default_factory=datetime.utcnow,
        sa_column=Column(DateTime(timezone=True), server_default=func.now()),
    )
    updated_at: datetime | None = Field(
        default_factory=datetime.utcnow,
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now()),
    )

    equipment: Equipment = Relationship(back_populates="reviews")


class AnalyticsDailySummary(SQLModel, table=True):
    __tablename__ = "analytics_daily_summary"

    date: date = Field(primary_key=True)
    total_reservations: int = Field(default=0)
    total_revenue: float = Field(default=0.0)
    new_customers: int = Field(default=0)
    average_order_value: float = Field(default=0.0)
    utilization_rate: float = Field(default=0.0)
    created_at: datetime | None = Field(
        default_factory=datetime.utcnow,
        sa_column=Column(DateTime(timezone=True), server_default=func.now()),
    )
    updated_at: datetime | None = Field(
        default_factory=datetime.utcnow,
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now()),
    )
