"""app.job.utils module"""
from app.job.models import Job
from app.job.repositories import JobRepository


def create_job(**kwargs) -> Job:
    """
    Create new job.

    Returns:
        Job created.
    """
    new_job = Job(**kwargs)
    return JobRepository.create(new_job)
