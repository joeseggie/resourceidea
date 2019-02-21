from flask import Blueprint


home_bp = Blueprint('home', __name__, url_prefix='/')


@home_bp.route('/')
def index():
    return '<h1>Hello, World!</h1>'
