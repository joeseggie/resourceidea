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
