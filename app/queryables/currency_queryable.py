"""Currency queryable.
"""
from ..models.currency import Currency


class CurrencyQueryable:
    '''Currency queryable.
    '''
    def __init__(self):
        '''Constructor.
        '''
        self.currency_queryable = Currency.query

    def to_list(self):
        '''List the currencies.
        '''
        query_result = self.currency_queryable.all()
        currencies_list = [{
            'Id': result.id,
            'Symbol': result.symbol,
            'Description': result.description,
            'CompanyId': result.company_id
        } for result in query_result]
        return currencies_list

    def where_company_is(self, company_id: int):
        '''Filter the currencies by company.

        Parameters
        ----------
        company_id {int} -- Company Id.
        '''
        self.currency_queryable = self.currency_queryable.filter_by(
            company_id=company_id
        )
        return self
