import pytest

from app.auth.utils import signup


def test_raises_value_error_when_organization_exists(session):
    # Arrange
    input = {
        'name': 'Organization 1'
    }

    # Assert
    with pytest.raises(ValueError):
        signup(**input)


def test_raises_value_error_when_email_exists(session):
    # Arrange
    input = {
        'name': 'Organization 10',
        'email': 'mail@example.com'
    }

    # Assert
    with pytest.raises(ValueError):
        signup(**input)
