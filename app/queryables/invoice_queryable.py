'''InvoiceQueryable module.
'''
from datetime import datetime
from ..models.invoice import Invoice


class InvoiceQueryable:
    '''Invoice queryable.
    '''
    def __init__(self):
        '''Constructor.
        '''
        self.invoice_queryable = Invoice.query

    def to_list(self):
        '''List invoices.
        '''
        query_result = self.invoice_queryable.all()
        invoices_list = [{
            'Id': result.id,
            'Amount': result.amount,
            'InvoiceDate': result.invoice_date,
            'PeriodStart': result.invoice_period_start,
            'PeriodEnd': result.invoice_period_end,
            'SubscriptionId': result.subscription_id
        } for result in query_result]
        return invoices_list

    def invoiced_before(self, invoice_date: datetime):
        '''Filter invoices created before a given date.

        Parameters
        ----------
        invoice_date {datetime} -- Invoices filtering date.
        '''
        self.invoice_queryable = self.invoice_queryable.filter(
            Invoice.invoice_date < invoice_date
        )
        return self

    def invoiced_after(self, invoice_date: datetime):
        '''Filter invoices created after a given date.

        Parameters
        ----------
        invoice_date {datetime} -- Invoices filtering date.
        '''
        self.invoice_queryable = self.invoice_queryable.filter(
            Invoice.invoice_date > invoice_date
        )
        return self

    def company_is(self, company_id: int):
        '''Filter invoices by company.

        Parameters
        ----------
        company_id {int} -- Company Id.
        '''
        self.invoice_queryable = self.invoice_queryable.filter(
            Invoice.subscription.has(company_id=company_id)
        )
        return self

    def subscription_is(self, subscription_id: int):
        '''Filter invoices by subscription.

        Parameters
        ----------
        subscription_id {int} -- Subscription Id.
        '''
        self.invoice_queryable = self.invoice_queryable.filter(
            Invoice.subscription_id == subscription_id
        )
        return self
