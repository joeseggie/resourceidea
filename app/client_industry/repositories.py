"""Client Industry repository"""
import re

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
        """
        model.name_slug = cls._name_slug(model.name)
        return cls.create(model)
