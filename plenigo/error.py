class PlenigoError(Exception):
    """
    Represents a plenigo error.
    """
    def __init__(self, http_status_code, error_code=None, error_message=None, validation_errors=None):
        super(PlenigoError, self).__init__(error_message)

        self._http_status_code = http_status_code
        self._error_code = error_code
        self._error_message = error_message
        self._validation_errors = validation_errors

    def __str__(self):
        return self._error_message or "<empty message>"

    def __repr__(self):
        return "%s(error_code=%r, error_message=%r, validation_errors=%r)" % (
            self.__class__.__name__,
            self._error_code,
            self._error_message,
            self._validation_errors,
        )

    def get_http_status_code(self):
        return self._http_status_code

    def get_error_code(self):
        return self._error_code

    def get_error_message(self):
        return self._error_message

    def get_validation_errors(self):
        return self._validation_errors

    def is_connection_error(self):
        return self._http_status_code == 502 or self._http_status_code == 504
