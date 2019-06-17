"""Test app.client.repositories.ClientRepository module"""
from app.client_industry.utils import create_client_industry
from app.client.models import Client
from app.client.repositories import ClientRepository
from app.organization.utils import create_organization


def test_create_client(session, fake_lorem):
    """Test create_client function"""

    # Arrange
    fake_industry = create_client_industry(name=fake_lorem.word())
    fake_org = create_organization(
        address=fake_lorem.word(),
        organization_name=fake_lorem.word())
    fake_client = Client(
        name=fake_lorem.word(),
        organization_id=fake_org.id,
        client_industry_id=fake_industry.id)

    # Act
    result = ClientRepository.create_client(fake_client)

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
    fake_client = ClientRepository.create_client(Client(
        name=fake_lorem.word(),
        organization_id=fake_org.id,
        client_industry_id=first_fake_industry.id))
    fake_client_name = fake_client.name
    fake_client_slug = fake_client.name_slug

    # Act
    result = ClientRepository.update(
        client_id=fake_client.id,
        name=fake_lorem.word(),
        client_industry_id=sec_fake_industry.id)

    # Assert
    assert isinstance(result, Client)
    assert result.name != fake_client_name
    assert result.name_slug != fake_client_slug
    assert result.client_industry_id != first_fake_industry.id
    assert result.id == fake_client.id
