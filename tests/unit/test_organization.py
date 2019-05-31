from uuid import UUID
from faker import Faker
from faker.providers import address
from faker.providers import company

import pytest
from werkzeug.exceptions import NotFound

from app.organization.repositories import OrganizationRepository
from app.organization.models import Organization
from app.organization.utils import create_organization
from app.organization.utils import delete_organization
from app.organization.utils import get_organizations
from app.organization.utils import get_organization
from app.organization.utils import update_organization
from app.organization.utils import get_name_slug


def test_create(session):
    # Arrange
    fake = Faker()
    fake.add_provider(company)
    fake.add_provider(address)
    organization_name = fake.company()
    organization_name_slug = get_name_slug(organization_name)
    new_organization = Organization(
        name=organization_name,
        name_slug=organization_name_slug,
        address=fake.street_name())

    # Act
    new_organization = OrganizationRepository.create(new_organization)

    # Assert
    assert isinstance(new_organization.id, str)


def test_get_by_id(session):
    test_organization = OrganizationRepository.get_all(
        sort_key='name',
        sort_order='asc'
    )[0]
    result = OrganizationRepository.get_one_by_id(test_organization.id)
    assert isinstance(result, Organization)
    assert result.id == test_organization.id
    assert result.name == test_organization.name
    assert result.name_slug == test_organization.name_slug
    assert result.address == test_organization.address
    assert result.status == test_organization.status


def test_get_all(session):
    assert isinstance(OrganizationRepository.get_all(
            sort_key='name',
            sort_order='asc'),
            list)


def test_update_by_id(session):
    # Arrange
    test_organization = OrganizationRepository.get_all(
        sort_key='name',
        sort_order='asc'
    )[0]
    # Act
    result = OrganizationRepository.update(
        model_id=test_organization.id,
        name='Organization name 1',
        name_slug='organization-name-1',
        address='Organization address 1')
    # Assert
    assert isinstance(result, Organization)
    assert result.name == 'Organization name 1'
    assert result.name_slug == 'organization-name-1'
    assert result.address == 'Organization address 1'
    assert result.id == test_organization.id


def test_delete_by_id(session):
    # Arrange
    test_organization = OrganizationRepository.get_all(
        sort_key='name',
        sort_order='asc'
    )[0]

    # Act
    result = OrganizationRepository.delete_by_id(
            test_organization.id)
    # Assert
    assert result == 1


def test_update_when_not_found_raises_not_found_exception(session):
    # Assert
    with pytest.raises(NotFound):
        OrganizationRepository.update(
            model_id='71c4b0b8-cf93-4b0b-8986-58c94aa2c578',
            name='Organization name 1',
            name_slug='organization-name-1',
            address='Organization address 1')


def test_delete_when_not_found_returns_zero(session):
    # Act
    result = OrganizationRepository.delete_by_id('91c4b0b8-cf93-4b0b-8986-58c94aa2c578')
    # Assert
    assert result == 0


def test_model_repr(session):
    new_organization = Organization(
        name='Organization 1',
        name_slug='organization-1',
        address='Organization address')
    # Assert
    repr(new_organization) == '<Organization Organization 1>'


def test_utils_get_organizations(session):
    assert isinstance(
            get_organizations(sort_key='name', sort_order='asc'), list)


def test_utils_get_organization(session):
    # Arrange
    test_organization = OrganizationRepository.get_all(
        sort_key='name',
        sort_order='asc'
    )[0]
    assert isinstance(
            get_organization(test_organization.id),
            Organization)


def test_utils_update_organization(session):
    test_organization = OrganizationRepository.get_all(
        sort_key='name',
        sort_order='asc'
    )[0]
    assert isinstance(update_organization(
        model_id=test_organization.id,
        name='Organization name',
        address='Organization address'), Organization)


def test_utils_create_organization(session):
    assert isinstance(create_organization(
        organization_name='Organization name',
        address='Organization address'), Organization)


def test_utils_delete_organization(session):
    assert isinstance(
            delete_organization('91c4b0b8-cf94-4b0b-8986-58c94aa2c578'),
            int)
