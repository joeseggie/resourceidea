"""
Tests suite configuration.
"""
import json
import os

from faker import Faker
from faker.providers import color
from faker.providers import date_time
from faker.providers import lorem
from faker.providers import misc
from faker.providers import person
from faker.providers import profile
import pytest

from app import create_app
from app.client.models import Client
from app.employee.models import Employee
from app.engagement.models import Engagement
from app.client_industry.models import ClientIndustry
from app.job.models import Job
from app.line_of_service.models import LineOfService
from app.organization.models import Organization
from app.role.models.role import Role
from app.role.repositories.role_repository import RoleRepository
from app.user.models import UserAccount
from database import db as _db


@pytest.fixture(scope='session')
def seed_data(app):
    """Seed data"""
    seed_filename = os.path.join(app.root_path, '../', 'seed_data.json')
    with open(seed_filename) as seed_file:
        seed_data = json.load(seed_file)
    return seed_data


@pytest.fixture(scope='session')
def app(request):
    """session-wide test Flask application"""
    app = create_app('testing')
    ctx = app.app_context()
    ctx.push()

    def teardown():
        """
        Clean up test session.
        """
        ctx.pop()

    request.addfinalizer(teardown)
    return app


@pytest.fixture(scope='session')
def db(app):
    """
    Setup database resource for the test suite.
    """
    _db.create_all()
    return _db


@pytest.fixture(scope='function')
def session(db, request, seed_data):
    """Create a new database session for the tests"""
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session = db.create_scoped_session(options=options)

    db.session = session

    client_industry_seed = seed_data['client_industry']
    client_industry_1 = ClientIndustry(**client_industry_seed)

    organization_seed = seed_data['organization']
    organization_1 = Organization(**organization_seed)

    user_account_seed = seed_data['user_account']
    user_account_seed['organization_id'] = organization_1.id
    user_1 = UserAccount(**user_account_seed)

    client_seed = seed_data['client']
    client_seed['organization_id'] = organization_1.id
    client_seed['client_industry_id'] = client_industry_1.id
    client_1 = Client(**client_seed)

    line_of_service_seed = seed_data['line_of_service']
    line_of_service_seed['organization_id'] = organization_1.id
    line_of_service_1 = LineOfService(**line_of_service_seed)

    engagement_seed = seed_data['engagement']
    engagement_seed['client_id'] = client_1.id
    engagement_seed['line_of_service_id'] = line_of_service_1.id
    engagement_seed['organization_id'] = organization_1.id
    engagement_1 = Engagement(**engagement_seed)

    employee_seed = seed_data['employee']
    employee_seed['user_account_id'] = user_1.id
    employee_seed['organization_id'] = organization_1.id
    employee_1 = Employee(**employee_seed)

    job_seed = seed_data['job']
    job_seed['engagement_id'] = engagement_1.id
    job_seed['organization_id'] = organization_1.id
    job_1 = Job(**job_seed)

    administrator_role = RoleRepository.get_by_name('administrator')
    if not administrator_role:
        role_1 = Role(name='Administrator', normalized_name='administrator')
        db.session.add(role_1)

    db.session.add(organization_1)
    db.session.add(user_1)
    db.session.add(client_industry_1)
    db.session.add(client_1)
    db.session.add(line_of_service_1)
    db.session.add(engagement_1)
    db.session.add(employee_1)
    db.session.add(job_1)
    db.session.commit()

    def teardown():
        """Clean up test suite."""
        transaction.rollback()
        connection.close()
        session.remove()

    request.addfinalizer(teardown)
    return session


@pytest.fixture(scope='function')
def fake_person():
    """Create a fake person for the test suite."""
    fake_person = Faker()
    fake_person.add_provider(person)
    return fake_person


@pytest.fixture(scope='function')
def fake_profile():
    """Create a fake user profile for the test suite."""
    fake_profile = Faker()
    fake_profile.add_provider(profile)
    return fake_profile


@pytest.fixture(scope='function')
def fake_misc():
    """Create a misc faker"""
    fake_misc = Faker()
    fake_misc.add_provider(misc)
    return fake_misc


@pytest.fixture(scope='function')
def fake_lorem():
    """Create a lorem faker"""
    fake_lorem = Faker()
    fake_lorem.add_provider(lorem)
    return fake_lorem


@pytest.fixture(scope='function')
def fake_datetime():
    """Create fake datetime"""
    fake_datetime = Faker()
    fake_datetime.add_provider(date_time)
    return fake_datetime


@pytest.fixture(scope='function')
def fake_color():
    """Create fake color"""
    fake_color = Faker()
    fake_color.add_provider(color)
    return fake_color
