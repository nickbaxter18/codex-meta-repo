"""
Integration tests for API endpoints.
"""
import pytest
from fastapi.testclient import TestClient


class TestHealthEndpoint:
    """Test health check endpoint."""
    
    def test_health_check(self, test_client: TestClient):
        """Test that health endpoint returns 200."""
        response = test_client.get("/health")
        assert response.status_code == 200
        assert "status" in response.json()


class TestAuthEndpoints:
    """Test authentication endpoints."""
    
    def test_register_endpoint(self, test_client: TestClient):
        """Test user registration endpoint."""
        user_data = {
            "email": "newuser@example.com",
            "fullName": "New User",
            "password": "newpassword123"
        }
        
        response = test_client.post("/api/auth/register", json=user_data)
        assert response.status_code == 201
        
        data = response.json()
        assert "accessToken" in data
        assert "expiresIn" in data
    
    def test_register_duplicate_email(self, test_client: TestClient, sample_user):
        """Test registration with duplicate email fails."""
        user_data = {
            "email": sample_user.email,
            "fullName": "Another User",
            "password": "password123"
        }
        
        response = test_client.post("/api/auth/register", json=user_data)
        assert response.status_code == 409
    
    def test_login_endpoint(self, test_client: TestClient, sample_user):
        """Test user login endpoint."""
        login_data = {
            "username": sample_user.email,
            "password": "testpassword123"
        }
        
        response = test_client.post("/api/auth/login", data=login_data)
        assert response.status_code == 200
        
        data = response.json()
        assert "access_token" in data
        assert "expires_in" in data
    
    def test_login_invalid_credentials(self, test_client: TestClient):
        """Test login with invalid credentials."""
        login_data = {
            "username": "nonexistent@example.com",
            "password": "wrongpassword"
        }
        
        response = test_client.post("/api/auth/login", data=login_data)
        assert response.status_code == 401
    
    def test_me_endpoint(self, test_client: TestClient, auth_headers):
        """Test getting current user info."""
        response = test_client.get("/api/auth/me", headers=auth_headers)
        assert response.status_code == 200
        
        data = response.json()
        assert "email" in data
        assert "fullName" in data
        assert "role" in data
    
    def test_me_endpoint_unauthorized(self, test_client: TestClient):
        """Test me endpoint without authentication."""
        response = test_client.get("/api/auth/me")
        assert response.status_code == 401


class TestCatalogEndpoints:
    """Test catalog endpoints."""
    
    def test_get_catalog(self, test_client: TestClient):
        """Test getting catalog data."""
        response = test_client.get("/api/catalog")
        assert response.status_code == 200
        
        data = response.json()
        assert "categories" in data
        assert "featured" in data
        assert "equipment" in data
    
    def test_get_catalog_with_category_filter(self, test_client: TestClient, sample_category):
        """Test catalog with category filter."""
        response = test_client.get(f"/api/catalog?category={sample_category.slug}")
        assert response.status_code == 200
        
        data = response.json()
        assert "categories" in data
        assert "equipment" in data
    
    def test_get_categories(self, test_client: TestClient):
        """Test getting categories list."""
        response = test_client.get("/api/catalog/categories")
        assert response.status_code == 200
        
        data = response.json()
        assert isinstance(data, list)
    
    def test_get_equipment_detail(self, test_client: TestClient, sample_equipment):
        """Test getting equipment detail."""
        response = test_client.get(f"/api/catalog/equipment/{sample_equipment.slug}")
        assert response.status_code == 200
        
        data = response.json()
        assert data["name"] == sample_equipment.name
        assert data["slug"] == sample_equipment.slug
    
    def test_get_equipment_availability(self, test_client: TestClient, sample_equipment):
        """Test getting equipment availability."""
        response = test_client.get(
            f"/api/catalog/equipment/{sample_equipment.slug}/availability",
            params={"startDate": "2024-01-01", "endDate": "2024-01-07"}
        )
        assert response.status_code == 200
        
        data = response.json()
        assert "available" in data
        assert "conflicts" in data
    
    def test_get_locations(self, test_client: TestClient):
        """Test getting locations list."""
        response = test_client.get("/api/catalog/locations")
        assert response.status_code == 200
        
        data = response.json()
        assert isinstance(data, list)


