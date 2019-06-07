import pytest

from app import create_app
from app.organization.models import Organization
from app.role.models.role import Role
from app.role.repositories.role_repository import RoleRepository
from app.user.models import UserAccount
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
    _db.create_all()
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
        name='Organization 1',
        name_slug='organization-1',
        address='Organization 1 address')
    company_2 = Organization(
        name='Organization 2',
        name_slug='organization-2',
        address='Organization 2 address')

    user_1 = UserAccount(
        username='test_user',
        password='password',
        email='mail@example.com',
        phone_number='000-0000-111',
        organization_id=company_2.id)

    user_2 = UserAccount(
        username='another_user',
        password='password',
        email='sample_mail@example.com',
        phone_number='000-2222-111',
        organization_id=company_2.id)

    administrator_role = RoleRepository.get_by_name('administrator')
    if not administrator_role:
        role_1 = Role(name='Administrator', normalized_name='administrator')
        db.session.add(role_1)

    db.session.add(company_1)
    db.session.add(company_2)
    db.session.add(user_1)
    db.session.add(user_2)
    db.session.commit()

    def teardown():
        transaction.rollback()
        connection.close()
        session.remove()

    request.addfinalizer(teardown)
    return session
