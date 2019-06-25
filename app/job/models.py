"""app.job.models module"""
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.common.enums import JobStatus
from app.common.models import BaseModel
from database import db


class Job(BaseModel):
    """Job model"""

    __tablename__ = 'job'

    title = db.Column(db.String(256))
    description = db.Column(db.String(256), nullable=True)
    start_date = db.Column(db.Date, nullable=True)
    completion_date = db.Column(db.Date, nullable=True)
    status = db.Column(db.Enum(JobStatus), default=JobStatus.NOT_STARTED)

    engagement_id = db.Column(UUID, db.ForeignKey('engagement.id'))
    engagement = relationship('Engagement')

    organization_id = db.Column(UUID, db.ForeignKey('organization.id'))
    organization = relationship('Organization')

    manager_id = db.Column(UUID, nullable=True)

    def __repr__(self):
        return '<Job %s>' % self.title
