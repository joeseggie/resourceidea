from marshmallow import fields
from marshmallow import pre_dump
from marshmallow import Schema
from marshmallow import validates_schema
from marshmallow import ValidationError


class SignupInputSchema(Schema):
    """
    Signup input schema
    """
    name = fields.String(required=True, load_from='organization')
    address = fields.String()
    username = fields.String(required=True)
    password = fields.String(required=True)
    confirm_password = fields.String(required=True)
    email = fields.Email(required=True)
    phone_number = fields.String()
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    other_names = fields.String()
    file_number = fields.String()

    @validates_schema
    def validate_password(self, data):
        if data['password'] != data['confirm_password']:
            raise ValidationError('Please confirm password to signup.')


class SignupDataSchema(Schema):
    """
    Schema for the data response
    """
    organization_id = fields.UUID(attribute='Organization.id')
    organization = fields.String(attribute='Organization.name')
    organization_slug = fields.String(attribute='Organization.name_slug')
    user_id = fields.UUID(attribute='UserAccount.id')
    username = fields.String(attribute='UserAccount.username')

    @pre_dump
    def prepare_data(self, data):
        organization, user_account = data
        return {'Organization': organization, 'UserAccount': user_account}


class SignupOutputSchema(Schema):
    """
    Signup output schema
    """
    status = fields.String()
    data = fields.Nested(SignupDataSchema)
