'''Subscription queryable.
'''
from ..models.subscription import Subscription


class SubscriptionQueryable:
    '''Subscription queryable.
    '''
    def __init__(self):
        '''Constructor.
        '''
        self.subscription_queryable = Subscription.query

    def to_list(self):
        '''List subscriptions.
        '''
        query_result = self.subscription_queryable.all()
        subscriptions_list = [{
            'Id': result.id,
            'Started': result.started,
            'Ended': result.ended,
            'CompanyId': result.company_id
        } for result in query_result]
        return subscriptions_list

    def where_company_is(self, company_id: int):
        '''Filter subscriptions by company.

        Parameters
        ----------
        company_id {int} -- Company Id.
        '''
        self.subscription_queryable = self.subscription_queryable.filter_by(
            company_id=company_id
        )
        return self
