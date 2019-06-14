"""Test app.client.utils module"""
from app.client.models import Client
from app.client.utils import create_client
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
