from typing import List
from typing import Tuple
from typing import Union
from uuid import UUID

from app.common.base_repository import BaseRepository
from app.role.models import Role


class RoleRepository(BaseRepository):
    """
    Roles repository.

    Args:
        BaseRepository: Base repository configuration.
    """
    model_class = Role

    @classmethod
    def update(cls, model_id: UUID, update_fields: Union[List, Tuple], **kwargs) -> model_class:
        """
        Update role model.

        Args:
            model_id {UUID}: Id of the role to update.

            update_fields {List | Tuple}: A tuple of list of fields to update

            **kwargs
        """
        return cls.update_by_id(model_id, update_fields, **kwargs)

    @classmethod
    def get_all(cls, **kwargs) -> List[model_class]:
        """
        Get all the roles.

        Args:
            **kwargs

        Returns:
            List of roles.
        """
        sort_key = kwargs['sort_key']
        sort_order = kwargs['sort_order']

        if sort_order == 'desc':
            query = cls.model_class.query.order_by(
                getattr(cls.model_class, sort_key).desc())
        else:
            query = cls.model_class.query.order_by(
                getattr(cls.model_class, sort_key).asc())

        return query.all()

    @classmethod
    def get_by_name(cls, normalized_name: str) -> model_class:
        """
        Get role by the normalized name.

        Args:
            normalized_name{str}: Name of the role.
        """
        return cls.model_class.query\
            .filter(cls.model_class.normalized_name == normalized_name)\
            .first()
