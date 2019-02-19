'''JobCommentQueryable unit tests.
'''
from unittest.mock import Mock

from app.queryables.job_comment_queryable import JobCommentQueryable


class TestJobCommentQueryable:
    def test_to_list(self):
        '''Test to_list method.
        '''
        queryable = JobCommentQueryable()
        result = queryable.to_list()
        assert isinstance(result, list)

    def test_where_job_is_returns_JobCommentQueryable(self):
        '''Test where_job_is method.
        '''
        queryable = JobCommentQueryable()
        job_id = Mock()
        result = queryable.where_job_is(job_id)
        assert isinstance(result, JobCommentQueryable)
