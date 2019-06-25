"""app.resource.schemas module"""
from marshmallow import fields
from marshmallow import Schema


class ResourceSchema(Schema):
    id = fields.UUID()
    employee_id = fields.UUID(required=True)
    color = fields.String()
    organization_id = fields.UUID(required=True)
