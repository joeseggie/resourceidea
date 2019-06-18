"""app.engagement.utils module"""
from app.engagement.models import Engagement
from app.engagement.repositories import EngagementRepository


def create_engagement(**kwargs) -> Engagement:
    """
    Create engagement.

    Returns:
        Engagement created.
    """
    new_engagement = Engagement(
        title=kwargs['title'],
        description=kwargs.get('description', None),
        start_date=kwargs.get('start_date', None),
        end_date=kwargs.get('end_date', None),
        color=kwargs.get('color', None),
        client_id=kwargs['client_id'],
        line_of_service_id=kwargs.get('line_of_service_id'))

    return EngagementRepository.create(new_engagement)
