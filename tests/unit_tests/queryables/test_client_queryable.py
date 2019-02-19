"""Test client queryable.
"""
from unittest.mock import Mock

from app.queryables.client_queryable import ClientQueryable


class TestClientQueryable:
    def test_to_list_returns_list(self):
        """Test to_list method returns a list.
        """
        queryable = ClientQueryable()
        result = queryable.to_list()
        assert isinstance(result, list)

    def test_where_company_is_returns_Query(self):
        """Test where_company_is returns Query object.
        """
        queryable = ClientQueryable()
        company_id = Mock()
        result = queryable.where_company_is(company_id)
        assert isinstance(result, ClientQueryable)
