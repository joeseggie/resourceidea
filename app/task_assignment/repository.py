"""app.task_assignment.repository module"""
from app.common.base_repository import BaseRepository
from app.task_assignment.models import TaskAssignment


class TaskAssignmentRepository(BaseRepository):
    """Task assignment repository."""

    model_class = TaskAssignment
