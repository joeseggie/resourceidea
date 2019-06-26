"""app.task.utils module"""
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
