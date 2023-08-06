from requests import RequestException, Response

class CardNotReadyError(Exception):
    pass

class CardError(Exception):
    pass

def raise_request_exception_from_res(res: Response):
    raise RequestException(
        request=res.request,
        response=res
    )