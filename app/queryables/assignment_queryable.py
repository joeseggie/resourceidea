"""Assignment queryable.
"""
from datetime import datetime

from sqlalchemy.orm.query import Query

from app.models.assignment import Assignment


class AssignmentQueryable:
    """Assignment queryable.
    """

    def __init__(self):
        """Constructor.
        """
        self.assignment_queryable = Assignment.query

    def to_list(self) -> list:
        """Return list of assignments.

        Returns
        -------
        List -- List of assignments.
        """
        pass

    def starts_before(self, filter_date: datetime) -> Query:
        """Get assignments that start before the filter date.

        Parameters
        ----------
        filter_date {datetime} -- Date used to filter results.
        """
        self.assignment_queryable = self.assignment_queryable.filter(
            Assignment.starts < filter_date
        )
        return self

    def starts_after(self, filter_date: datetime) -> Query:
        """Get assignments that start after the filter date.

        Parameters
        ----------
        filter_date {datetime} -- Date used to filter results.

        Returns
        -------
        Query -- sqlalchemy.orm.query.Query object.
        """
        self.assignment_queryable = self.assignment_queryable.filter(
            Assignment.start > filter_date
        )
        return self

    def ends_before(self, filter_date: datetime) -> Query:
        """Get assignments that end before the filter date.

        Parameters
        ----------
        filter_date {datetime} -- Date used to filter results.

        Returns
        -------
        Query -- sqlalchemy.orm.query.Query object.
        """
        self.assignment_queryable = self.assignment_queryable.filter(
            Assignment.ends < filter_date
        )
        return self

    def ends_after(self, filter_date: datetime) -> Query:
        """Get assignments that end after the filter date.

        Parameters
        ----------
        filter_date {datetime} -- Date used to filter results.

        Returns
        -------
        Query -- sqlalchemy.orm.query.Query object.
        """
        self.assignment_queryable = self.assignment_queryable.filter(
            Assignment.ends > filter_date
        )
        return self

    def where_resource_is(self, resource_id: int) -> Query:
        """Get assignments that belong to resource with Id specified.

        Parameters
        ----------
        resource_id {int} -- Resource Id.

        Returns
        -------
        Query -- sqlalchemy.orm.query.Query object.
        """
        self.assignment_queryable = self.assignment_queryable.filter_by(
            resource_id=resource_id
        )
        return self

    def where_assignment_status_is(self, assignment_status_id: int) -> Query:
        """Get assignments of a given status.

        Parameters
        ----------
        assignment_status_id {int} -- Assignment status Id.

        Returns
        -------
        Query -- sqlalchemy.orm.query.Query object.
        """
        self.assignment_queryable = self.assignment_queryable.filter_by(
            assignment_status_id=assignment_status_id
        )
        return self

    def where_job_task_is(self, job_task_id: int) -> Query:
        """Get assignments that belong to a job task.

        Parameters
        ----------
        job_task_id {int} -- Job task Id.

        Returns
        -------
        Query -- sqlalchemy.orm.query.Query object.
        """
        self.assignment_queryable = self.assignment_queryable.filter_by(
            job_task_id=job_task_id
        )
        return self
