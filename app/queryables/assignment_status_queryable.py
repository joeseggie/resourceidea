"""Assignment status queryable.
"""
from app.models.assignment_status import AssignmentStatus


class AssistantStatusQueryable:
    """Query assignment statuses.
    """

    def __init__(self):
        """Constructor.
        """
        self.assignment_status_queryable = AssignmentStatus.query

    def to_list(self):
        """Get list of assignment statuses.
        """
        query_result = self.assignment_status_queryable.all()
        assignment_statuses_list = [{
            'Id': result.id,
            'Description': result.description
        } for result in query_result]
        return assignment_statuses_list
