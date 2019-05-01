from uuid import UUID

from app.company.repository import CompanyRepository
from app.company.models import Company


def test_create(session):
    new_company = Company(
        name='Company 1',
        name_stub='company-1',
        address='Company address')
    new_company = CompanyRepository.create(new_company)

    assert isinstance(new_company.id, UUID)


def test_get_by_id(session):
    company = CompanyRepository.get_one_by_id(UUID('91c4b0b8-cf94-4b0b-8986-58c94aa2c578'))
    assert isinstance(company, Company)


def test_get_all(session):
    assert isinstance(CompanyRepository.get_all(), list)


def test_update_by_id(session):
    # Act
    result = CompanyRepository.update(
        id=UUID('91c4b0b8-cf94-4b0b-8986-58c94aa2c578'),
        name='Company name 1',
        name_stub='company-name-1',
        address='Company address 1')
    # Assert
    assert isinstance(result, Company)
    assert result.name == 'Company name 1'
    assert result.name_stub == 'company-name-1'
    assert result.address == 'Company address 1'
    assert result.id == UUID('91c4b0b8-cf94-4b0b-8986-58c94aa2c578')


def test_delete_by_id(session):
    # Act
    result = CompanyRepository.delete_by_id(UUID('91c4b0b8-cf94-4b0b-8986-58c94aa2c578'))
    # Assert
    assert result == 1
