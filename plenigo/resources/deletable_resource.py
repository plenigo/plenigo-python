import abc

from plenigo.resources.resource import APIResource

from plenigo.resources.updatable_resource import APIUpdatableResource


class APIDeletableResource(APIUpdatableResource, abc.ABC):
    """
    Represents an API entity that can be deleted.
    """

    def delete(self) -> None:
        """
        Deletes the current instance.
        """
        self._http_client.delete("%s/%s" % (self._get_entity_url_part(), self.get_id()))
