from collections import OrderedDict
from datetime import datetime

from plenigo.client.http_client import HTTPClient, Sorting
from plenigo.resources.deletable_resource import APIDeletableResource
from plenigo.resources.searchable_resource import APISearchableResource


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

    @staticmethod
    def search(http_client: HTTPClient, size: int = 100, starting_after: datetime = None, sort: Sorting = Sorting.ASC,
               start_time: datetime = None, end_time: datetime = None, external_system_id: str = None) -> any:
        """
        Retrieve all customers for the given search parameters.
        :param http_client: http client to use
        :param size: amount of elements to return
        :param starting_after: last element for pagination
        :param sort: sorting order
        :param start_time: start time
        :param end_time: end time
        :param external_system_id: external system id
        :return: list of elements
        """
        return APISearchableResource._search_base(http_client=http_client, get_entity_url=Address._get_entity_url_part, 
                                                  create_instance=Address._create_instance, size=size, starting_after=starting_after, sort=sort, 
                                                  start_time=start_time, end_time=end_time)
