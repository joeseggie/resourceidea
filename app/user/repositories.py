from typing import List
from uuid import UUID

from sqlalchemy.orm import Query

from app.common.base_repository import BaseRepository
from app.user.models import UserAccount


class UserRepository(BaseRepository):
    model_class = UserAccount

    @classmethod
    def _sorted_user_accounts_query(cls, query: Query, **kwargs) -> Query:
        """
        Returns a sorted query of user accounts.

        Returns:
            Query: Sorted user accounts query.
        """
        sort_key = kwargs['sort_key']
        sort_order = kwargs['sort_order']

        if sort_order == 'desc':
            query = query.order_by(
                getattr(cls.model_class, sort_key).desc())
        else:
            query = query.order_by(
                getattr(cls.model_class, sort_key).asc())
        return query

    @classmethod
    def get_all(cls, **kwargs) -> List[model_class]:
        """
        Get all the user accounts.

        Returns:
            List[UserAccount]: List of user accounts.
        """
        organization_id = kwargs['organization_id']
        query = cls.model_class.query\
            .filter(cls.model_class.organization_id == organization_id)
        query = cls._sorted_user_accounts_query(query, **kwargs)
        return query.to_list()

    @classmethod
    def update(cls, model_id: UUID, **kwargs) -> model_class:
        """
        Update user account.

        Args:
            model_id (UUID): User account id.

        Returns:
            UserAccount: User account.
        """
        update_fields = ('username', 'email', 'phone_number')
        return cls.update_by_id(model_id, update_fields, **kwargs)

    @classmethod
    def confirm_phone_number(cls, model_id: UUID, **kwargs) -> model_class:
        """
        Confirm phone number of a user account.

        Args:
            model_id (UUID): id of the user account whose phone number
            is to be confirmed.

        Returns:
            UserAccount: User account.
        """
        update_fields = ('phone_number_confirmed',)
        return cls.update_by_id(model_id, update_fields, **kwargs)

    @classmethod
    def confirm_email(cls, model_id: UUID, **kwargs) -> model_class:
        """
        Confirm email of a user account.

        Args:
            model_id (UUID): Id of user account whose email is to be
            confirmed.

        Returns:
            UserAccount: User account.
        """
        update_fields = ('email_confirmed',)
        return cls.update_by_id(model_id, update_fields, **kwargs)

    @classmethod
    def get_one_by_field(cls, **kwargs) -> model_class:
        """
        Get all user accounts filtered by fields.

        Returns:
            UserAccount: User account.
        """
        query = cls.model_class.query
        for field in list(kwargs.keys()):
            query = query.filter(
                getattr(cls.model_class, field) == kwargs[field])
        return query.first()
