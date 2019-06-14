"""Client Industry utils module"""
from app.client_industry.models import ClientIndustry
from app.client_industry.repositories import ClientIndustryRepository


def create_client_industry(name: str) -> ClientIndustry:
    """
    Creates client industry.

    Args:
        name (str): Name of client industry to be added.

    Returns:
        ClientIndustry: Client industry that has been added.

    Raises:
        ValueError if client industry name already exists.
    """
    new_client_industry = ClientIndustry(name=name)
    return ClientIndustryRepository.add(new_client_industry)


def update_client_industry(
        client_industry_id: str,
        **updates):
    """
    Update client industry.

    Args:
        client_industry_id (str): Client industry ID.

    Returns:
        Updated client industry.

    Raises:
        ValueError if client industry update name already exists.
    """
    update_fields = ('name', 'name_slug', )
    return ClientIndustryRepository.update(
        client_industry_id=client_industry_id,
        update_fields=update_fields,
        **updates)
