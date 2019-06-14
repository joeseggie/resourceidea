"""
Testing client industry repository operations.
"""
from uuid import UUID

import pytest

from app.client_industry.models import ClientIndustry
from app.client_industry.repositories import ClientIndustryRepository
from app.organization.utils import create_organization


def test_create(session, fake_lorem, fake_profile):
    """Test creating a client industry."""

    # Arrange
    fake_org = create_organization(
        organization_name=fake_lorem.word(),
        address=fake_profile.profile()['address'])
    test_model = ClientIndustry(
        name=fake_lorem.word(),
        organization_id=fake_org.id)

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


def test_get_one_by_id(session, fake_lorem):
    """Test get_one_by_id"""

    # Arrange
    fake_model = ClientIndustryRepository.add(
        ClientIndustry(name=fake_lorem.word()))

    # Act
    result = ClientIndustryRepository.get_one_by_id(model_id=fake_model.id)

    # Assert
    assert result is not None
    assert isinstance(result, ClientIndustry)
    assert result == fake_model


def test_list_client_industries(session, fake_lorem):
    """Test list_client_industries"""

    # Arrange
    fake_model = ClientIndustry(
        name=fake_lorem.word(),
        name_slug=fake_lorem.word())
    ClientIndustryRepository.create(fake_model)

    # Act
    result = ClientIndustryRepository.list_client_industries()

    # Assert
    assert isinstance(result, list)
