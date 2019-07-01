"""
app.task_assignment.models module
"""
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.common.models import BaseModel
from database import db


class TaskAssignment(BaseModel):
    """
    Task assignment model.
    """
    __tablename__ = 'task_assignment'

    start_date_time = db.Column(db.DateTime(timezone=True), nullable=False)
    end_date_time = db.Column(db.DateTime(timezone=True), nullable=False)

    task_id = db.Column(UUID, db.ForeignKey('task.id'), nullable=False)
    task = relationship('Task')

    resource_id = db.Column(UUID, db.ForeignKey('resource.id'), nullable=True)
    resource = relationship('Resource')
