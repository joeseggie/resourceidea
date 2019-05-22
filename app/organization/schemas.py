from marshmallow import fields
from marshmallow import Schema
from marshmallow.validate import OneOf
from marshmallow_enum import EnumField

from app.common.enums import CompanyStatus


class CompanyViewSchema(Schema):
    id = fields.UUID()
    name = fields.String()
    name_slug = fields.String()
    address = fields.String()
    status = EnumField(CompanyStatus)


class CompanyCreatedSchema(Schema):
    status = fields.String()
    code = fields.Integer()
    data = fields.Nested(CompanyViewSchema)


class CompanyListSchema(Schema):
    status = fields.String()
    code = fields.Integer()
    data = fields.Nested(CompanyViewSchema, many=True)


class CompanyListFilterSchema(Schema):
    sort_key = fields.String(OneOf(['name', 'status']), missing='name')
    sort_order = fields.String(missing='asc')


class CompanyInputSchema(Schema):
    name = fields.String(required=True)
    address = fields.String(required=True)
