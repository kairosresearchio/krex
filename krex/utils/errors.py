class APIRequestError(Exception):
    def __init__(self, request, message, status_code=None, time=None, resp_headers=None):
        self.request = request
        self.message = message
        self.status_code = status_code if status_code is not None else "Unknown"
        self.time = time if time is not None else "Unknown"
        self.resp_headers = resp_headers
        super().__init__(f"{message} (ErrCode: {self.status_code}) (ErrTime: {self.time})" f".\nRequest → {request}.")


class FailedRequestError(APIRequestError):
    pass


class InvalidRequestError(APIRequestError):
    pass


class APIException(Exception):
    def __init__(self, response):
        self.status_code = response.status_code
        self.response = response.text

    def __str__(self):
        return "APIException(http status=%s): response=%s" % (
            self.status_code,
            self.response,
        )


class RequestException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return "RequestException: %s" % self.message


class ParamsException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return "ParamsException: %s" % self.message
