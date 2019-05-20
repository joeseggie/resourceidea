from uuid import UUID

import pytest
from werkzeug.exceptions import NotFound

from app.company.repository import CompanyRepository
from app.company.models import Company
from app.company.utils import create_company
from app.company.utils import delete_company
from app.company.utils import get_companies
from app.company.utils import get_company
from app.company.utils import update_company


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


def test_update_when_not_found_raises_not_found_exception(session):
    # Assert
    with pytest.raises(NotFound):
        CompanyRepository.update(
            id=UUID('91c4b0b8-cf93-4b0b-8986-58c94aa2c578'),
            name='Company name 1',
            name_stub='company-name-1',
            address='Company address 1')


def test_delete_when_not_found_returns_zero(session):
    # Act
    result = CompanyRepository.delete_by_id(UUID('91c4b0b8-cf93-4b0b-8986-58c94aa2c578'))
    # Assert
    assert result == 0


def test_model_repr(session):
    new_company = Company(
        name='Company 1',
        name_stub='company-1',
        address='Company address')
    # Assert
    repr(new_company) == '<Company Company 1>'


def test_utils_get_companies(session):
    assert isinstance(get_companies(), list)


def test_utils_get_company(session):
    assert isinstance(
            get_company(UUID('91c4b0b8-cf94-4b0b-8986-58c94aa2c578')),
            Company)


def test_utils_update_company(session):
    assert isinstance(update_company(
        model_id=UUID('91c4b0b8-cf94-4b0b-8986-58c94aa2c578'),
        name='Company name',
        address='Company address'), Company)


def test_utils_create_company(session):
    assert isinstance(create_company(
        name='Company name',
        address='Company address'), Company)


def test_utils_delete_company(session):
    assert isinstance(
            delete_company(UUID('91c4b0b8-cf94-4b0b-8986-58c94aa2c578')),
            int)
