"""Job model.
"""
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.common.enums import EngagementStatus
from app.common.models import BaseModel
from database import db


class Engagement(BaseModel):
    """Engagement model.

    Args:
        BaseModel: Base model.
    """

    __tablename__ = 'engagement'

    title = db.Column(db.String(256))
    description = db.Column(db.String(256))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    color = db.Column(db.String(7))
    status = db.Column(
        db.Enum(EngagementStatus),
        default=EngagementStatus.NOT_STARTED)
    manager_id = db.Column(UUID, nullable=True)
    partner_id = db.Column(UUID, nullable=True)

    client_id = db.Column(UUID, db.ForeignKey('client.id'))
    client = relationship('Client')

    line_of_service_id = db.Column(
        UUID, db.ForeignKey('line_of_service.id'))
    line_of_service = relationship('LineOfService')

    organization_id = db.Column(UUID, db.ForeignKey('organization.id'))
    organization = relationship('Organization')

    def __repr__(self):
        return '<Engagement %s>' % self.title
