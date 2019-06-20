"""Tests for app.jobs.utils module"""
from app.engagement.utils import list_engagements
from app.job.models import Job
from app.job.utils import create_job


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
