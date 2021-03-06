"""app.task.utils module"""
from typing import List
from uuid import UUID

from app.task.models import Task
from app.task.repository import TaskRepository


def create_task(**kwargs) -> Task:
    """
    Create a new task.

    Returns:
        Created task.
    """
    new_task = Task(
        title=kwargs['title'],
        description=kwargs.get('description', None),
        job_id=kwargs['job_id'])
    return TaskRepository.create(new_task)


def update_task(task_id: UUID, **kwargs) -> Task:
    """
    Update job task.

    Args:
        task_id (UUID): Task ID.

    Returns:
        Task updated.
    """
    update_fields = ('title', 'description', 'job_id',)
    return TaskRepository.update_by_id(
        model_id=task_id,
        fields_for_update=update_fields,
        **kwargs)


def get_task(task_id: UUID) -> Task:
    """
    Get task.

    Args:
        task_id (UUID): Task ID.

    Returns:
        Task
    """
    return TaskRepository.get_one_by_id(model_id=task_id)


def list_tasks() -> List[Task]:
    """
    List tasks.

    Returns:
        List of tasks.
    """
    return TaskRepository.get_all()
