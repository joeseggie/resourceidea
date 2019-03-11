import pytest

from app import create_app, db


@pytest.fixture
def client():
    app = create_app('testing')
    client = app.test_client()
    with app.app_context() as app_context:
        app_context.push()
        db.init_app(app)
        db.create_all()

        yield client

        db.session.remove()
        db.drop_all()
        app_context.pop()
