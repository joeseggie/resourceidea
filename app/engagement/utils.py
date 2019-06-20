"""app.engagement.utils module"""
from typing import List
from uuid import UUID

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


def update_engagement(engagement_id: UUID, **kwargs) -> Engagement:
    """
    Updates an engagement.

    Args:
        engagement_id (UUID): ID of engagement to be updated.

    Returns:
        Engagement updated.

    Raises:
        ValueError if the engagement with the ID specified does not exist.
    """
    engagement_for_update = EngagementRepository.get_one_by_id(engagement_id)
    if not engagement_for_update:
        raise ValueError('Engagement with ID specified does not exist.')

    update_fields = ('title', 'description', 'start_date', 'end_date',
                     'color', 'status', 'client_id', 'line_of_service_id',
                     'organization_id',)
    return EngagementRepository.update_by_id(
        model_id=engagement_id,
        fields_for_update=update_fields,
        **kwargs)


def list_engagements() -> List[Engagement]:
    """
    List engagements.

    Returns:
        List of engagements.
    """
    return EngagementRepository.get_all()
