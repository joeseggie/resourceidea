from typing import List
from uuid import UUID

from app.common.base_repository import BaseRepository
from app.company.models import Company

from werkzeug.exceptions import NotFound


class CompanyRepository(BaseRepository):
    model_class = Company

    @classmethod
    def update(cls, id: UUID, **kwargs):
        company = cls.get_one_by_id(id)
        if not company:
            raise NotFound('Company does not exist')
        update_fields = ('name', 'name_stub', 'address')
        return cls.update_by_id(id, update_fields, **kwargs)

    @classmethod
    def get_all(cls) -> List[model_class]:
        return Company.query.to_list()
