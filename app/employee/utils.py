"""
Employee utils
"""
import random
from string import digits

from app.employee.repository import EmployeeRepository


def generate_file_number() -> str:
    """
    Generate employee file number.

    Returns:
        str - Employee file number.
    """
    return f'EF{"".join(random.choice(digits) for i in range(6))}'


def file_number_exists(file_number: str) -> bool:
    """
    Checks if the file number is already used.

    Args:
        file_number {str}: File number.

    Returns:
        bool - True if the already in use. Otherwise, False.
    """
    employee = EmployeeRepository\
        .get_one_by_file_number(file_number)

    return True if employee else False
