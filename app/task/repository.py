"""app.task.repository module"""
from app.common.base_repository import BaseRepository
from app.task.models import Task


class TaskRepository(BaseRepository):
    """Tasks repository"""
    model_class = Task
