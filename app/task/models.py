"""app.task.models module"""
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.common.enums import TaskStatus
from app.common.models import BaseModel
from database import db


class Task(BaseModel):
    """Task model"""

    __tablename__ = 'task'

    title = db.Column(db.String(256))
    description = db.Column(db.String(256), nullable=True)
    status = db.Column(db.Enum(TaskStatus), default=TaskStatus.NOT_STARTED)

    job_id = db.Column(UUID, db.ForeignKey('job.id'))
    job = relationship('Job')
