"""Company model
"""
from app.common.enums import OrganizationStatus
from app.common.models import BaseModel
from database import db


class Organization(BaseModel):
    """
    Organization model.

    Args:
        BaseModel : Base model.
    """

    __tablename__ = 'organization'

    name = db.Column(db.String(256))
    name_slug = db.Column(db.String(256), unique=True)
    address = db.Column(db.String(256))
    status = db.Column(db.Enum(OrganizationStatus))

    def __repr__(self):
        return '<Organization %s>' % self.name
