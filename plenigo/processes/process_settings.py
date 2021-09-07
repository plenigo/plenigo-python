from plenigo.client.http_client import HTTPClient


class ProcessSettings:
    """
    Contains process settings logic.
    """

    @staticmethod
    def get_process_settings(http_client: HTTPClient, language: str) -> any:
        """
        Get settings for configuring the SSO and checkout part.
        :param http_client: http client to use
        :param language: language translations should be delivered in
        :return: request result
        """
        return http_client.post(url="processes/settings", params={"language": language})
