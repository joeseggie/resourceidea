"""Tests for app.jobs.utils module"""
from datetime import date

from app.engagement.utils import list_engagements
from app.job.models import Job
from app.job.utils import create_job
from app.job.utils import update_job


def test_create_job(session, fake_lorem):
    """Test create_job function"""

    # Arrange
    fake_engagement_id = next(iter(list_engagements() or []), None).id
    fake_job = {
        'title': fake_lorem.sentence(),
        'description': fake_lorem.paragraph(),
        'engagement_id': fake_engagement_id
    }

    # Act
    result = create_job(**fake_job)

    # Assert
    if not isinstance(result, Job):
        raise AssertionError()


def test_update_job(session, fake_lorem):
    """Test update_job function"""

    # Arrange
    fake_engagement_id = next(iter(list_engagements() or []), None).id
    fake_job = {
        'title': fake_lorem.sentence(),
        'description': fake_lorem.paragraph(),
        'engagement_id': fake_engagement_id
    }
    fake_job = create_job(**fake_job)
    old_id = fake_job.id
    old_title = fake_job.title
    updates = {
        'title': 'Changed title',
        'description': 'Changed description',
        'start_date': date.today(),
        'completion_date': date.today()
    }

    # Act
    result = update_job(fake_job.id, **updates)

    # Assert
    if not isinstance(result, Job):
        raise AssertionError()
    if old_id != result.id:
        raise AssertionError()
    if old_title == result.title:
        raise AssertionError()
