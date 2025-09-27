from datetime import date, timedelta

from sqlmodel import Session, select

from ..models import (
    Category,
    Equipment,
    EquipmentMedia,
    Location,
    MaintenanceLog,
    MaintenanceStatus,
    Reservation,
    ReservationStatus,
    Review,
    User,
    UserRole,
)
from ..security import hash_password
from ..utils.identifiers import generate_reservation_code


CATEGORY_DATA = [
    {
        "slug": "earth-moving",
        "name": "Earth Moving",
        "description": "Excavators, backhoes, and earth movers for construction sites.",
        "icon": "shovel",
    },
    {
        "slug": "power-lighting",
        "name": "Power & Lighting",
        "description": "Portable generators, light towers, and power distribution.",
        "icon": "bolt",
    },
    {
        "slug": "site-services",
        "name": "Site Services",
        "description": "Fencing, sanitation, and temporary structures.",
        "icon": "map",
    },
]

EQUIPMENT_DATA = [
    {
        "slug": "volvo-ecr88d",
        "name": "Volvo ECR88D Excavator",
        "summary": "Compact radius excavator ideal for urban excavation projects.",
        "description": "Fuel-efficient excavator with advanced hydraulics, zero tail swing, and multiple bucket options.",
        "category_slug": "earth-moving",
        "daily_rate": 525.0,
        "deposit_amount": 2000.0,
        "replacement_cost": 115000.0,
        "availability_count": 6,
        "min_rental_days": 2,
        "tags": ["excavator", "diesel", "gps-ready"],
        "specifications": {
            "Operating Weight": "19,010 lbs",
            "Engine Power": "55 kW",
            "Max Dig Depth": "15 ft 1 in",
        },
        "media": [
            {
                "url": "https://images.unsplash.com/photo-1509395176047-4a66953fd231",
                "alt_text": "Volvo excavator on construction site",
                "is_primary": True,
            }
        ],
    },
    {
        "slug": "generac-gp8000e",
        "name": "Generac GP8000E Generator",
        "summary": "Electric start generator with 10,000 starting watts.",
        "description": "Reliable portable generator with idle control, covered outlets, and large fuel tank for extended runtime.",
        "category_slug": "power-lighting",
        "daily_rate": 145.0,
        "deposit_amount": 600.0,
        "replacement_cost": 1800.0,
        "availability_count": 14,
        "tags": ["generator", "electric-start", "power"],
        "specifications": {
            "Running Watts": "8,000",
            "Engine": "Generac OHV",
            "Fuel Tank": "7.9 gal",
        },
        "media": [
            {
                "url": "https://images.unsplash.com/photo-1610484826967-09c572c08216",
                "alt_text": "Portable generator on jobsite",
                "is_primary": True,
            }
        ],
    },
    {
        "slug": "skyjack-sj45t",
        "name": "Skyjack SJ45 T Boom Lift",
        "summary": "45 ft telescopic boom lift with rough terrain package.",
        "description": "4WD boom lift featuring 45 ft platform height, axle-based 4WD, and skycoded control system.",
        "category_slug": "site-services",
        "daily_rate": 420.0,
        "deposit_amount": 1500.0,
        "replacement_cost": 84000.0,
        "availability_count": 4,
        "tags": ["boom-lift", "telescopic", "4wd"],
        "specifications": {
            "Platform Height": "45 ft",
            "Platform Capacity": "660 lbs",
            "Horizontal Reach": "36 ft",
        },
        "media": [
            {
                "url": "https://images.unsplash.com/photo-1517344934927-31c8a0b2805e",
                "alt_text": "Telescopic boom lift working on warehouse",
                "is_primary": True,
            }
        ],
    },
]

LOCATION_DATA = [
    {
        "name": "Denver Logistics Hub",
        "address_line1": "1450 Market Street",
        "city": "Denver",
        "state": "CO",
        "postal_code": "80202",
        "country": "USA",
        "phone_number": "+1-303-555-0123",
    },
    {
        "name": "Phoenix Service Yard",
        "address_line1": "220 Industrial Way",
        "city": "Phoenix",
        "state": "AZ",
        "postal_code": "85004",
        "country": "USA",
        "phone_number": "+1-602-555-0199",
    },
]

REVIEWS_DATA = [
    {
        "equipment_slug": "volvo-ecr88d",
        "author_name": "Jordan Michaels",
        "author_company": "Summit Peak Construction",
        "rating": 5,
        "headline": "Seamless excavation, every time",
        "comment": "The Volvo ECR88D has been a workhorse for our downtown projects. Delivery, training, and pickup were flawless.",
    },
    {
        "equipment_slug": "generac-gp8000e",
        "author_name": "Priya Patel",
        "author_company": "SolarGrid Installers",
        "rating": 4,
        "headline": "Reliable auxiliary power",
        "comment": "Quiet operation and long runtime kept our crews productive during planned outages.",
    },
]


def seed_initial_data(session: Session) -> None:
    category_exists = session.exec(select(Category)).first()
    if category_exists:
        return

    categories: dict[str, Category] = {}
    for payload in CATEGORY_DATA:
        category = Category(**payload)
        session.add(category)
        categories[payload["slug"]] = category

    session.commit()

    locations: list[Location] = []
    for payload in LOCATION_DATA:
        location = Location(**payload)
        session.add(location)
        locations.append(location)

    session.commit()

    for equipment_payload in EQUIPMENT_DATA:
        category = categories[equipment_payload.pop("category_slug")]
        media_payloads = equipment_payload.pop("media", [])
        equipment = Equipment(category_id=category.id, **equipment_payload)  # type: ignore[arg-type]
        session.add(equipment)
        session.commit()

        for media_payload in media_payloads:
            media = EquipmentMedia(equipment_id=equipment.id, **media_payload)
            session.add(media)

        maintenance_log = MaintenanceLog(
            equipment_id=equipment.id,
            status=MaintenanceStatus.COMPLETED,
            notes="Factory certified inspection completed within the last 30 days.",
        )
        session.add(maintenance_log)

    session.commit()

    for review_payload in REVIEWS_DATA:
        equipment = session.exec(select(Equipment).where(Equipment.slug == review_payload.pop("equipment_slug"))).one()
        review = Review(equipment_id=equipment.id, **review_payload)
        session.add(review)

    session.commit()

    admin_exists = session.exec(select(User).where(User.email == "admin@u-dig-it.com")).first()
    if not admin_exists:
        session.add(
            User(
                email="admin@u-dig-it.com",
                full_name="U-DIG-IT Admin",
                hashed_password=hash_password("ChangeMe123!"),
                role=UserRole.ADMIN,
            )
        )
        session.commit()

    first_equipment = session.exec(select(Equipment)).first()
    first_location = locations[0] if locations else None
    if first_equipment and first_location:
        session.add(
            Reservation(
                reservation_code=generate_reservation_code(),
                customer_name="Sample Customer",
                customer_email="sample.customer@example.com",
                equipment_id=first_equipment.id,
                location_id=first_location.id,
                start_date=date.today() + timedelta(days=3),
                end_date=date.today() + timedelta(days=6),
                total_days=3,
                subtotal_amount=first_equipment.daily_rate * 3,
                deposit_amount=first_equipment.deposit_amount,
                total_amount=first_equipment.daily_rate * 3 + first_equipment.deposit_amount,
                status=ReservationStatus.CONFIRMED,
            )
        )
        session.commit()
