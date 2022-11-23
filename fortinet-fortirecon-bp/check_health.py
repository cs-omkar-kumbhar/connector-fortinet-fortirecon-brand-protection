from .make_rest_api_call import MakeRestApiCall


def _check_health(config: dict) -> bool:
    try:
        endpoint = ""
        method = "GET"
        MS = MakeRestApiCall(config=config)
        MS.make_request(endpoint=endpoint, method=method)
        return True
    except Exception as e:
        raise Exception(e)