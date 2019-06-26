"""app.job.schemas modules"""
from marshmallow import fields
from marshmallow import Schema
from marshmallow_enum import EnumField

from app.common.enums import JobStatus


class JobSchema(Schema):
    """Job schema"""
    id = fields.UUID()
    title = fields.String(required=True)
    description = fields.String()
    start_date = fields.Date()
    completion_date = fields.Date()
    status = EnumField(JobStatus)
    engagement_id = fields.UUID()
    organization_id = fields.UUID()
    manager_id = fields.UUID()
