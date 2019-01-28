"""Client queryable.
"""
from app.models.client import Client


class ClientQueryable:
    """Client queryable.
    """

    def __init__(self):
        """Constructor.
        """
        self.client_queryable = Client.query

    def to_list(self):
        """Get list of clients.
        """
        query_result = self.client_queryable.all()
        clients_list = [{
            'Id': result.id,
            'Name': result.name,
            'NameStub': result.name_stub,
            'Address': result.address,
            'CompanyId': result.company_id
        } for result in query_result]
        return clients_list
