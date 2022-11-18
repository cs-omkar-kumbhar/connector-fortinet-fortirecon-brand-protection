from .make_rest_api_call import MakeRestApiCall


def get_alert_details_by_id(config: dict, params: dict) -> dict:
    org_id = params.pop("org_id")
    alert_id = params.pop("id")
    endpoint = f"/bp/{org_id}/alerts/{alert_id}"  # edit endpoint
    method = "GET"  # GET/POST/PUT/DELETE

    MK = MakeRestApiCall(config=config)
    response = MK.make_request(endpoint=endpoint, method=method, params=params)
    return response
