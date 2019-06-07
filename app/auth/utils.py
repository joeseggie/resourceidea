from app.organization.utils import create_organization
from app.organization.utils import get_organization_by_name
from app.role.models.user_role import UserRole
from app.role.repositories.role_repository import RoleRepository
from app.role.repositories.user_role_repository import UserRoleRepository
from app.user.utils import create_user
from app.user.utils import get_user_by_email
from app.user.utils import get_user_by_phone_number
from app.user.utils import get_user_by_username


def signup(**kwargs):
    """
    Signup new subscription.
    """
    organization_exists = get_organization_by_name(**kwargs)
    if organization_exists:
        raise ValueError('Organization name already exists')

    email_exists = get_user_by_email(**kwargs)
    if email_exists:
        raise ValueError('Email already exists')

    phone_number_exists = get_user_by_phone_number(**kwargs)
    if phone_number_exists:
        raise ValueError('Phone number already exists')

    username_exists = get_user_by_username(**kwargs)
    if username_exists:
        raise ValueError('Username is already taken')

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

    return new_organization, new_user
