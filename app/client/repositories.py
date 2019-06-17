"""app.client.repositories module"""
from app.common.base_repository import BaseRepository
from app.common.utils import name_slug
from app.client.models import Client


class ClientRepository(BaseRepository):
    """
    Client repository.
    """
    model_class = Client

    @classmethod
    def create_client(cls, new_client: Client) -> Client:
        """
        Create a new client.

        Args:
            new_client (Client): New client to be created.

        Returns:
            New client created.
        """
        new_client.name_slug = name_slug(new_client.name)
        return cls.create(new_client)

    @classmethod
    def update(cls, client_id: str, **kwargs) -> Client:
        """
        Update client information.

        Returns:
            Updated client information.
        """
        update_fields = ('name', 'name_slug', 'address', 'client_industry_id')
        kwargs['name_slug'] = name_slug(kwargs['name'])

        return cls.update_by_id(
            model_id=client_id,
            fields_for_update=update_fields,
            **kwargs)
