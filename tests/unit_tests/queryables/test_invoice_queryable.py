'''Test InvoiceQueryable.
'''
from datetime import datetime
import unittest
from unittest.mock import Mock

from app.queryables.invoice_queryable import InvoiceQueryable


class TestInvoiceQueryable(unittest.TestCase):
    '''Test InvoiceQueryable.
    '''
    def test_to_list(self):
        '''Test to_list method.
        '''
        queryable = InvoiceQueryable()
        result = queryable.to_list()
        self.assertIsInstance(result, list)

    def test_invoiced_after(self):
        '''Test invoiced_before method.
        '''
        queryable = InvoiceQueryable()
        invoice_date = datetime.now()
        result = queryable.invoiced_after(invoice_date)
        self.assertIsInstance(result, InvoiceQueryable)

    def test_invoiced_before(self):
        '''Test invoiced_before method.
        '''
        queryable = InvoiceQueryable()
        invoice_date = datetime.now()
        result = queryable.invoiced_before(invoice_date)
        self.assertIsInstance(result, InvoiceQueryable)

    def test_subscription_is(self):
        '''Test subscription_is method.
        '''
        queryable = InvoiceQueryable()
        subscription_id = Mock()
        result = queryable.subscription_is(subscription_id)
        self.assertIsInstance(result, InvoiceQueryable)

    def test_company_is(self):
        '''Test where_company_is method.
        '''
        queryable = InvoiceQueryable()
        mock_company_id = Mock()
        result = queryable.company_is(mock_company_id)
        self.assertIsInstance(result, InvoiceQueryable)
