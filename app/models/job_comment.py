"""Job comment model.
"""
from app import db


class JobComment(db.Model):
    """Job comment model.

    Parameters
    ----------
    db : Model
    """
    __tablename__ = 'job_comment'

    id = db.Column(db.Integer, primary_key=True)
    details = db.Column(db.String(256))
    made = db.Column(db.DateTime)

    job_id = db.Column(db.Integer, db.ForeignKey('job.id'))
    job = db.relationship('Job', backref=db.backref(
        'job_comments',
        lazy=True
    ))

    resource_id = db.Column(db.Integer, db.ForeignKey('resource.id'))
    resource = db.relationship('Resource', backref='job_comments')
