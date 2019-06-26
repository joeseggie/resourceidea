"""Test app.tasks.utils module"""
from app.job.utils import list_jobs
from app.task.models import Task
from app.task.utils import create_task


def test_create_task(session, fake_lorem):
    """Test create_task function"""

    # Arrange
    fake_job_id = next(iter(list_jobs() or []), None).id
    fake_task = {
        'title': fake_lorem.sentence(),
        'description': fake_lorem.paragraph(),
        'job_id': fake_job_id
    }

    # Act
    result = create_task(**fake_task)

    # Assert
    if not isinstance(result, Task):
        raise AssertionError()
