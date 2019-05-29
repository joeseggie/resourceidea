from app.organization.utils import create_organization


def signup(**kwargs):
    """
    Signup new subscription.
    """
    return create_organization(**kwargs)
