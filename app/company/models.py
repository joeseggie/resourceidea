"""Company model
"""
from app.common.enums import CompanyStatus
from app.common.utils import default_uuid_pk
from database import db


class Company(db.Model):
    """Company model.

    Parameters
    ----------
    db : Model
    """
    __tablename__ = 'company'

    id = default_uuid_pk()
    name = db.Column(db.String(256))
    name_stub = db.Column(db.String(256))
    address = db.Column(db.String(256))
    status = db.Column(db.Enum(CompanyStatus))

    def __repr__(self):
        return '<Company %s>' % self.name
