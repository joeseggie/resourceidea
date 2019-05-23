from marshmallow import fields
from marshmallow import Schema
from marshmallow.validate import OneOf


class UsersListFilterSchema(Schema):
    sort_key = fields.String(
        OneOf(choices=['username', 'email', 'phone_number']),
        missing='username')
    sort_order = fields.String(missing='asc')


class UsersListSchema(Schema):
    username = fields.String()
    email = fields.String()
    phone_number = fields.String()


class UserInputSchema(Schema):
    username = fields.String()
    password = fields.String()
    confirm_password = fields.String()
    email = fields.String()
    confirm_email = fields.String()
    phone_number = fields.String()
