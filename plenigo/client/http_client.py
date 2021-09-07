import abc
import json
import random
import time
from collections import OrderedDict
from enum import Enum
from typing import Dict, Optional
from urllib import parse

import requests

from plenigo import util
from plenigo.error import PlenigoError
from plenigo.util import LogLevel


class HTTPClient(abc.ABC):
    """
    Base class for plenigo HTTP client.
    """
    MAX_DELAY = 2
    INITIAL_DELAY = 0.5
    MAX_RETRY_AFTER = 60

    def __init__(self, timeout: int = 80, retry_attempts: int = 0, http_proxy: Optional[str] = None):
        if timeout < 10:
            raise ValueError("Timeout must be 10 or higher.")
        self._timeout = timeout
        if retry_attempts < 0 or retry_attempts > 3:
            raise ValueError("Retry attempts must be between 0 and 3.")
        self._retry_attempts = retry_attempts
        if http_proxy and (not isinstance(http_proxy, str) or not http_proxy.startswith("https://")):
            raise ValueError("Proxy must be specified as a string and must be a a SSL proxy.")
        self._http_proxy = http_proxy

    @abc.abstractmethod
    def _add_authorization_header(self, headers: Dict[str, str]) -> Dict[str, str]:
        """
        Adds authorization headers.
        :param headers: existing headers
        :return: enhanced headers
        """
        return headers

    @abc.abstractmethod
    def _get_base_url(self) -> str:
        """
        Get base URL.
        :return: base URL
        """
        return ""

    def delete(self, url: str, headers: Dict[str, str] = None, params: Dict = None) -> any:
        """
        Sends a HTTP DELETE request.
        :param url: url to call
        :param headers: headers to send
        :param params: params to add
        :return: result
        """
        return self._request("DELETE", url, headers, params)

    def get(self, url: str, headers: Dict[str, str] = None, params: Dict = None) -> any:
        """
        Sends a HTTP GET request.
        :param url: url to call
        :param headers: headers to send
        :param params: params to add
        :return: result
        """
        return self._request("GET", url, headers, params)

    def post(self, url: str, headers: Dict[str, str] = None, params: Dict = None, data: Dict = None) -> any:
        """
        Sends a HTTP POST request.
        :param url: url to call
        :param headers: headers to send
        :param params: params to add
        :param data: body data
        :return: result
        """
        return self._request("POST", url, headers, params, data)

    def put(self, url: str, headers: Dict[str, str] = None, params: Dict = None, data: Dict = None) -> any:
        """
        Sends a HTTP PUT request.
        :param url: url to call
        :param headers: headers to send
        :param params: params to add
        :param data: body data
        :return: result
        """
        return self._request("PUT", url, headers, params, data)

    def _request(self, method: str, url: str, headers: Dict[str, str] = None, params: Dict = None, data: Optional[Dict] = None) -> any:
        """
        Sends a HTTP request.
        :param method: HTTP method to use
        :param url: url to call
        :param headers: headers to send
        :param params: params to add
        :param data: body data
        :return: result
        """
        url = parse.urljoin(self._get_base_url(), url)
        status_code = 0
        num_retries = 0

        while True:
            try:
                headers = self._add_authorization_header(headers)
                result = requests.request(method, url, headers=headers, json=data, timeout=self._timeout, params=params)
                content = result.content
                status_code = result.status_code
                connection_error = None
                if status_code >= 400:
                    error_data = json.loads(content.decode("utf-8"), object_pairs_hook=OrderedDict)
                    raise PlenigoError(status_code, error_code=error_data["errorCode"], error_message=error_data["errorMessage"])
            except PlenigoError as error:
                raise error
            except Exception as ex:
                connection_error = ex
                content = None

            if status_code in [502, 504] and num_retries < self._retry_attempts:
                if connection_error:
                    util.log_message(LogLevel.INFO, "Encountered a retryable error %s." % connection_error)
                num_retries += 1
                sleep_time = self.__sleep_time_seconds(num_retries)
                util.log_message(LogLevel.INFO, "Initiating retry %i for request %s %s after sleeping %.2f seconds." % (num_retries, method, url, sleep_time))
                time.sleep(sleep_time)
            else:
                if content is not None:
                    return json.loads(content.decode("utf-8"), object_pairs_hook=OrderedDict)
                else:
                    raise connection_error

    @staticmethod
    def __sleep_time_seconds(num_retries: int):
        """
        Calculates time to wait in seconds before the next try.
        :param num_retries: number of retries
        :return: seconds to wait
        """
        # Apply exponential backoff with initial_network_retry_delay on the
        # number of num_retries so far as inputs.
        # Do not allow the number to exceed max_network_retry_delay.
        sleep_seconds = min(HTTPClient.INITIAL_DELAY * (2 ** (num_retries - 1)), HTTPClient.MAX_DELAY)

        sleep_seconds = sleep_seconds * 0.5 * (1 + random.uniform(0, 1))
        # But never sleep less than the base sleep seconds.
        sleep_seconds = max(HTTPClient.INITIAL_DELAY, sleep_seconds)
        return sleep_seconds


class PlenigoApiType(Enum):
    STAGE = "https://api.plenigo-stage.com/api/v3.0/"
    LIVE = "https://api.plenigo.com/api/v3.0/"


class Sorting(Enum):
    ASC = "ASC"
    DESC = "DESC"


class PlenigoHTTPClient(HTTPClient):
    """
    The plenigo public API HTTP client.
    """
    def __init__(self, api_type: PlenigoApiType, api_key: str, timeout: int = 80, retry_attempts: int = 0, http_proxy: Optional[str] = None):
        super(PlenigoHTTPClient, self).__init__(timeout, retry_attempts, http_proxy)
        if not api_key:
            raise ValueError("API key provided must not be empty.")
        self.__api_key = api_key
        if api_type not in [PlenigoApiType.LIVE, PlenigoApiType.STAGE]:
            raise ValueError("API type provided is not valid.")
        self.__api_type = api_type

    def _add_authorization_header(self, headers: Dict[str, str]) -> Dict[str, str]:
        if headers is None:
            headers = {"X-plenigo-token": self.__api_key}
        else:
            headers["X-plenigo-token"] = self.__api_key
        return headers

    def _get_base_url(self) -> str:
        return self.__api_type.value
