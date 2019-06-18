"""
Employee repository.
"""
from typing import Union
from typing import List
from typing import Tuple

from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID

from app.common.base_repository import BaseRepository
from app.employee.models import Employee


class EmployeeRepository(BaseRepository):
    """
    Employee repository.
    """
    model_class = Employee

    @classmethod
    def update(cls,
               employee_id: UUID,
               update_fields: Union[List, Tuple],
               **kwargs) -> model_class:
        """
        Update employee record.

        Args:
            employee_id (UUID): Employee Id

            update_fields (List | Tuple): Fields to update

        Returns:
            Employee record.
        """
        return cls.update_by_id(employee_id, update_fields, **kwargs)

    @classmethod
    def get_one_by_file_number(cls, file_number: str) -> Employee:
        """
        Get employee by file number.

        Args:
            file_number (str): Employee file number.

        Returns:
            Employee: Employee with file number.
        """
        return cls.model_class.query\
            .filter(
                func.lower(
                    cls.model_class.file_number) == func.lower(file_number))\
            .first()
