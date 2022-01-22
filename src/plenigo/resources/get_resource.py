import abc

from plenigo.client.http_client import HTTPClient
from plenigo.resources.resource import APIResource


class APIGetResource(APIResource, abc.ABC):
    """
    Represents an API entity that can be retrieved.
    """

    @staticmethod
    @abc.abstractmethod
    def get(http_client: HTTPClient, entity_id: any) -> any:
        """
        Retrieves the entity that is identified by the id
        :param http_client: http client to use
        :param entity_id: id of the entity
        :return: retrieved instance
        """
        return None
