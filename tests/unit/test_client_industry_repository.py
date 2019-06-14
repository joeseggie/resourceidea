"""
Testing client industry repository operations.
"""
from uuid import UUID

import pytest

from app.client_industry.models import ClientIndustry
from app.client_industry.repositories import ClientIndustryRepository


def test_create(session, fake_lorem):
    """Test creating a client industry."""
    # Arrange
    test_model = ClientIndustry(name=fake_lorem.word())

    # Act
    result = ClientIndustryRepository.add(model=test_model)

    # Assert
    assert isinstance(result, ClientIndustry)
    assert isinstance(UUID(result.id), UUID)


def test_update(session, fake_lorem):
    """Test updating a client industry"""
    # Arrange
    test_model = ClientIndustryRepository.add(
        ClientIndustry(name=fake_lorem.word()))
    updates = {
        'name': 'Changed name',
        'name_slug': 'changed-name'
    }
    update_fields = ('name', 'name_slug', )

    # Act
    result = ClientIndustryRepository\
        .update(test_model.id, update_fields, **updates)

    # Assert
    assert isinstance(result, ClientIndustry)
    assert test_model.id == result.id


def test_update_raises_value_error_exception(session, fake_lorem):
    """Test update raises ValueError exception when invalid
    data is supplied"""

    # Arrange
    test_model = ClientIndustryRepository.add(
        ClientIndustry(name=fake_lorem.word()))
    updates = {
        'name': 'Existing name',
        'name_slug': 'existing-name'
    }
    update_fields = ('name', 'name_slug', )

    # Assert
    with pytest.raises(ValueError):
        ClientIndustryRepository\
            .update(test_model.id, update_fields, **updates)
