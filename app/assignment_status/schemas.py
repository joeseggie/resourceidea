from marshmallow import fields
from marshmallow import Schema


class AssignmentStatusSchema(Schema):
    id = fields.Integer(required=True)
    description = fields.String(required=True)


class AssignmentStatusListOutputSchema(Schema):
    status = fields.String(required=True)
    code = fields.Integer()
    data = fields.Nested(AssignmentStatusSchema, many=True)


class NewAssignmentStatusInputSchema(Schema):
    description = fields.String(required=True)


class NewAssignmentStatusOutputSchema(Schema):
    status = fields.String(required=True)
    code = fields.Integer()
    data = fields.Nested(AssignmentStatusSchema)
