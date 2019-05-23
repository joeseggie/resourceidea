"""Line of service model.
"""
from database import db


class LineOfService(db.Model):
    """Line of service model.

    Parameters
    ----------
    db : Model
    """
    __tablename__ = 'line_of_service'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

    company_id = db.Column(db.Integer, db.ForeignKey('organization.id'))
    company = db.relationship('Company', backref='lines_of_service')

    def __repr__(self):
        return '<Line of service %r>' % self.name
