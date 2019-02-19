"""Test client industry queryable.
"""
from unittest.mock import Mock

from app.queryables.client_industry_queryable import ClientIndustryQueryable


class TestClientIndustryQueryable:
    def test_to_list_returns_list(self):
        """Tests if to_list method returns a list.
        """
        queryable = ClientIndustryQueryable()
        result = queryable.to_list()
        assert isinstance(result, list)

    def test_where_company_is_returns_Query(self):
        """Test if the where_company_is method returns
        a ClientIndustryQueryable object.
        """
        queryable = ClientIndustryQueryable()
        company_id = Mock()
        result = queryable.where_company_is(company_id)
        assert isinstance(result, ClientIndustryQueryable)
