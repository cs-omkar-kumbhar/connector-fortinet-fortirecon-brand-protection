from .make_rest_api_call import MakeRestApiCall
from .handle_date import handle_date


def get_typo_domains(config: dict, params: dict) -> dict:
    org_id = params.pop("org_id")
    endpoint = f"/bp/{org_id}/typo_domains"  # edit endpoint
    method = "GET"  # GET/POST/PUT/DELETE
    # write your code here, if needed.
    if params.get("id"):
        endpoint += "/" + params.pop("id")
    if params.get("start_date"):
        params["start_date"] = handle_date(params.get("start_date"))
    if params.get("end_date"):
        params["end_date"] = handle_date(params.get("end_date"))

    MK = MakeRestApiCall(config=config)
    response = MK.make_request(endpoint=endpoint, method=method, params=params)
    return response
