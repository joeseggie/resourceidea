"""Test app.client.utils module"""
from uuid import uuid4

from app.client.models import Client
from app.client.utils import create_client
from app.client.utils import get_client
from app.client.utils import update_client
from app.client_industry.utils import create_client_industry
from app.organization.utils import create_organization


def test_create_client(session, fake_lorem):
    """Test create_client function."""

    # Arrange
    fake_industry = create_client_industry(name=fake_lorem.word())
    fake_org = create_organization(
        address=fake_lorem.word(),
        organization_name=fake_lorem.word())

    # Act
    result = create_client(
        name=fake_lorem.word(),
        organization_id=fake_org.id,
        client_industry_id=fake_industry.id,
        name_stub=fake_lorem.word())

    # Assert
    assert isinstance(result, Client)


def test_update_client(session, fake_lorem):
    """Test update_client function."""

    # Arrange
    first_fake_industry = create_client_industry(name=fake_lorem.word())
    sec_fake_industry = create_client_industry(name=fake_lorem.word())
    fake_org = create_organization(
        address=fake_lorem.word(),
        organization_name=fake_lorem.word())
    fake_client = create_client(
        name=fake_lorem.word(),
        organization_id=fake_org.id,
        client_industry_id=first_fake_industry.id)
    fake_client_name = fake_client.name
    fake_client_slug = fake_client.name_slug

    # Act
    result = update_client(
        client_id=fake_client.id,
        name=fake_lorem.word(),
        client_industry_id=sec_fake_industry.id)

    # Assert
    assert isinstance(result, Client)
    assert result.name != fake_client_name
    assert result.name_slug != fake_client_slug
    assert result.client_industry_id != first_fake_industry.id
    assert result.id == fake_client.id


def test_get_client(session, fake_lorem):
    """Test get_client function."""

    # Arrange
    fake_industry = create_client_industry(name=fake_lorem.word())
    fake_org = create_organization(
        address=fake_lorem.word(),
        organization_name=fake_lorem.word())
    test_client = create_client(
        name=fake_lorem.word(),
        organization_id=fake_org.id,
        client_industry_id=fake_industry.id)

    # Act
    result = get_client(test_client.id)

    # Assert
    assert result is not None
    assert isinstance(result, Client)
    assert result.id == test_client.id


def test_get_client_returns_none(session):
    """Test get_client returns None if not found."""

    # Arrange
    fake_client_id = str(uuid4())

    # Act
    result = get_client(client_id=fake_client_id)

    # Assert
    assert result is None
