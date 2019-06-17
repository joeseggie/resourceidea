"""LineOfService model schemas"""
from marshmallow import fields
from marshmallow import Schema


class LineOfServiceSchema(Schema):
    """Line of service schema."""
    id = fields.String()
    name = fields.String(required=True)