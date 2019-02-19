"""Test assignment status queryable.
"""
from app.queryables.assignment_status_queryable import AssistantStatusQueryable


class TestAssignmentStatusQueryable:
    def test_returns_list(self):
        '''Test returns list.
        '''

        queryable = AssistantStatusQueryable()
        result = queryable.to_list()
        assert isinstance(result, list)
