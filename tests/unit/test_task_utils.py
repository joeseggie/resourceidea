"""Test app.tasks.utils module"""
from app.job.utils import list_jobs
from app.task.models import Task
from app.task.utils import create_task
from app.task.utils import update_task


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


def test_update_task(session, fake_lorem):
    """Test update_task function"""

    # Arrange
    fake_job_id = next(iter(list_jobs() or []), None).id
    fake_task_data = {
        'title': fake_lorem.sentence(),
        'description': fake_lorem.paragraph(),
        'job_id': fake_job_id
    }
    fake_task = create_task(**fake_task_data)
    fake_task_title = fake_task.title
    task_updates = {'title': 'Changed task'}

    # Act
    result = update_task(fake_task.id, **task_updates)

    # Assert
    if fake_task_title == result.title:
        raise AssertionError()
