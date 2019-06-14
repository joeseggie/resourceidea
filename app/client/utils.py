"""app.client.utils module"""
from app.client.models import Client
from app.client.repositories import ClientRepository


def create_client(**kwargs):
    """
    Create client

    Returns:
        New client.
    """
    new_client = Client(
        name=kwargs['name'],
        address=kwargs.get('address', None),
        organization_id=kwargs['organization_id'],
        client_industry_id=kwargs['client_industry_id'])

    return ClientRepository.create_client(new_client)
