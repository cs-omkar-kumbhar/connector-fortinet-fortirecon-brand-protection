from .make_rest_api_call import MakeRestApiCall


def get_rogue_app_by_id(config: dict, params: dict) -> dict:

    endpoint = "/bp/{0}/rogue_apps/{1}".format(params.pop("org_id"),params.pop("id"))  # edit endpoint
    method = "GET"  # GET/POST/PUT/DELETE
    # write your code here, if needed.

    MK = MakeRestApiCall(config=config)
    response = MK.make_request(endpoint=endpoint, method=method, params=params)
    return response
