from typing import List
from uuid import UUID

from flask_restful import abort

from app.common.base_repository import BaseRepository
from app.company.models import Company


class CompanyRepository(BaseRepository):
    model_class = Company

    @classmethod
    def update(cls, model_id: UUID, **kwargs) -> model_class:
        company = cls.get_one_by_id(model_id)
        if not company:
            abort(404, message=f'Company was not found.')
        update_fields = ('name', 'name_slug', 'address')
        return cls.update_by_id(model_id, update_fields, **kwargs)

    @classmethod
    def get_all(cls, **kwargs) -> List[model_class]:
        print(kwargs)
        sort_key = kwargs.get('sort_key')
        sort_order = kwargs.get('sort_order')

        if sort_order == 'desc':
            query = Company.query.order_by(
                getattr(cls.model_class, sort_key).desc())
        else:
            query = Company.query.order_by(
                getattr(cls.model_class, sort_key).asc())

        return query.to_list()
