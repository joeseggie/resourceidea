from app.employee.models import Employee
from app.employee.repository import EmployeeRepository
from app.employee.utils import file_number_exists
from app.employee.utils import generate_file_number
from app.organization.utils import create_organization
from app.organization.utils import organization_name_exists
from app.messenger.utils import send_email
from app.role.models.user_role import UserRole
from app.role.repositories.role_repository import RoleRepository
from app.role.repositories.user_role_repository import UserRoleRepository
from app.user.utils import create_user
from app.user.utils import email_exists
from app.user.utils import phone_number_exists
from app.user.utils import username_exists


def signup(**kwargs):
    """
    Signup new subscription.
    """
    if organization_name_exists(kwargs['name']):
        raise ValueError('Organization name already exists')

    if email_exists(kwargs['email']):
        raise ValueError('Email already exists')

    if 'phone_number' in kwargs\
            and phone_number_exists(kwargs['phone_number']):
        raise ValueError('Phone number already exists')

    if username_exists(kwargs['username']):
        raise ValueError('Username is already taken')

    file_number = kwargs.get('file_number', generate_file_number())
    if file_number_exists(file_number):
        raise ValueError('File number already exists')

    new_organization = create_organization(
        organization_name=kwargs['name'],
        address=kwargs.get('address', None))

    new_user = create_user(
        organization_id=new_organization.id,
        username=kwargs['username'],
        password=kwargs['password'],
        email=kwargs['email'],
        phone_number=kwargs.get('phone_number', None))

    administrator_role = RoleRepository.get_by_name('administrator')

    UserRoleRepository.create(
        UserRole(user_account_id=new_user.id, role_id=administrator_role.id))

    new_employee = Employee(
        file_number=file_number,
        first_name=kwargs['first_name'],
        last_name=kwargs['last_name'],
        user_account_id=new_user.id,
        organization_id=new_organization.id,
        other_names=kwargs.get('other_names', None))
    EmployeeRepository.create(new_employee)

    recipients = [kwargs['email'], ]
    subject = f'Welcome {kwargs["first_name"]} {kwargs["last_name"]}'
    body_text = f'Dear {kwargs["first_name"]} {kwargs["last_name"]},\n'\
                'Thank you for joining us.'
    body_html = f'Dear {kwargs["first_name"]} {kwargs["last_name"]},\n'\
                'Thank you for joining us.'

    send_email(recipients, subject, body_text, body_html)

    return new_organization, new_user
