from abc import ABC
from typing import List
from typing import Tuple
from typing import Union

from uuid import UUID

from sqlalchemy.orm import Query

from database import db


class BaseRepository(ABC):
    model_class = None

    @classmethod
    def _base_query(cls) -> Query:
        return cls.model_class.query

    @classmethod
    def update_by_id(cls, id: UUID, fields_for_update: Union[Tuple, List], **kwargs) -> Query:
        update_data = {}
        for field in fields_for_update:
            if field in kwargs:
                update_data[field] = kwargs[field]

        cls._base_query().filter_by(id=id).update(update_data)
        db.session.commit()
        return cls.get_one_by_id(id)

    @classmethod
    def get_one_by_id(cls, id: UUID) -> model_class:
        return cls.model_class.query.get(id)

    @classmethod
    def create(cls, model: db.Model) -> model_class:
        db.session.add(model)
        db.session.commit()
        return model

    @classmethod
    def delete_by_id(cls, id: UUID) -> int:
        rows_deleted = cls._base_query().filter_by(id=id).delete()
        db.session.commit()
        return rows_deleted
