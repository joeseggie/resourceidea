"""Client Industry repository"""
import re
from typing import Tuple

from app.client_industry.models import ClientIndustry
from app.common.base_repository import BaseRepository


class ClientIndustryRepository(BaseRepository):
    """Client Industry repository"""
    model_class = ClientIndustry

    @classmethod
    def _name_slug(cls, name: str) -> str:
        """
        Get the slug of a client industry's name.

        Args:
            name (str): Client industry's name.

        Returns:
            str: Name slug formatted to remove all
            non-alphanumeric characters.
        """
        return '-'.join(re.split(r'\W', name.lower()))

    @classmethod
    def add(cls, model: model_class) -> model_class:
        """
        Create new client industry.

        Args:
            model (ClientIndustry): New client industry to add.

        Returns:
            ClientIndustry: Client industry that has been added.

        Raises:
            ValueError if client industry name already exists.
        """
        model.name_slug = cls._name_slug(model.name)
        return cls.create(model)

    @classmethod
    def update(cls,
               client_industry_id: str,
               update_fields: Tuple,
               **updates) -> model_class:
        """
        Update client industry.

        Args:
            client_industry_id (str): Client industry ID.

            update_fields (List, Tuple): Fields to be updated.

            updates: Data to update.

        Returns:
            Updated client industry.

        Raises:
            ValueError if client industry update name already exists.
        """
        if 'name' in updates:
            updates['name_slug'] = cls._name_slug(updates['name'])
            if 'name_slug' not in update_fields:
                update_fields = update_fields + ('name_slug', )

        return cls.update_by_id(
            model_id=client_industry_id,
            fields_for_update=update_fields,
            **updates)
