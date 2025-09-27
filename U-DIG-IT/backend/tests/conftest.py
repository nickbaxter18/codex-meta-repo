"""
Pytest configuration and shared fixtures for U-DIG-IT backend tests.
"""
import os
import tempfile
from typing import Generator
from unittest.mock import Mock

import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, create_engine, SQLModel
from sqlalchemy.pool import StaticPool

from app.main import app
from app.database import get_session
from app.models import User, UserRole, Category, Equipment, Location
from app.security import hash_password


@pytest.fixture(scope="session")
def test_db_url() -> str:
    """Create a temporary SQLite database for testing."""
    return "sqlite:///./test.db"


@pytest.fixture(scope="function")
def test_engine(test_db_url: str):
    """Create a test database engine."""
    engine = create_engine(
        test_db_url,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    SQLModel.metadata.create_all(engine)
    yield engine
    SQLModel.metadata.drop_all(engine)


@pytest.fixture(scope="function")
def test_session(test_engine) -> Generator[Session, None, None]:
    """Create a test database session."""
    with Session(test_engine) as session:
        yield session


@pytest.fixture(scope="function")
def test_client(test_session: Session) -> Generator[TestClient, None, None]:
    """Create a test client with database dependency override."""
    def get_test_session():
        return test_session
    
    app.dependency_overrides[get_session] = get_test_session
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()


@pytest.fixture
def sample_user(test_session: Session) -> User:
    """Create a sample user for testing."""
    user = User(
        email="test@example.com",
        full_name="Test User",
        hashed_password=hash_password("testpassword123"),
        role=UserRole.CUSTOMER,
        is_active=True
    )
    test_session.add(user)
    test_session.commit()
    test_session.refresh(user)
    return user


@pytest.fixture
def sample_admin_user(test_session: Session) -> User:
    """Create a sample admin user for testing."""
    user = User(
        email="admin@example.com",
        full_name="Admin User",
        hashed_password=hash_password("adminpassword123"),
        role=UserRole.ADMIN,
        is_active=True
    )
    test_session.add(user)
    test_session.commit()
    test_session.refresh(user)
    return user


@pytest.fixture
def sample_category(test_session: Session) -> Category:
    """Create a sample category for testing."""
    category = Category(
        name="Test Category",
        slug="test-category",
        description="A test category",
        icon="test-icon"
    )
    test_session.add(category)
    test_session.commit()
    test_session.refresh(category)
    return category


@pytest.fixture
def sample_location(test_session: Session) -> Location:
    """Create a sample location for testing."""
    location = Location(
        name="Test Location",
        address="123 Test Street",
        city="Test City",
        state="TS",
        zip_code="12345",
        phone="555-0123",
        email="location@test.com"
    )
    test_session.add(location)
    test_session.commit()
    test_session.refresh(location)
    return location


@pytest.fixture
def sample_equipment(test_session: Session, sample_category: Category, sample_location: Location) -> Equipment:
    """Create a sample equipment item for testing."""
    equipment = Equipment(
        name="Test Equipment",
        slug="test-equipment",
        description="A test equipment item",
        daily_rate=100.00,
        category_id=sample_category.id,
        location_id=sample_location.id,
        is_available=True
    )
    test_session.add(equipment)
    test_session.commit()
    test_session.refresh(equipment)
    return equipment


@pytest.fixture
def auth_headers(test_client: TestClient, sample_user: User) -> dict:
    """Get authentication headers for a test user."""
    response = test_client.post(
        "/api/auth/login",
        data={"username": sample_user.email, "password": "testpassword123"}
    )
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


@pytest.fixture
def admin_auth_headers(test_client: TestClient, sample_admin_user: User) -> dict:
    """Get authentication headers for an admin user."""
    response = test_client.post(
        "/api/auth/login",
        data={"username": sample_admin_user.email, "password": "adminpassword123"}
    )
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


@pytest.fixture
def mock_sentry():
    """Mock Sentry for testing."""
    with pytest.MonkeyPatch().context() as m:
        m.setattr("app.main.sentry_sdk", Mock())
        yield


@pytest.fixture(autouse=True)
def setup_test_env():
    """Set up test environment variables."""
    os.environ.update({
        "JWT_SECRET": "test-jwt-secret-key-for-testing-only-32-chars",
        "REFRESH_TOKEN_SECRET": "test-refresh-secret-key-for-testing-only-32-chars",
        "BACKEND_ENVIRONMENT": "test",
        "BACKEND_LOG_LEVEL": "warning"
    })
    yield
    # Cleanup
    for key in ["JWT_SECRET", "REFRESH_TOKEN_SECRET", "BACKEND_ENVIRONMENT", "BACKEND_LOG_LEVEL"]:
        os.environ.pop(key, None)

