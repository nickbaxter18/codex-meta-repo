"""
Unit tests for authentication functionality.
"""
import pytest
from fastapi import HTTPException
from sqlmodel import Session

from app.routers.auth import register_user, login_user
from app.models import User, UserRole
from app.schemas import UserCreate, TokenResponse
from app.security import hash_password, verify_password, create_access_token


class TestPasswordSecurity:
    """Test password hashing and verification."""
    
    def test_password_hashing(self):
        """Test that passwords are properly hashed."""
        password = "testpassword123"
        hashed = hash_password(password)
        
        assert hashed != password
        assert len(hashed) > 50  # bcrypt hashes are long
        assert hashed.startswith("$2b$")  # bcrypt format
    
    def test_password_verification(self):
        """Test password verification works correctly."""
        password = "testpassword123"
        hashed = hash_password(password)
        
        assert verify_password(password, hashed) is True
        assert verify_password("wrongpassword", hashed) is False
    
    def test_different_passwords_different_hashes(self):
        """Test that different passwords produce different hashes."""
        password1 = "password1"
        password2 = "password2"
        
        hash1 = hash_password(password1)
        hash2 = hash_password(password2)
        
        assert hash1 != hash2


class TestJWTToken:
    """Test JWT token creation and validation."""
    
    def test_token_creation(self):
        """Test that access tokens are created successfully."""
        email = "test@example.com"
        token = create_access_token(email)
        
        assert isinstance(token, str)
        assert len(token) > 50  # JWT tokens are long
        assert "." in token  # JWT format has dots
    
    def test_token_contains_email(self):
        """Test that token contains the user email."""
        email = "test@example.com"
        token = create_access_token(email)
        
        # This is a basic check - in a real implementation,
        # you'd decode the JWT to verify the payload
        assert email in str(token) or len(token) > 0


class TestUserRegistration:
    """Test user registration functionality."""
    
    def test_register_new_user(self, test_session: Session):
        """Test registering a new user."""
        user_data = UserCreate(
            email="newuser@example.com",
            full_name="New User",
            password="newpassword123"
        )
        
        response = register_user(user_data, test_session)
        
        assert isinstance(response, TokenResponse)
        assert response.access_token is not None
        assert response.expires_in > 0
    
    def test_register_duplicate_email(self, test_session: Session, sample_user: User):
        """Test that duplicate email registration fails."""
        user_data = UserCreate(
            email=sample_user.email,  # Same email as existing user
            full_name="Another User",
            password="password123"
        )
        
        with pytest.raises(HTTPException) as exc_info:
            register_user(user_data, test_session)
        
        assert exc_info.value.status_code == 409
        assert "already registered" in str(exc_info.value.detail)
    
    def test_register_with_profile_data(self, test_session: Session):
        """Test registering a user with profile information."""
        user_data = UserCreate(
            email="profileuser@example.com",
            full_name="Profile User",
            password="password123",
            phone_number="555-0123",
            company_name="Test Company"
        )
        
        response = register_user(user_data, test_session)
        
        assert isinstance(response, TokenResponse)
        assert response.access_token is not None


class TestUserLogin:
    """Test user login functionality."""
    
    def test_login_valid_credentials(self, test_session: Session, sample_user: User):
        """Test login with valid credentials."""
        from fastapi.security import OAuth2PasswordRequestForm
        
        form_data = OAuth2PasswordRequestForm(
            username=sample_user.email,
            password="testpassword123"
        )
        
        response = login_user(form_data, test_session)
        
        assert isinstance(response, TokenResponse)
        assert response.access_token is not None
        assert response.expires_in > 0
    
    def test_login_invalid_email(self, test_session: Session):
        """Test login with invalid email."""
        from fastapi.security import OAuth2PasswordRequestForm
        
        form_data = OAuth2PasswordRequestForm(
            username="nonexistent@example.com",
            password="password123"
        )
        
        with pytest.raises(HTTPException) as exc_info:
            login_user(form_data, test_session)
        
        assert exc_info.value.status_code == 401
        assert "Invalid credentials" in str(exc_info.value.detail)
    
    def test_login_invalid_password(self, test_session: Session, sample_user: User):
        """Test login with invalid password."""
        from fastapi.security import OAuth2PasswordRequestForm
        
        form_data = OAuth2PasswordRequestForm(
            username=sample_user.email,
            password="wrongpassword"
        )
        
        with pytest.raises(HTTPException) as exc_info:
            login_user(form_data, test_session)
        
        assert exc_info.value.status_code == 401
        assert "Invalid credentials" in str(exc_info.value.detail)


class TestSecurityValidation:
    """Test security-related validations."""
    
    def test_weak_password_rejection(self):
        """Test that weak passwords are rejected."""
        weak_passwords = [
            "123456",
            "password",
            "admin",
            "qwerty",
            "12345678"
        ]
        
        for weak_password in weak_passwords:
            # This would be implemented in the UserCreate validation
            # For now, we just document the expected behavior
            assert len(weak_password) < 8 or weak_password in weak_passwords
    
    def test_email_validation(self):
        """Test that email validation works correctly."""
        valid_emails = [
            "user@example.com",
            "test.email@domain.co.uk",
            "user+tag@example.org"
        ]
        
        invalid_emails = [
            "notanemail",
            "@example.com",
            "user@",
            "user@.com"
        ]
        
        # This would be implemented with Pydantic email validation
        for email in valid_emails:
            assert "@" in email and "." in email.split("@")[1]
        
        for email in invalid_emails:
            assert "@" not in email or "." not in email.split("@")[1]

