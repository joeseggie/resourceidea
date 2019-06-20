"""app.job.repositories module"""
from app.common.base_repository import BaseRepository
from app.job.models import Job


class JobRepository(BaseRepository):
    """Job repository"""
    model_class = Job
