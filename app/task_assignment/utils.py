"""app.task_assignment.utils module"""
from app.task_assignment.models import TaskAssignment
from app.task_assignment.repository import TaskAssignmentRepository


def create_task_assignment(**kwargs) -> TaskAssignment:
    """
    Create a new task assignment.

    Returns:
        Task assignment that has been created.
    """
    new_task_assignment = TaskAssignment(
        start_date_time = kwargs['start_date_time'],
        end_date_time = kwargs['end_date_time'],
        task_id = kwargs['task_id'],
        resource_id = kwargs.get('resource_id', None))
    return TaskAssignmentRepository.create(new_task_assignment)
