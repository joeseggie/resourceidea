"""app.engagement.utils module"""
from datetime import date
from app.client.utils import list_clients
from app.engagement.models import Engagement
from app.engagement.utils import create_engagement
from app.engagement.utils import update_engagement
from app.client_industry.utils import list_client_industries


def test_create_engagement(session, fake_lorem, fake_color):
    """Test create_engagement function"""

    # Arrange
    fake_client = next(iter(list_clients() or []), None)
    fake_industry = next(iter(list_client_industries() or []), None)
    fake_start_date = date.today()
    fake_end_date = date.today()

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


def test_update_engagement(session, fake_lorem, fake_color):
    """Test update_engagement function"""

    # Arrange
    fake_client = next(iter(list_clients() or []), None)
    fake_industry = next(iter(list_client_industries() or []), None)
    fake_start_date = date.today()
    fake_end_date = date.today()
    fake_engagement = create_engagement(
        title=fake_lorem.word(),
        description=fake_lorem.word(),
        start_date=fake_start_date,
        end_date=fake_end_date,
        color=fake_color.hex_color(),
        client_id=fake_client.id,
        client_industry_id=fake_industry.id)
    update_data = {
        'title': 'Change titled',
        'description': 'Description of the engagement changed.',
        'start_date': date.today(),
        'end_date': date.today(),
        'color': '#EEE000',
        'client_id': fake_client.id,
        'client_industry_id': fake_industry.id
    }
    origin_title = fake_engagement.title
    origin_description = fake_engagement.description
    origin_color = fake_engagement.color

    # Act
    result = update_engagement(fake_engagement.id, **update_data)
    print(result.title, fake_engagement.title)

    # Assert
    if not isinstance(result, Engagement):
        raise AssertionError()
    if result.id != fake_engagement.id:
        raise AssertionError()
    if result.title == origin_title:
        raise AssertionError()
    if result.description == origin_description:
        raise AssertionError()
    if result.color == origin_color:
        raise AssertionError()
