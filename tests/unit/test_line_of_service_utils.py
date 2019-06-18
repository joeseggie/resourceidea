"""Tests for app.line_of_service.utils module"""
from app.line_of_service.models import LineOfService
from app.line_of_service.utils import create_line_of_service
from app.line_of_service.utils import update_line_of_service


def test_create_line_of_service(session, fake_lorem):
    """Test create_line_of_service."""

    # Arrange
    fake_los = fake_lorem.word()

    # Act
    result = create_line_of_service(name=fake_los)

    # Assert
    if not isinstance(result, LineOfService):
        raise AssertionError()


def test_update_line_of_service(session, fake_lorem):
    """Test update_line_of_service"""

    # Arrange
    fake_los = create_line_of_service(name=fake_lorem.word())
    fake_los_name = fake_los.name

    # Act
    result = update_line_of_service(
        line_of_service_id=fake_los.id,
        name=fake_lorem.word())

    # Assert
    if not isinstance(result, LineOfService):
        raise AssertionError()
    if result.name == fake_los_name:
        raise AssertionError()
