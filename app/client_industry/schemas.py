"""Client Industry schemas"""
from marshmallow import fields
from marshmallow import Schema


class ClientIndustrySchema(Schema):
    """ClientIndustry object schema"""
    id = fields.UUID()
    name = fields.String(required=True)
    name_slug = fields.String()
