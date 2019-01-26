"""Test assignment status queryable.
"""
from app.queryables.assignment_status_queryable import AssistantStatusQuerayble


def test_returns_list():
    queryable = AssistantStatusQuerayble()
    result = queryable.to_list()
    assert isinstance(result, list)
