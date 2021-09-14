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
    def create_search_params(size: int = 100, starting_after: any = None, sort: Sorting = Sorting.ASC,
                             start_time: datetime = None, end_time: datetime = None) -> dict:
        """
        Creates params for retrieve all calls
        :param size: amount of elements to return
        :param starting_after: last element for pagination
        :param sort: sorting order
        :param start_time: start time
        :param end_time: end time
        :return: list of elements
        """
        params = {
            "size": size,
            "sort": sort
        }
        if starting_after is not None:
            params["startingAfter"] = starting_after
        if start_time is not None:
            params["startTime"] = start_time.astimezone(datetime.timezone.utc).isoformat()
        if end_time is not None:
            params["endTime"] = end_time.astimezone(datetime.timezone.utc).isoformat()
        return params

    @staticmethod
    def _search_base(http_client: HTTPClient, get_entity_url: Callable, create_instance: Callable, size: int = 100, starting_after: datetime = None,
                     sort: Sorting = Sorting.ASC, start_time: datetime = None, end_time: datetime = None, add_additional_params: Callable = None) -> any:
        """
        Retrieve all elements that are found regarding the search parameters.
        :param http_client: http client to use
        :param get_entity_url: get entity url
        :param create_instance: function to create a concrete instance
        :param size: amount of elements to return
        :param starting_after: last element for pagination
        :param sort: sorting order
        :param start_time: start time
        :param end_time: end time
        :param add_additional_params: function for adding additional params 
        :return: list of elements
        """
        params = APISearchableResource.create_search_params(size, starting_after, sort, start_time, end_time)
        params = add_additional_params(params)
        result = http_client.get(url=get_entity_url(), params=params)
        if "items" in result:
            return [create_instance(http_client, data) for data in result["items"]]
        return []

    @staticmethod
    @abc.abstractmethod
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