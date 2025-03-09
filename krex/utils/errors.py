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
