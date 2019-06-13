"""
Testing client industry operations.
"""
from uuid import UUID

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
