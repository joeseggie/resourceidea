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
