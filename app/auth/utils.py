from app.organization.utils import create_organization
from app.organization.utils import get_organization_by_name
from app.user.utils import create_user


def signup(**kwargs):
    """
    Signup new subscription.
    """
    organization_exists = get_organization_by_name(**kwargs)
    if organization_exists:
        raise ValueError('Organization name already exists')

    new_organization = create_organization(
        organization_name=kwargs['name'],
        address=kwargs.get('address', None))

    new_user = create_user(
        organization_id=new_organization.id,
        username=kwargs['username'],
        password=kwargs['password'],
        email=kwargs['email'],
        phone_number=kwargs.get('phone_number', None))

    return new_organization, new_user
