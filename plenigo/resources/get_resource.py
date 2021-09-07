import abc

from plenigo.client.http_client import HTTPClient
from plenigo.resources.resource import APIResource


class APIGetResource(APIResource, abc.ABC):
    """
    Represents an API entity that can be retrieved.
    """

    @staticmethod
    def get(http_client: HTTPClient, entity_id: any) -> any:
        """
        Retrieves the entity that is identified by the id
        :param http_client: http client to use
        :param entity_id: id of the entity
        :return: retrieved instance
        """
        data = http_client.get("%s/%s" % (APIResource._get_entity_url_part(), entity_id))
        return APIResource._create_instance(http_client, data)
