import abc
import datetime
from typing import Callable

from plenigo.client.http_client import HTTPClient, Sorting
from plenigo.resources.resource import APIResource


class APISearchableResource(APIResource, abc.ABC):
    """
    Represents an API entity that can be searched.
    """

    @staticmethod
    def search(http_client: HTTPClient, size: int = 100, starting_after: datetime = None, sort: Sorting = Sorting.ASC,
               start_time: datetime = None, end_time: datetime = None, add_additional_params: Callable = None) -> any:
        """
        Retrieve all elements that are found regarding the search parameters.
        :param http_client: http client to use
        :param size: amount of elements to return
        :param starting_after: last element for pagination
        :param sort: sorting order
        :param start_time: start time
        :param end_time: end time
        :param add_additional_params: function for adding additional params 
        :return: list of elements
        """
        params = APISearchableResource._create_search_params(size, starting_after, sort, start_time, end_time)
        params = add_additional_params(params)
        result = http_client.get(url=APISearchableResource._get_entity_url_part(), params=params)
        if "items" in result:
            return [APISearchableResource._create_instance(http_client, data) for data in result["items"]]
        return []