class TestReservationEndpoints:
    """Test reservation endpoints."""
    
    def test_create_reservation(self, test_client: TestClient, auth_headers, sample_equipment):
        """Test creating a reservation."""
        reservation_data = {
            "equipmentId": sample_equipment.id,
            "startDate": "2024-01-01",
            "endDate": "2024-01-07",
            "notes": "Test reservation"
        }
        
        response = test_client.post(
            "/api/reservations",
            json=reservation_data,
            headers=auth_headers
        )
        assert response.status_code == 201
        
        data = response.json()
        assert "reservationCode" in data
        assert "status" in data
    
    def test_create_reservation_unauthorized(self, test_client: TestClient, sample_equipment):
        """Test creating reservation without authentication."""
        reservation_data = {
            "equipmentId": sample_equipment.id,
            "startDate": "2024-01-01",
            "endDate": "2024-01-07"
        }
        
        response = test_client.post("/api/reservations", json=reservation_data)
        assert response.status_code == 401
    
    def test_get_user_reservations(self, test_client: TestClient, auth_headers):
        """Test getting user's reservations."""
        response = test_client.get("/api/reservations", headers=auth_headers)
        assert response.status_code == 200
        
        data = response.json()
        assert isinstance(data, list)
    
    def test_get_user_reservations_unauthorized(self, test_client: TestClient):
        """Test getting reservations without authentication."""
        response = test_client.get("/api/reservations")
        assert response.status_code == 401


class TestAnalyticsEndpoints:
    """Test analytics endpoints."""
    
    def test_get_dashboard_snapshot_admin(self, test_client: TestClient, admin_auth_headers):
        """Test getting dashboard snapshot as admin."""
        response = test_client.get("/api/analytics/dashboard", headers=admin_auth_headers)
        assert response.status_code == 200
        
        data = response.json()
        assert "totalReservations" in data
        assert "totalRevenue" in data
        assert "topEquipment" in data
    
    def test_get_dashboard_snapshot_unauthorized(self, test_client: TestClient):
        """Test getting dashboard snapshot without authentication."""
        response = test_client.get("/api/analytics/dashboard")
        assert response.status_code == 401
    
    def test_get_dashboard_snapshot_customer(self, test_client: TestClient, auth_headers):
        """Test getting dashboard snapshot as customer (should fail)."""
        response = test_client.get("/api/analytics/dashboard", headers=auth_headers)
        assert response.status_code == 403


class TestErrorHandling:
    """Test error handling across endpoints."""
    
    def test_404_for_nonexistent_equipment(self, test_client: TestClient):
        """Test 404 for nonexistent equipment."""
        response = test_client.get("/api/catalog/equipment/nonexistent")
        assert response.status_code == 404
    
    def test_400_for_invalid_date_range(self, test_client: TestClient, sample_equipment):
        """Test 400 for invalid date range."""
        response = test_client.get(
            f"/api/catalog/equipment/{sample_equipment.slug}/availability",
            params={"startDate": "2024-01-07", "endDate": "2024-01-01"}  # End before start
        )
        assert response.status_code == 400
    
    def test_422_for_invalid_json(self, test_client: TestClient):
        """Test 422 for invalid JSON in request body."""
        response = test_client.post(
            "/api/auth/register",
            data="invalid json",
            headers={"Content-Type": "application/json"}
        )
        assert response.status_code == 422


class TestCORSHeaders:
    """Test CORS headers are properly set."""
    
    def test_cors_headers(self, test_client: TestClient):
        """Test that CORS headers are present."""
        response = test_client.options("/api/catalog")
        assert response.status_code == 200
        
        # Check for CORS headers
        assert "Access-Control-Allow-Origin" in response.headers
        assert "Access-Control-Allow-Methods" in response.headers
        assert "Access-Control-Allow-Headers" in response.headers

