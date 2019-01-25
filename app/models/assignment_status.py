"""Assignment status model
"""
from app import db


class AssignmentStatus(db.Model):
    """Assignment status model.

    Parameters
    ----------
    db : Model
    """
    __tablename__ = 'assignment_status'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(50))

    def __repr__(self):
        return '<Assignment status %s>' % self.description
