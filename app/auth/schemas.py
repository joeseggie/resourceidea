from marshmallow import fields
from marshmallow import pre_dump
from marshmallow import Schema


class SignupInputSchema(Schema):
    """
    Signup input schema
    """
    name = fields.String(required=True, load_from='organization')
    address = fields.String(required=True)


class SignupDataSchema(Schema):
    """
    Schema for the data response
    """
    name = fields.String(dump_to='organization')
    address = fields.String()
    status = fields.String()
    name_slug = fields.String()

    @pre_dump
    def get_status_value(self, data):
        data.status = data.status.value
        return data


class SignupOutputSchema(Schema):
    """
    Signup output schema
    """
    status = fields.String()
    data = fields.Nested(SignupDataSchema)
