"""app.task_assignment.utils module"""
from uuid import UUID

from app.task_assignment.models import TaskAssignment
from app.task_assignment.repository import TaskAssignmentRepository


def create_task_assignment(**kwargs) -> TaskAssignment:
    """
    Create a new task assignment.

    Returns:
        Task assignment that has been created.
    """
    new_task_assignment = TaskAssignment(
        start_date_time=kwargs['start_date_time'],
        end_date_time=kwargs['end_date_time'],
        task_id=kwargs['task_id'],
        resource_id=kwargs.get('resource_id', None))
    return TaskAssignmentRepository.create(new_task_assignment)


def update_task_assignment(assignment_id: UUID, **kwargs) -> TaskAssignment:
    """
    Update task assignment.

    Args:
        assignment_id (UUID): Task assignment ID.

    Returns:
         Updated task assignment.
    """
    assignment_for_update = TaskAssignmentRepository\
        .get_one_by_id(assignment_id)
    update_fields = ('resource_id', 'start_date_time', 'end_date_time',)
    if not assignment_for_update:
        raise ValueError('Assignment with ID specified does not found')
    return TaskAssignmentRepository.update_by_id(
        model_id=assignment_id,
        fields_for_update=update_fields,
        **kwargs)
