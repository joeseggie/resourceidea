from typing import List

from sqlalchemy.dialects.postgresql import UUID

from app.common.base_repository import BaseRepository
from app.organization.models import Organization


class OrganizationRepository(BaseRepository):
    """
    Organization repository.

    Args:
        BaseRepository: Base repository.
    """
    model_class = Organization

    @classmethod
    def update(cls, model_id: UUID, **kwargs) -> model_class:
        """
        Update organization details.

        Args:
            model_id (UUID): Model ID.

        Returns:
            Organization updated.
        """
        update_fields = ('name', 'name_slug', 'address')
        return cls.update_by_id(model_id, update_fields, **kwargs)

    @classmethod
    def get_all(cls, **kwargs) -> List[model_class]:
        """
        List organizations.

        Returns:
            List of organizations.
        """
        sort_key = kwargs.get('sort_key')
        sort_order = kwargs.get('sort_order')

        if sort_order == 'desc':
            query = cls.model_class.query.order_by(
                getattr(cls.model_class, sort_key).desc())
        else:
            query = cls.model_class.query.order_by(
                getattr(cls.model_class, sort_key).asc())

        return query.to_list()

    @classmethod
    def get_one_by_name(cls, name_slug: str, **kwargs) -> model_class:
        """
        Get an organization by name.

        Args:
            name_slug (str): Name slug.

        Returns:
            Organization.
        """
        return cls.model_class.query\
            .filter(cls.model_class.name_slug == name_slug)\
            .first()
