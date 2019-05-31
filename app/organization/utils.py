import re
from typing import List
from uuid import UUID

from app.common.enums import OrganizationStatus
from app.organization.models import Organization
from app.organization.repositories import OrganizationRepository


def get_name_slug(name: str) -> str:
    """Get the stub of the organization's name.

    Arguments:
        name {str} -- Organization name.

    Returns:
        str -- Organization name stub.
    """
    return '-'.join(re.split(r'\W', name.lower()))


def get_organizations(**kwargs) -> List[Organization]:
    """Get a list of organizations.

    Returns:
        List[Organization] -- List of organizations.
    """
    return OrganizationRepository.get_all(**kwargs)


def get_organization(model_id: UUID) -> Organization:
    """Get a organization given the Id.

    Arguments:
        model_id {UUID} -- Id of the organization.

    Returns:
        Organization -- Organization.
    """
    return OrganizationRepository.get_one_by_id(model_id)


def get_organization_by_name(name: str, **kwargs) -> Organization:
    """
    Get organization by name.

    Args:
        organization_name {str}: Organization name

    Returns:
        Organization: Organization.
    """
    kwargs['name_slug'] = get_name_slug(name)
    return OrganizationRepository.get_all_by_name(**kwargs)


def update_organization(model_id: UUID, **kwargs) -> Organization:
    """Update organization data.

    Arguments:
        model_id {UUID} -- Organization Id.

    Returns:
        Organization -- Updated organization.
    """
    return OrganizationRepository.update(
        model_id=model_id,
        name_slug=get_name_slug(kwargs['name']),
        **kwargs)


def create_organization(organization_name: str, address: str) -> Organization:
    """Add new organization.

    Returns:
        Organization -- New organization.
    """
    return OrganizationRepository.create(Organization(
        name=organization_name,
        name_slug=get_name_slug(organization_name),
        address=address,
        status=OrganizationStatus.ACTIVE))


def delete_organization(model_id: UUID) -> int:
    """Delete organization.

    Arguments:
        model_id {UUID} -- Id of the organization to be deleted.

    Returns:
        int -- Number of rows deleted.
    """
    return OrganizationRepository.delete_by_id(model_id)
