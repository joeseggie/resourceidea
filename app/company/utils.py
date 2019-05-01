import re
from typing import List
from uuid import UUID

from app.company.models import Company
from app.company.repository import CompanyRepository


def _get_name_stub(name: str) -> str:
    """Get the stub of the company's name.

    Arguments:
        name {str} -- Company name.

    Returns:
        str -- Company name stub.
    """
    return '-'.join(re.split(r'\W', name))


def get_companies() -> List[Company]:
    """Get a list of companies.

    Returns:
        List[Company] -- List of companies.
    """
    return CompanyRepository.get_all()


def get_company(id: UUID) -> Company:
    """Get a company given the Id.

    Arguments:
        id {UUID} -- Id of the company.

    Returns:
        Company -- Company.
    """
    return CompanyRepository.get_one_by_id(id)


def update_company(id: UUID, **kwargs) -> Company:
    """Update company data.

    Arguments:
        id {UUID} -- Company Id.

    Returns:
        Company -- Updated company.
    """
    return CompanyRepository.update(id, name_stub=_get_name_stub(kwargs['name']), **kwargs)


def create_company(**kwargs) -> Company:
    """Add new company.

    Returns:
        Company -- New company.
    """
    return CompanyRepository.create(Company(
        name=kwargs['name'],
        name_stub=_get_name_stub(kwargs['name']),
        address=kwargs['address']))


def delete_company(id: UUID) -> int:
    """Delete company.

    Arguments:
        id {UUID} -- Id of the company to be deleted.

    Returns:
        int -- Number of rows deleted.
    """
    return CompanyRepository.delete_by_id(id)
