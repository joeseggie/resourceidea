from abc import ABC
from typing import Tuple
from typing import List

from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy.orm import Query
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import NotFound

from database import db


class BaseRepository(ABC):
    model_class = None

    @classmethod
    def _raise_invalid_data_error(cls):
        """Raises invalid data ValueError"""
        raise ValueError('Invalid data supplied')

    @classmethod
    def _base_query(cls) -> Query:
        return cls.model_class.query

    @classmethod
    def update_by_id(cls,
                     model_id: UUID,
                     fields_for_update: Tuple,
                     **kwargs) -> model_class:
        """
        Update model by ID.

        Args:
            model_id (UUID): Model ID.

            fields_for_update (Tuple): Fields to be updated on the model.

        Returns:
            Updated model.

        Raises:
            ValueError: An error occurred while processing the data supplied
            for a new client industry.
        """
        try:
            if cls._model_exists(model_id):
                update_data = {}
                for field in fields_for_update:
                    if field in kwargs:
                        update_data[field] = kwargs[field]

                cls._base_query().filter_by(id=model_id).update(update_data)
                db.session.commit()
        except IntegrityError:
            cls._raise_invalid_data_error()
        else:
            return cls.get_one_by_id(model_id)

    @classmethod
    def get_one_by_id(cls, model_id: UUID) -> model_class:
        """
        Get model by ID.

        Args:
            model_id (UUID): Model ID.

        Returns:
            Model with the ID provided.
        """
        return cls.model_class.query.filter_by(id=model_id).first()

    @classmethod
    def create(cls, model: db.Model) -> model_class:
        """
        Create new client industry.

        Args:
            model: Client industry to be saved to the database.

        Returns:
            Newly created client industry.

        Raises:
            ValueError: An error occurred while processing the data supplied
            for a new client industry.
        """
        try:
            db.session.add(model)
            db.session.commit()
        except IntegrityError:
            cls._raise_invalid_data_error()
        else:
            return model

    @classmethod
    def delete_by_id(cls, model_id: UUID) -> int:
        """
        Delete model by id.

        Args:
            model_id (UUID): model ID.

        Returns:
            Number of rows deleted.
        """
        rows_deleted = cls._base_query().filter_by(id=model_id).delete()
        db.session.commit()
        return rows_deleted

    @classmethod
    def _model_exists(cls, model_id: UUID) -> bool:
        """
        Checks if the model exists.

        Args:
            model_id (str): model ID.

        Returns:
            True, if model exists. Otherwise, False.
        """
        model_query = cls.get_one_by_id(model_id)
        if model_query:
            return True
        else:
            raise NotFound('Model does not exist')

    @classmethod
    def get_all(cls) -> List[model_class]:
        """
        Get list

        Returns:
            List of model.
        """
        return cls.model_class.query.all()
