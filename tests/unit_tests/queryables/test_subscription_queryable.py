'''Subscription queryable unit tests.
'''
from unittest.mock import Mock

from app.queryables.subscription_queryable import SubscriptionQueryable


class TestSubscriptionQueryable:
    '''Test subscription queryable.
    '''
    def test_to_list_returns_list(self):
        '''Test to_list method returns list.
        '''
        queryable = SubscriptionQueryable()
        result = queryable.to_list()
        assert isinstance(result, list)

    def test_where_company_is_returns_SubscriptionQueryable(self):
        '''Test where_company_is method returns SubscriptionQueryable.
        '''
        queryable = SubscriptionQueryable()
        company_id = Mock()
        result = queryable.where_company_is(company_id)
        assert isinstance(result, SubscriptionQueryable)
