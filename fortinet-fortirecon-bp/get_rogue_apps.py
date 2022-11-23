from .make_rest_api_call import MakeRestApiCall


def get_rogue_apps(config: dict, params: dict) -> dict:
    org_id = params.pop("org_id")
    endpoint = f"/bp/{org_id}/rogue_apps"  # edit endpoint
    method = "GET"  # GET/POST/PUT/DELETE
    # write your code here, if needed.
    MK = MakeRestApiCall(config=config)
    response = MK.make_request(endpoint=endpoint, method=method, params=params)
    return response
