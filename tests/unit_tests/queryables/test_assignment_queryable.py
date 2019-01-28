from datetime import datetime
from unittest.mock import Mock

from sqlalchemy.orm.query import Query

from app.queryables.assignment_queryable import AssignmentQueryable


def test_returns_list():
    queryable = AssignmentQueryable()
    result = queryable.to_list()
    assert isinstance(result, list)


def test_starts_before_filter_returns_Query():
    queryable = AssignmentQueryable()
    date_filter = datetime.now()
    result = queryable.starts_before(date_filter)
    assert isinstance(result, Query)


def test_starts_after_filter_returns_Query():
    queryable = AssignmentQueryable()
    date_filter = datetime.now()
    result = queryable.starts_after(date_filter)
    assert isinstance(result, Query)


def test_ends_before_filter_returns_Query():
    queryable = AssignmentQueryable()
    date_filter = datetime.now()
    result = queryable.ends_before(date_filter)
    assert isinstance(result, Query)


def test_ends_after_filter_returns_Query():
    queryable = AssignmentQueryable()
    date_filter = datetime.now()
    result = queryable.ends_after(date_filter)
    assert isinstance(result, Query)


def test_where_resource_is_returns_Query():
    queryable = AssignmentQueryable()
    resource_id = Mock()
    result = queryable.where_resource_is(resource_id)
    assert isinstance(result, Query)


def test_where_assignment_status_is_returns_Query():
    queryable = AssignmentQueryable()
    assignment_status_id = Mock()
    result = queryable.where_assignment_status_is(assignment_status_id)
    assert isinstance(result, Query)


def test_where_job_task_is_returns_Query():
    queryable = AssignmentQueryable()
    job_task_id = Mock()
    result = queryable.where_job_task_is(job_task_id)
    assert isinstance(result, Query)
