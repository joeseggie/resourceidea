"""Department model.
"""
from database import db


class Department(db.Model):
    """Department model.

    Parameters
    ----------
    db : Model
    """
    __tablename__ = 'department'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

    company_id = db.Column(
        db.Integer,
        db.ForeignKey('company.id')
    )
    company = db.relationship(
        'Company',
        backref='departments'
    )
