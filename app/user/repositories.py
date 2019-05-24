from flask import abort
from typing import List
from uuid import UUID

from app.common.base_repository import BaseRepository
from app.user.models import UserAccount


class UserRepository(BaseRepository):
    model_class = UserAccount

    @classmethod
    def get_all(cls, **kwargs) -> List[model_class]:
        sort_key = kwargs['sort_key']
        sort_order = kwargs['sort_order']

        if sort_order == 'desc':
            query = cls.model_class.query.order_by(
                getattr(cls.model_class, sort_key).desc())
        else:
            query = cls.model_class.query.order_by(
                getattr(cls.model_class, sort_key).asc())
        return query.to_list()

    @classmethod
    def update(cls, model_id: UUID, **kwargs):
        user_account = cls.get_one_by_id(model_id)
        if not user_account:
            abort(404, message='User account was not found')
        update_fields = ('username', 'email', 'phone_number')
        return cls.update_by_id(model_id, update_fields, **kwargs)
