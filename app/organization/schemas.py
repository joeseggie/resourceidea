from marshmallow import fields
from marshmallow import Schema
from marshmallow.validate import OneOf
from marshmallow_enum import EnumField

from app.common.enums import OrganizationStatus


class OrganizationViewSchema(Schema):
    id = fields.UUID()
    name = fields.String()
    name_slug = fields.String()
    address = fields.String()
    status = EnumField(OrganizationStatus)


class OrganizationCreatedSchema(Schema):
    status = fields.String()
    code = fields.Integer()
    data = fields.Nested(OrganizationViewSchema)


class OrganizationListSchema(Schema):
    status = fields.String()
    code = fields.Integer()
    data = fields.Nested(OrganizationViewSchema, many=True)


class OrganizationListFilterSchema(Schema):
    sort_key = fields.String(OneOf(['name', 'status']), missing='name')
    sort_order = fields.String(missing='asc')


class OrganizationInputSchema(Schema):
    name = fields.String(required=True)
    address = fields.String(required=True)
