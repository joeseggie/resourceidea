from marshmallow import fields
from marshmallow import Schema


class RoleSchema(Schema):
    Id = fields.UUID()
    name = fields.String(required=True)
