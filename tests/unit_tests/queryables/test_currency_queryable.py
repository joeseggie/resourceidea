"""Tests for currency queryable.
"""
from unittest.mock import Mock

from app.queryables.currency_queryable import CurrencyQueryable


class TestCurrencyQueryable:
    '''Tests for currency queryable.
    '''
    def test_to_list_returns_list(self):
        '''Test to_list method returns list.
        '''
        queryable = CurrencyQueryable()
        result = queryable.to_list()
        assert isinstance(result, list)

    def test_where_company_is_returns_CurrencyQueryable(self):
        '''Test where_company_is returns CurrencyQueryable.
        '''
        queryable = CurrencyQueryable()
        company_id = Mock()
        result = queryable.where_company_is(company_id)
        assert isinstance(result, CurrencyQueryable)
