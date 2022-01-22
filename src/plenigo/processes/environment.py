class Environment:
    """
    Represents a customers browser environment
    """

    def __init__(self, os: str = None, browser: str = None, source: str = None, source_url: str = None, ip_address: str = None, country: str = None):
        self.__os = os
        self.__browser = browser
        self.__source = source
        self.__source_url = source_url
        self.__ip_address = ip_address
        self.__country = country

    def get_as_params(self) -> dict:
        """
        Returns env values as params.
        :return: env values
        """
        params = {}
        if self.__os:
            params["os"] = self.__os
        if self.__browser:
            params["browser"] = self.__browser
        if self.__source:
            params["source"] = self.__source
        if self.__source_url:
            params["source_url"] = self.__source_url
        if self.__ip_address:
            params["ip_address"] = self.__ip_address
        if self.__country:
            params["country"] = self.__country
        return params
