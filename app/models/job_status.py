"""Job status model.
"""
from database import db


class JobStatus(db.Model):
    """Job status model

    Parameters
    ----------
    db : Model
    """
    __tablename__ = 'job_status'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(64))

    def __repr__(self):
        return '<Job status %s>' % self.description
