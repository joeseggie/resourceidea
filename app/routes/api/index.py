from flask import Blueprint, jsonify


index_blueprint = Blueprint('index_blueprint', __name__)


@index_blueprint.route('/')
def index():
    return jsonify({
        'status': 200,
        'data': [
            {'message': 'Welcome to the ResourceIdea API'}
        ]
    }), 200
