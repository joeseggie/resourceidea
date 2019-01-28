"""Test assignment status queryable.
"""
from app.queryables.assignment_status_queryable import AssistantStatusQueryable


def test_returns_list():
    queryable = AssistantStatusQueryable()
    result = queryable.to_list()
    assert isinstance(result, list)
