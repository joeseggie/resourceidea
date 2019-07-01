"""app.task.schemas module"""
from marshmallow import fields
from marshmallow import Schema
from marshmallow_enum import EnumField

from app.common.enums import TaskStatus


class TaskSchema(Schema):
    """Task schema"""
    id = fields.UUID()
    title = fields.String(required=True)
    description = fields.String()
    status = EnumField(TaskStatus)
    job_id = fields.UUID()
