"""Tests for app.line_of_service.utils module"""
from app.line_of_service.models import LineOfService
from app.line_of_service.utils import create_line_of_service


def test_create_line_of_service(session, fake_lorem):
    """Test create_line_of_service."""

    # Arrange
    fake_los = fake_lorem.word()

    # Act
    result = create_line_of_service(name=fake_los)

    # Assert
    if not isinstance(result, LineOfService):
        raise AssertionError()
