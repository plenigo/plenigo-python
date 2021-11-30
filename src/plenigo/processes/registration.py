from plenigo.client.http_client import HTTPClient
from plenigo.processes.environment import Environment


class Registration:
    """
    Contains registration process logic.
    """

    @staticmethod
    def start_registration(http_client: HTTPClient, registration_data: dict) -> any:
        """
        This function starts the registration process for a new customer. If address data will be provided a new invoice address will be created -
        country is mandatory for an address. If only the first and the last name are provided the first and last name of the customer will be filled.
        :param http_client: http client to use
        :param registration_data: registration data to use
        :return: request result
        """
        return http_client.post(url="processes/registration/start", data=registration_data)

    @staticmethod
    def validate_registration_token(http_client: HTTPClient, verification_token: str, token: str, env: Environment = None) -> any:
        """
        This function finishes the registration process by providing a token.
        :param http_client: http client to use
        :param verification_token: verification token
        :param token: process token
        :param env: environment data of the customer logging in
        :return: request result
        """
        data = {"verificationToken": verification_token, "token": token}
        if env:
            data.update(env.get_as_params())
        return http_client.post(url="processes/registration/validate", data=data)

    @staticmethod
    def resend_verification_token(http_client: HTTPClient, token: str, env: Environment = None) -> any:
        """
        This function resend the registration process token.
        :param http_client: http client to use
        :param token: process token
        :param env: environment data of the customer logging in
        :return: request result
        """
        data = {"token": token}
        if env:
            data.update(env.get_as_params())
        return http_client.post(url="processes/registration/resendToken", data=data)

    @staticmethod
    def start_registration_identifier(http_client: HTTPClient, registration_data: dict) -> any:
        """
        This functionality starts the registration process for a existing customer with registration identifier.
        :param http_client: http client to use
        :param registration_data: registration data to use
        :return: request result
        """
        return http_client.post(url="processes/registration/start", data=registration_data)

    @staticmethod
    def validate_registration_token_identifier(http_client: HTTPClient, verification_token: str, token: str, env: Environment = None) -> any:
        """
        TThis function finishes the registration process with registration identifier by providing a token.
        :param http_client: http client to use
        :param verification_token: verification token
        :param token: process token
        :param env: environment data of the customer logging in
        :return: request result
        """
        data = {"verificationToken": verification_token, "token": token}
        if env:
            data.update(env.get_as_params())
        return http_client.post(url="processes/registration/validate", data=data)

    @staticmethod
    def resend_verification_token_identifier(http_client: HTTPClient, token: str, env: Environment = None) -> any:
        """
        This function resend the registration process registration identifier token.
        :param http_client: http client to use
        :param token: process token
        :param env: environment data of the customer logging in
        :return: request result
        """
        data = {"token": token}
        if env:
            data.update(env.get_as_params())
        return http_client.post(url="processes/registration/resendToken", data=data)