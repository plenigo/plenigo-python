from collections import OrderedDict
from datetime import datetime

from plenigo.client.http_client import HTTPClient, Sorting
from plenigo.resources.resource import APIResource
from plenigo.resources.searchable_resource import APISearchableResource


class Activity(APIResource):
    """
    Represents an activity.
    """

    def __init__(self, http_client: HTTPClient, data: OrderedDict):
        super(Activity, self).__init__(http_client, data)

    def get_id(self) -> any:
        return ""

    @staticmethod
    def _get_entity_url_part() -> str:
        return "activities"

    @staticmethod
    def _create_instance(http_client: HTTPClient, data: OrderedDict) -> any:
        return Activity(http_client, data)

    @staticmethod
    def search(http_client: HTTPClient, customer_id: str, size: int = 100, starting_after: datetime = None, sort: Sorting = Sorting.ASC,
               start_time: datetime = None, end_time: datetime = None, json_object_type: str = None, json_object_identifier: str = None) -> any:
        """
        Retrieve all activities for a customer.
        :param http_client: http client to use
        :param customer_id: customer to get activites for
        :param size: amount of elements to return
        :param starting_after: last element for pagination
        :param sort: sorting order
        :param start_time: start time
        :param end_time: end time
        :param json_object_type: type the activity belongs to
        :param json_object_identifier: identifier of the object the activity belongs to. Can only be used in combination with jsonObjectType
        :return: list of elements
        """
        params = APISearchableResource.create_search_params(size, starting_after, sort, start_time, end_time)
        if json_object_type:
            params["jsonObjectType"] = json_object_type
        if json_object_identifier:
            params["jsonObjectIdentifier"] = json_object_identifier
        result = http_client.get(url="%s/%s" % (APIResource._get_entity_url_part(), customer_id), params=params)
        if "items" in result:
            return [APIResource._create_instance(http_client, data) for data in result["items"]]
        return []
