"""Job position model.
"""
from app import db


class JobPosition(db.Model):
    """Job position model.

    Parameters
    ----------
    db : Model
    """
    __tablename__ = 'job_position'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    level = db.Column(db.Integer)

    department_id = db.Column(
        db.Integer,
        db.ForeignKey('department.id')
    )
    department = db.relationship(
        'Department',
        backref='job_positions')
