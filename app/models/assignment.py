"""Assignment model.
"""
from database import db


class Assignment(db.Model):
    """Assignment model

    Parameters
    ----------
    db : Model
    """
    __tablename__ = 'assignment'

    id = db.Column(db.Integer, primary_key=True)
    starts = db.Column(db.DateTime)
    ends = db.Column(db.DateTime)

    # resource_id = db.Column(db.Integer, db.ForeignKey('resource.id'))
    # resource = db.relationship('Resource', backref='assignments')

    # job_task_id = db.Column(db.Integer, db.ForeignKey('job_task.id'))
    # job_task = db.relationship('JobTask', backref='assignments')

    assignment_status_id = db.Column(db.Integer, db.ForeignKey(
        'assignment_status.id'
    ))
