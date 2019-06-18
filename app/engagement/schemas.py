"""app.engagement.schemas module"""
from marshmallow import fields
from marshmallow import Schema
from marshmallow_enum import EnumField

from app.common.enums import EngagementStatus


class EngagementSchema(Schema):
    """Engagement schema"""

    id = fields.UUID()
    title = fields.String(required=True)
    description = fields.String()
    start_date = fields.Date()
    end_date = fields.Date()
    color = fields.String()
    status = EnumField(EngagementStatus)
