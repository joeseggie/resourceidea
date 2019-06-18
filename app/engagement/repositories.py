"""app.engagement.repositories module"""
from app.common.base_repository import BaseRepository
from app.engagement.models import Engagement


class EngagementRepository(BaseRepository):
    """
    EngagementRepository.
    """
    model_class = Engagement
