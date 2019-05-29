"""Assignment status model
"""
from database import db


class AssignmentStatus(db.Model):
    """Assignment status model.

    Parameters
    ----------
    db : Model
    """
    __tablename__ = 'assignment_status'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(50))
    # assignments = db.relationship(
    #     'Assignment',
    #     backref='assignment_status',
    #     lazy='dynamic'
    # )
