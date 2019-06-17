"""Line of service model.
"""
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.common.models import BaseModel
from database import db


class LineOfService(BaseModel):
    """Line of service model.

    Args:
        BaseModel: Base model.
    """

    __tablename__ = 'line_of_service'

    name = db.Column(db.String(128))

    organization_id = db.Column(UUID, db.ForeignKey('organization.id'))
    organization = relationship('Organization')

    def __repr__(self):
        return '<Line of service %s>' % self.name
