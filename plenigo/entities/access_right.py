from collections import OrderedDict

from plenigo.client.http_client import HTTPClient
from plenigo.resources.resource import APIResource


class AccessRight(APIResource):
    """
    Represents an access right.
    """
    def __init__(self, http_client: HTTPClient, data: OrderedDict):
        super(AccessRight, self).__init__(http_client, data)

    def get_id(self) -> any:
        if self._data is not None and "customerId" in self._data:
            return self._data["customerId"]
        return ""

    @staticmethod
    def _get_entity_url_part() -> str:
        return "accessRights"

    @staticmethod
    def _create_instance(http_client: HTTPClient, data: OrderedDict) -> any:
        return AccessRight(http_client, data)

    @staticmethod
    def get(http_client: HTTPClient, entity_id: any) -> any:
        """
        Retrieves the entity that is identified by the id
        :param http_client: http client to use
        :param entity_id: id of the entity
        :return: retrieved instance
        """
        data = http_client.get("%s/%s" % (AccessRight._get_entity_url_part(), entity_id))
        return AccessRight._create_instance(http_client, data)

    @staticmethod
    def check_access(http_client: HTTPClient, customer_id: str, access_right_unique_ids: []) -> any:
        """
        Check if customer has a valid access right for one or multiple access rights identified by the provided access right unique ids.
        :param http_client: http client to use
        :param customer_id: unique id of the customer
        :param access_right_unique_ids: comma separated ids of access right unique ids
        :return: detailed information about the allowed accesses of a customer
        """
        return http_client.get(url="accessRights/%s/hasAccess" % customer_id, params={"accessRightUniqueIds": ",".join(access_right_unique_ids)})

    @staticmethod
    def get_all(http_client: HTTPClient, customer_id: str) -> any:
        """
        Get all access rights for a customer identified by the passed customer id.
        :param http_client: http client to use
        :param customer_id: unique id of the customer
        :return: all access rights of a customer
        """
        return http_client.get(url="accessRights/%s" % customer_id)

    @staticmethod
    def create(http_client: HTTPClient, data: dict) -> any:
        """
        Creates a new instance with the given data.
        :param http_client: http client to use
        :param data: instance data
        :return: instance created
        """
        data = http_client.post("%s/%s" % (AccessRight._get_entity_url_part(), data["customerId"]), data=data)
        return AccessRight._create_instance(http_client, data)

    def update(self, access_right_unique_id: str, data: dict) -> any:
        """
        Saves the current instance.
        :param access_right_unique_id: unique id of the access right to update
        :param data: access right data
        :return: updated instance
        """
        if self._http_client is None:
            raise ValueError("Instance must be a managed instance.")
        self._data = self._http_client.put(url="%s/%s/%s" % (APIResource._get_entity_url_part(), self.get_id(), access_right_unique_id), data=data)
        return self

    def delete(self, access_right_unique_id: str) -> None:
        """
        Deletes a specific access right.
          :param access_right_unique_id: unique id of the access right to delete
        """
        self._http_client.delete("%s/%s/%s" % (APIResource._get_entity_url_part(), self.get_id(), access_right_unique_id))
