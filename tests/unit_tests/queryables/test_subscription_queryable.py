'''Subscription queryable unit tests.
'''
import unittest
from unittest.mock import Mock

from app.queryables.subscription_queryable import SubscriptionQueryable


class TestSubscriptionQueryable(unittest.TestCase):
    '''Test subscription queryable.
    '''
    def test_to_list_returns_list(self):
        '''Test to_list method returns list.
        '''
        queryable = SubscriptionQueryable()
        result = queryable.to_list()
        self.assertIsInstance(result, list)

    def test_where_company_is_returns_SubscriptionQueryable(self):
        '''Test where_company_is method returns SubscriptionQueryable.
        '''
        queryable = SubscriptionQueryable()
        company_id = Mock()
        result = queryable.where_company_is(company_id)
        self.assertIsInstance(result, SubscriptionQueryable)
