"""Test client industry utils"""
from uuid import uuid4

import pytest
from werkzeug.exceptions import NotFound

from app.client_industry.models import ClientIndustry
from app.client_industry.utils import create_client_industry
from app.client_industry.utils import update_client_industry


def test_update(session, fake_lorem):
    """Test updating a client industry"""
    # Arrange
    test_model = create_client_industry(name=fake_lorem.word())
    updates = {
        'name': 'Changed name',
    }

    # Act
    result = update_client_industry(test_model.id, **updates)

    # Assert
    assert isinstance(result, ClientIndustry)
    assert test_model.id == result.id


def test_update_raises_not_found_exception(session, fake_lorem):
    """Test update raises NotFound exception when the resource is
     not found"""

    # Arrange
    fake_id = str(uuid4())
    fake_updates = {
        'name': fake_lorem.word(),
    }

    # Assert
    with pytest.raises(NotFound):
        update_client_industry(fake_id, **fake_updates)


def test_update_raises_value_error_exception(session, fake_lorem):
    """Test update raises ValueError exception when invalid
    data is supplied"""

    # Arrange
    test_model = create_client_industry(name=fake_lorem.word())
    updates = {
        'name': 'Existing name',
    }

    # Assert
    with pytest.raises(ValueError):
        update_client_industry(test_model.id, **updates)
