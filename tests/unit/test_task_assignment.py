"""Test app.task_assignment.utils module."""
from datetime import datetime
from datetime import timedelta

import pytz

from app.resource.utils import list_resources
from app.task.utils import list_tasks
from app.task_assignment.models import TaskAssignment
from app.task_assignment.utils import create_task_assignment
from app.task_assignment.utils import get_task_assignment
from app.task_assignment.utils import update_task_assignment


def test_create_task_assignment(session):
    """Test create_task_assignment method."""
    # Arrange
    fake_task_id = next(iter(list_tasks() or []), None).id
    fake_resource_id = next(iter(list_resources() or []), None)
    utc_date = datetime.utcnow()
    utc_date = utc_date.replace(tzinfo=pytz.utc)
    fake_start_date_time = utc_date
    fake_start_date_time = fake_start_date_time.replace(tzinfo=pytz.utc)
    fake_end_datetime = utc_date + timedelta(days=5)
    fake_end_datetime = fake_end_datetime.replace(tzinfo=pytz.utc)
    new_task_assignment = dict(
        resource_id=fake_resource_id,
        task_id=fake_task_id,
        start_date_time=fake_start_date_time,
        end_date_time=fake_end_datetime)

    # Act
    result = create_task_assignment(**new_task_assignment)

    # Assert
    if not isinstance(result, TaskAssignment):
        raise AssertionError()


def test_create_task_assignment_none_resource(session):
    """Test create_task_assignment with no resource."""

    # Arrange
    fake_task_id = next(iter(list_tasks() or []), None).id
    utc_date = datetime.utcnow()
    fake_start_date_time = utc_date
    fake_end_datetime = utc_date + timedelta(days=5)
    new_task_assignment = dict(
        resource_id=None,
        task_id=fake_task_id,
        start_date_time=fake_start_date_time,
        end_date_time=fake_end_datetime)

    # Act
    result = create_task_assignment(**new_task_assignment)

    # Assert
    if not isinstance(result, TaskAssignment):
        raise AssertionError()


def test_create_task_assignment_no_resource(session):
    """Test create_task_assignment with no resource."""

    # Arrange
    fake_task_id = next(iter(list_tasks() or []), None).id
    utc_date = datetime.utcnow()
    fake_start_date_time = utc_date
    fake_end_datetime = utc_date + timedelta(days=5)
    new_task_assignment = dict(
        task_id=fake_task_id,
        start_date_time=fake_start_date_time,
        end_date_time=fake_end_datetime)

    # Act
    result = create_task_assignment(**new_task_assignment)

    # Assert
    if not isinstance(result, TaskAssignment):
        raise AssertionError()


def test_update_task_assignment(session):
    """Test update_task_assignment function"""

    # Arrange
    fake_task_id = next(iter(list_tasks() or []), None).id
    utc_date = datetime.utcnow()
    fake_start_date_time = utc_date
    fake_end_datetime = utc_date + timedelta(days=5)
    utc_date_update = datetime.utcnow()
    update_start_date_time = utc_date_update
    update_end_datetime = utc_date_update + timedelta(days=5)
    new_task_assignment = dict(
        task_id=fake_task_id,
        start_date_time=fake_start_date_time,
        end_date_time=fake_end_datetime)
    fake_assignment = create_task_assignment(**new_task_assignment)
    updates = {
        'start_date_time': update_start_date_time,
        'end_date_time': update_end_datetime
    }

    # Act
    result = update_task_assignment(fake_assignment.id, **updates)

    # Assert
    if not isinstance(result, TaskAssignment):
        raise AssertionError()
    if result.start_date_time == fake_start_date_time:
        raise AssertionError()
    if result.end_date_time == fake_end_datetime:
        raise AssertionError()


def test_get_task_assignment(session):
    """Test get_task_assignment function"""

    # Arrange
    fake_task_id = next(iter(list_tasks() or []), None).id
    utc_date = datetime.utcnow()
    fake_start_date_time = utc_date
    fake_start_date_time = fake_start_date_time.replace(tzinfo=pytz.utc)
    fake_end_datetime = utc_date + timedelta(days=5)
    fake_end_datetime = fake_end_datetime.replace(tzinfo=pytz.utc)
    new_task_assignment = dict(
        task_id=fake_task_id,
        start_date_time=fake_start_date_time,
        end_date_time=fake_end_datetime)
    fake_assignment = create_task_assignment(**new_task_assignment)

    # Act
    result = get_task_assignment(fake_assignment.id)

    # Assert
    if not isinstance(result, TaskAssignment):
        raise AssertionError()
    if result.start_date_time != fake_start_date_time:
        raise AssertionError()
    if result.end_date_time != fake_end_datetime:
        raise AssertionError()
    if result.task_id != fake_task_id:
        raise AssertionError()
