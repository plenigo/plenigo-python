from plenigo.client.http_client import HTTPClient
from plenigo.processes.environment import Environment


class Login:
    """
    Contains login process logic.
    """

    @staticmethod
    def verify_login_with_username(http_client: HTTPClient, username: str, password: str, env: Environment = None) -> any:
        """
        This function verifies the log in data of a customer and executes the log in. The caller must decide if a
        username is provided for login. If both are provided only the email address will be used.
        :param http_client: http client to use
        :param username: username provided
        :param password: password provided
        :param env: environment data of the customer logging in
        :return: request result
        """
        data = {"username": username, "password": password}
        if env:
            data.update(env.get_as_params())
        return http_client.post(url="processes/login/verify", data=data)

    @staticmethod
    def verify_login_with_email(http_client: HTTPClient, email: str, password: str, env: Environment = None) -> any:
        """
        This function verifies the log in data of a customer and executes the log in. The caller must decide if an
        email address is provided for login. If both are provided only the email address will be used.
        :param http_client: http client to use
        :param email: email address provided
        :param password: password provided
        :param env: environment data of the customer logging in
        :return: request result
        """
        data = {"email": email, "password": password}
        if env:
            data.update(env.get_as_params())
        return http_client.post(url="processes/login/verify", data=data)

    @staticmethod
    def verify_two_factor(http_client: HTTPClient, two_factor_token: str, token: str, env: Environment = None) -> any:
        """
        This function validates the two factor token of a customer.
        :param http_client: http client to use
        :param two_factor_token: two factor token
        :param token: process token
        :param env: environment data of the customer logging in
        :return: request result
        """
        data = {"twoFactorToken": two_factor_token, "token": token}
        if env:
            data.update(env.get_as_params())
        return http_client.post(url="processes/login/verifyTwoFactorAuth", data=data)

    @staticmethod
    def verify_password_reset(http_client: HTTPClient, password: str, token: str, env: Environment = None) -> any:
        """
        This function validates the password reset of a customer.
        :param http_client: http client to use
        :param password: password
        :param token: process token
        :param env: environment data of the customer logging in
        :return: request result
        """
        data = {"password": password, "token": token}
        if env:
            data.update(env.get_as_params())
        return http_client.post(url="processes/login/verifyResetPassword", data=data)

    @staticmethod
    def update_additional_data(http_client: HTTPClient, data: dict) -> any:
        """
        Add missing customer data like username, first name and last name to the customer if requested by process.
        Only data that are actively requested can be set here.
        :param http_client: http client to use
        :param data: data to send
        :return: request result
        """
        return http_client.post(url="processes/login/updateAdditionalData", data=data)

    @staticmethod
    def remove_active_session(http_client: HTTPClient, removal_token: str, session_id: str = None) -> any:
        """
        Removes one or all active sessions of a customer. If a session id is provided the specific session will be
        removed otherwise all active sessions will be removed.
        :param http_client: http client to use
        :param removal_token: removal token
        :param session_id: session id if a specific session should be removed
        :return: request result
        """
        return http_client.put(url="processes/login/changeSessions/%s" % removal_token, params={"sessionId": session_id})
