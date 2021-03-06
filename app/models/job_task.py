"""Job task model.
"""
from database import db


class JobTask(db.Model):
    """Job task model.

    Parameters
    ----------
    db : Model
    """
    __tablename__ = 'job_task'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(256))

    job_id = db.Column(db.Integer, db.ForeignKey('job.id'))
    job = db.relationship('Job', backref='job_tasks')
