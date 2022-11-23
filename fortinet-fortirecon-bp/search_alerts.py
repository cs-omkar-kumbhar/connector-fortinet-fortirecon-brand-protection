from .make_rest_api_call import MakeRestApiCall
from .utils_functions import handle_date


def search_alerts(config: dict, params: dict) -> dict:
    org_id = params.pop("org_id")
    endpoint = f"/bp/{org_id}/alerts"  # edit endpoint
    method = "GET"  # GET/POST/PUT/DELETE
    # write your code here, if needed.
    if params.get("start_date"):
        params["start_date"] = handle_date(params.get("start_date"))
    if params.get("end_date"):
        params["end_date"] = handle_date(params.get("end_date"))

    MK = MakeRestApiCall(config=config)
    response = MK.make_request(endpoint=endpoint, method=method, params=params)
    return response
