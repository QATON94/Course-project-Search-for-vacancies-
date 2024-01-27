class APIException(Exception):
    pass


class HeadHunterAPIAvailableError(APIException):
    pass


class HeadHunterRequestAPIError(APIException):
    pass
