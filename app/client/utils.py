"""app.client.utils module"""
from app.client.models import Client
from app.client.repositories import ClientRepository


def create_client(**kwargs) -> Client:
    """
    Create client

    Returns:
        New client.
    """
    new_client = Client(
        name=kwargs['name'],
        address=kwargs.get('address', None),
        organization_id=kwargs['organization_id'],
        client_industry_id=kwargs.get('client_industry_id', None))

    return ClientRepository.create_client(new_client)


def update_client(**kwargs) -> Client:
    """
    Update client

    Returns:
        Updated client.
    """
    return ClientRepository.update(
        client_id=kwargs['client_id'],
        name=kwargs['name'],
        address=kwargs.get('address', None),
        client_industry_id=kwargs.get('client_industry_id', None))


def get_client(client_id: str) -> Client:
    """
    Get client by ID.

    Args:
        client_id (str): Client ID.

    Returns:
        Client details.
    """
    return ClientRepository.get_one_by_id(model_id=client_id)


def list_clients() -> list:
    """
    List clients.

    Returns:
        List of clients.
    """
    return ClientRepository.get_all()
