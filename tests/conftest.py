import os

import pytest

from app import create_app
from app.organization.models import Organization
from database import db as _db


@pytest.fixture(scope='session')
def app(request):
    """session-wide test Flask application"""
    app = create_app('testing')
    ctx = app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return app


@pytest.fixture(scope='session')
def db(app, request):
    def teardown():
        _db.drop_all()

    _db.app = app
    _db.create_all()

    request.addfinalizer(teardown)
    return _db


@pytest.fixture(scope='function')
def session(db, request):
    """Create a new database session for the tests"""
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session = db.create_scoped_session(options=options)

    db.session = session

    company_1 = Organization(
        id='91c4b0b8-cf94-4b0b-8986-58c94aa2c578',
        name='Company 1',
        name_slug='organization-1',
        address='Company 1 address')
    company_2 = Organization(
        name='Company 2',
        name_slug='organization-2',
        address='Company 2 address')

    db.session.add(company_1)
    db.session.add(company_2)

    db.session.commit()

    def teardown():
        transaction.rollback()
        connection.close()
        session.remove()

    request.addfinalizer(teardown)
    return session
