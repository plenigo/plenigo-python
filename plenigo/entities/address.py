from collections import OrderedDict
from datetime import datetime

from plenigo.client.http_client import HTTPClient, Sorting
from plenigo.resources.deletable_resource import APIDeletableResource


class Address(APIDeletableResource):
    """
    Represents an address.
    """

    def __init__(self, http_client: HTTPClient, data: OrderedDict):
        super(Address, self).__init__(http_client, data)

    def get_id(self) -> any:
        if self._data is not None and "addressId" in self._data:
            return self._data["addressId"]
        return ""

    @staticmethod
    def _get_entity_url_part() -> str:
        return "addresses"

    @staticmethod
    def _create_instance(http_client: HTTPClient, data: OrderedDict) -> any:
        return Address(http_client, data)
