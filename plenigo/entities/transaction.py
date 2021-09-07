from collections import OrderedDict

from plenigo.client.http_client import HTTPClient
from plenigo.resources.searchable_resource import APISearchableResource


class Transaction(APISearchableResource):
    """
    Represents a transactions.
    """

    def __init__(self, http_client: HTTPClient, data: OrderedDict):
        super(Transaction, self).__init__(http_client, data)

    def get_id(self) -> any:
        if self._data is not None and "transactionId" in self._data:
            return self._data["transactionId"]
        return ""

    @staticmethod
    def _get_entity_url_part() -> str:
        return "transactions"

    @staticmethod
    def _create_instance(http_client: HTTPClient, data: OrderedDict) -> any:
        return Transaction(http_client, data)
