from plenigo.client.http_client import HTTPClient
from plenigo.processes.environment import Environment


class PasswordForgotten:
    """
    Contains password forgotten process logic.
    """

    @staticmethod
    def send_token_with_username(http_client: HTTPClient, username: str, language: str, verification_url: str = None, env: Environment = None) -> any:
        """
        This function sends the password forgotten token to reset password.
        :param http_client: http client to use
        :param username: username provided
        :param language: language of the customer
        :param verification_url: url to verify registration - if provided two parameters are added to the url (token and step) and it is passed to the
        registration mail. This way the application that embeds the plenigo registration from can handle a user verification via link instead of a
        token process.
        :param env: environment data of the customer logging in
        :return: request result
        """
        data = {"username": username, "language": language}
        if verification_url:
            data["verificationUrl"] = verification_url
        if env:
            data.update(env.get_as_params())
        return http_client.post(url="processes/passwordForgotten/sendToken", data=data)

    @staticmethod
    def send_token_with_email(http_client: HTTPClient, email: str, language: str, verification_url: str = None, env: Environment = None) -> any:
        """
        This function sends the password forgotten token to reset password.
        :param http_client: http client to use
        :param email: email address provided
        :param language: language of the customer
        :param verification_url: url to verify registration - if provided two parameters are added to the url (token and step) and it is passed to the
        registration mail. This way the application that embeds the plenigo registration from can handle a user verification via link instead of a
        token process.
        :param env: environment data of the customer logging in
        :return: request result
        """
        data = {"email": email, "language": language}
        if verification_url:
            data["verificationUrl"] = verification_url
        if env:
            data.update(env.get_as_params())
        return http_client.post(url="processes/passwordForgotten/sendToken", data=data)

    @staticmethod
    def resend_token(http_client: HTTPClient, token: str, env: Environment = None) -> any:
        """
        This function resend the password forgotten token to reset password.
        :param http_client: http client to use
        :param token: process token
        :param env: environment data of the customer logging in
        :return: request result
        """
        data = {"token": token}
        if env:
            data.update(env.get_as_params())
        return http_client.post(url="processes/passwordForgotten/resendToken", data=data)

    @staticmethod
    def token_verification(http_client: HTTPClient, verification_token: str, token: str, env: Environment = None) -> any:
        """
        This function validates the two factor token of a customer.
        :param http_client: http client to use
        :param verification_token: verification token
        :param token: process token
        :param env: environment data of the customer logging in
        :return: request result
        """
        data = {"verificationToken": verification_token, "token": token}
        if env:
            data.update(env.get_as_params())
        return http_client.post(url="processes/passwordForgotten/verifyToken", data=data)

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
        return http_client.post(url="processes/passwordForgotten/resetPassword", data=data)

    @staticmethod
    def verify_two_factor(http_client: HTTPClient, two_factor_token: str, token: str, env: Environment = None) -> any:
        """
        This function verifies the two factor of the customer.
        :param http_client: http client to use
        :param two_factor_token: two factor token
        :param token: process token
        :param env: environment data of the customer logging in
        :return: request result
        """
        data = {"twoFactorToken": two_factor_token, "token": token}
        if env:
            data.update(env.get_as_params())
        return http_client.post(url="processes/passwordForgotten/verifyTwoFactor", data=data)

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
        return http_client.put(url="passwordForgotten/changeSessions/%s" % removal_token, params={"sessionId": session_id})


