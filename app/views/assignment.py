from flask_restful import fields, Resource


assignment_fields = {
    'id': fields.Integer
}


class AssignmentResource(Resource):
    def get(self):
        pass
