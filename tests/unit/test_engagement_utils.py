"""app.engagement.utils module"""
from datetime import date
from app.client.utils import list_clients
from app.engagement.models import Engagement
from app.engagement.utils import create_engagement
from app.client_industry.utils import list_client_industries


def test_create_engagement(session, fake_lorem, fake_color):
    """Test create_engagement function"""

    # Arrange
    fake_client = next(iter(list_clients() or []), None)
    fake_industry = next(iter(list_client_industries() or []), None)
    fake_start_date = date.today()
    fake_end_date = date.today()

    print(fake_start_date, fake_end_date)

    # Act
    result = create_engagement(
        title=fake_lorem.word(),
        description=fake_lorem.word(),
        start_date=fake_start_date,
        end_date=fake_end_date,
        color=fake_color.hex_color(),
        client_id=fake_client.id,
        client_industry_id=fake_industry.id)

    # Assert
    if not isinstance(result, Engagement):
        raise AssertionError()
