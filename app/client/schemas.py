"""app.client.schemas module"""
from marshmallow import fields
from marshmallow import Schema


class ClientSchema(Schema):
    """Client schema"""
    id = fields.UUID()
    name = fields.String(required=True)
    name_slug = fields.String()
    address = fields.String()
    organization_id = fields.UUID()
