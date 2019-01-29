'''JobCommentQueryable module.
'''
from app.models.job_comment import JobComment


class JobCommentQueryable:
    '''Job comment queryable.
    '''
    def __init__(self):
        '''Constructor.
        '''
        self.job_comment_queryable = JobComment.query

    def to_list(self):
        '''List job comments.
        '''
        query_result = self.job_comment_queryable.all()
        job_comments_list = [{
            'Id': result.id,
            'Details': result.details,
            'Made': result.made,
            'JobId': result.job_id,
            'ResourceId': result.resource_id
        } for result in query_result]
        return job_comments_list

    def where_job_is(self, job_id: int):
        '''Filter job comments by Job Id.

        Parameters
        ----------
        job_id {int} -- Job Id.
        '''
        self.job_comment_queryable = self.job_comment_queryable.filter(
            JobComment.job_id == job_id
        )
        return self
