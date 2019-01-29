"""Job model.
"""
from app import db


class Job(db.Model):
    """Job model.

    Parameters
    ----------
    db : Model
    """
    __tablename__ = 'job'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(256))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    color = db.Column(db.String(7))
    manager_id = db.Column(db.Integer, db.ForeignKey('resource.id'))
    manager = db.relationship(
        'Resource',
        backref='jobs_managed'
    )
    partner_id = db.Column(db.Integer, db.ForeignKey('resource.id'))
    partner = db.relationship(
        'Resource',
        backref='jobs_as_partner'
    )

    job_status_id = db.Column(db.Integer, db.ForeignKey('job_status.id'))
    job_status = db.relationship('JobStatus', backref='jobs')

    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    client = db.relationship('Client', backref='jobs')

    line_of_service_id = db.Column(db.Integer, db.ForeignKey(
        'line_of_service.id'
    ))
    line_of_service = db.relationship('LineOfService', backref='jobs')
