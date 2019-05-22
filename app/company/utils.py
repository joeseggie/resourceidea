import re
from typing import List
from uuid import UUID

from app.company.models import Company
from app.company.repositories import CompanyRepository


def _get_name_slug(name: str) -> str:
    """Get the stub of the company's name.

    Arguments:
        name {str} -- Company name.

    Returns:
        str -- Company name stub.
    """
    return '-'.join(re.split(r'\W', name.lower()))


def get_companies(**kwargs) -> List[Company]:
    """Get a list of companies.

    Returns:
        List[Company] -- List of companies.
    """
    return CompanyRepository.get_all(**kwargs)


def get_company(model_id: UUID) -> Company:
    """Get a company given the Id.

    Arguments:
        model_id {UUID} -- Id of the company.

    Returns:
        Company -- Company.
    """
    return CompanyRepository.get_one_by_id(model_id)


def update_company(model_id: UUID, **kwargs) -> Company:
    """Update company data.

    Arguments:
        model_id {UUID} -- Company Id.

    Returns:
        Company -- Updated company.
    """
    return CompanyRepository.update(
        model_id=model_id,
        name_slug=_get_name_slug(kwargs['name']),
        **kwargs)


def create_company(**kwargs) -> Company:
    """Add new company.

    Returns:
        Company -- New company.
    """
    return CompanyRepository.create(Company(
        name=kwargs['name'],
        name_slug=_get_name_slug(kwargs['name']),
        address=kwargs['address']))


def delete_company(model_id: UUID) -> int:
    """Delete company.

    Arguments:
        model_id {UUID} -- Id of the company to be deleted.

    Returns:
        int -- Number of rows deleted.
    """
    return CompanyRepository.delete_by_id(model_id)
