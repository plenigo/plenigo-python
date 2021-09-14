import abc
from collections import OrderedDict

from plenigo.client.http_client import HTTPClient


class APIResource(abc.ABC):
    """
    Represents an API entity.
    """

    _http_client: HTTPClient
    _data: OrderedDict

    def __init__(self, http_client: HTTPClient, data: OrderedDict):
        self._http_client = http_client
        self._data = data

    @abc.abstractmethod
    def get_id(self) -> any:
        """
        Returns the main id of an entity that is used for API calls.
        :return: id
        """
        return ""

    @staticmethod
    @abc.abstractmethod
    def _get_entity_url_part() -> str:
        """
        Returns the base url part for the concrete entity.
        :return: entity url part
        """
        return ""

    @staticmethod
    @abc.abstractmethod
    def _create_instance(http_client: HTTPClient, data: OrderedDict) -> any:
        """
        Creates a concrete instance of the current entity.
        :param http_client: http client to use
        :param data: content for the entity
        :return: concrete instance
        """
        return None

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

    def __setitem__(self, key, value):
        self._data[key] = value
        return None

    def __getitem__(self, key):
        try:
            return self._data[key]
        except KeyError as err:
            raise AttributeError(*err.args)

    def __iter__(self):
        return self._data

    def __repr__(self):
        return self._data.__repr__()

    def __str__(self):
        return self._data.__str__()
