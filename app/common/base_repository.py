from abc import ABC
from typing import List
from typing import Tuple
from typing import Union

from uuid import UUID

from sqlalchemy.orm import Query
from werkzeug.exceptions import NotFound

from database import db


class BaseRepository(ABC):
    model_class = None

    @classmethod
    def _base_query(cls) -> Query:
        return cls.model_class.query

    @classmethod
    def update_by_id(cls, model_id: UUID,
                     fields_for_update: Union[Tuple, List],
                     **kwargs) -> model_class:
        if cls._model_exists(model_id):
            update_data = {}
            for field in fields_for_update:
                if field in kwargs:
                    update_data[field] = kwargs[field]

            cls._base_query().filter_by(id=model_id).update(update_data)
            db.session.commit()
            return cls.get_one_by_id(model_id)

    @classmethod
    def get_one_by_id(cls, model_id: UUID) -> model_class:
        return cls.model_class.query.get(model_id)

    @classmethod
    def create(cls, model: db.Model) -> model_class:
        db.session.add(model)
        db.session.commit()
        return model

    @classmethod
    def delete_by_id(cls, model_id: UUID) -> int:
        rows_deleted = cls._base_query().filter_by(id=model_id).delete()
        db.session.commit()
        return rows_deleted

    @classmethod
    def _model_exists(cls, model_id: UUID) -> bool:
        model_query = cls.get_one_by_id(model_id)
        if model_query:
            return True
        else:
            raise NotFound('Model does not exist')
