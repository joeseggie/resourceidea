from datetime import datetime
from unittest.mock import Mock

from app.queryables.assignment_queryable import AssignmentQueryable


class TestAssignmentQueryable:
    def test_returns_list(self):
        """Test list is returned.
        """
        queryable = AssignmentQueryable()
        result = queryable.to_list()
        assert isinstance(result, list)

    def test_starts_before_filter_returns_Query(self):
        '''Test Query object is returned.
        '''
        queryable = AssignmentQueryable()
        date_filter = datetime.now()
        result = queryable.starts_before(date_filter)
        assert isinstance(result, AssignmentQueryable)

    def test_starts_after_filter_returns_Query(self):
        '''Test returns Query object.
        '''
        queryable = AssignmentQueryable()
        date_filter = datetime.now()
        result = queryable.starts_after(date_filter)
        assert isinstance(result, AssignmentQueryable)

    def test_ends_before_filter_returns_Query(self):
        '''Test returns Query object after filtering by end date.
        '''

        queryable = AssignmentQueryable()
        date_filter = datetime.now()
        result = queryable.ends_before(date_filter)
        assert isinstance(result, AssignmentQueryable)

    def test_ends_after_filter_returns_Query(self):
        '''Test returns Query object after filtering.
        '''

        queryable = AssignmentQueryable()
        date_filter = datetime.now()
        result = queryable.ends_after(date_filter)
        assert isinstance(result, AssignmentQueryable)

    def test_where_resource_is_returns_Query(self):
        queryable = AssignmentQueryable()
        resource_id = Mock()
        result = queryable.where_resource_is(resource_id)
        assert isinstance(result, AssignmentQueryable)

    def test_where_assignment_status_is_returns_Query(self):
        '''Test returns Query object after filtering.
        '''

        queryable = AssignmentQueryable()
        assignment_status_id = Mock()
        result = queryable.where_assignment_status_is(assignment_status_id)
        assert isinstance(result, AssignmentQueryable)

    def test_where_job_task_is_returns_Query(self):
        '''Test returns Query object after filtering.
        '''

        queryable = AssignmentQueryable()
        job_task_id = Mock()
        result = queryable.where_job_task_is(job_task_id)
        assert isinstance(result, AssignmentQueryable)
