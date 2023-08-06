class CerebrateError(Exception):
    def __init__(
        self,
        message=None,
        status=None,
        code=None,
    ):
        super(CerebrateError, self).__init__(message)

        self._message = message
        self._status = status
        self._code = code

    def __str__(self):
        message = self._message or "<empty message>"
        code = self._code or 500
        status = self._status or "Server Error"
        return f"{code} {status}: {message}"

    def __repr__(self):
        return "%s(code=%r, status=%r, message=%r)" % (
            self.__class__.__name__,
            self._code,
            self._status,
            self._message,
        )

    @property
    def message(self):
        return self._message

    @property
    def status(self):
        return self._status

    @property
    def code(self):
        return self._code


class ServerError(CerebrateError):
    pass


class ArgumentValidationError(CerebrateError):
    pass


class AuthenticationError(CerebrateError):
    pass
