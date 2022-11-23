from .make_rest_api_call import MakeRestApiCall


def get_takedown_requests(config: dict, params: dict) -> dict:
    org_id = params.pop("org_id")
    endpoint = f"/bp/{org_id}/takedowns"  # edit endpoint
    method = "GET"  # GET/POST/PUT/DELETE

    MK = MakeRestApiCall(config=config)
    response = MK.make_request(endpoint=endpoint, method=method, params=params)
    return response