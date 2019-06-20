"""app.job.utils module"""
from uuid import UUID

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


def update_job(job_id: UUID, **kwargs) -> Job:
    """
    Update job.

    Args:
        job_id (UUID): ID of job to be update.

    Returns:
        Updated job.

    Raises:
        ValueError if the job with the ID does not exist.
    """
    job_for_update = JobRepository.get_one_by_id(job_id)
    if not job_for_update:
        raise ValueError('Job with ID specified does not exists')

    update_fields = ('title', 'description', 'start_date', 'completion_date',
                     'status')
    return JobRepository.update_by_id(
        model_id=job_for_update.id,
        fields_for_update=update_fields,
        **kwargs)


def get_job(job_id: UUID) -> Job:
    """
    Get job by ID.

    Args:
        job_id (UUID): ID of the job to be returned.

    Returns:
        Job
    """
    return JobRepository.get_one_by_id(model_id=job_id)
