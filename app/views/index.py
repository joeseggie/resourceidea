from flask_restful import Resource


class Index(Resource):
    '''
    Index API resource
    '''
    def get(self):
        return {'message': 'Welcome to the ResourceIdea API'}
