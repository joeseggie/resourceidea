"""Employee model.
"""
from app import db


class Employee(db.Model):
    """Employee model.

    Parameters
    ----------
    db : Model
    """
    __tablename__ = 'employee'

    id = db.Column(db.Integer, primary_key=True)
    file_number = db.Column(db.String(16))
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    join_date = db.Column(db.DateTime)
    termination_date = db.Column(db.DateTime)

    resource_id = db.Column(db.Integer, db.ForeignKey('resource.id'))
    resource = db.relationship(
        'Resource',
        backref=db.backref(
            'employee',
            uselist=False
        )
    )

    def __repr__(self):
        return '<Employee %r %r>' % (self.first_name, self.last_name)
