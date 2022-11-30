"""
This file will be auto-generated on each "new operation action", so avoid editing in this file.
"""
from datetime import datetime
import requests
# import time
from connectors.core.connector import get_logger, ConnectorError

# from connectors.core.utils import update_connnector_config


error_msg = {
    401: 'Authentication failed due to invalid credentials',
    429: 'Rate limit was exceeded',
    403: 'Token is invalid or expired',
    "ssl_error": 'SSL certificate validation failed',
    'time_out': 'The request timed out while trying to connect to the remote server',
}

logger = get_logger("fortinet-fortirecon-bp")


class MakeRestApiCall:

    def __init__(self, config):
        self.server_url = config.get('server_url', '').strip().strip('/')
        if not self.server_url.startswith('http') or not self.server_url.startswith('https'):
            self.server_url = 'https://' + self.server_url
        self.authkey = config.get("api_key", '')
        self.verify_ssl = config.get("verify_ssl", True)

    def make_request(self, endpoint='', params=None, data=None, method='GET', headers=None, url=None, json_data=None):
        try:
            if url is None:
                url = self.server_url + endpoint

            headers = {"Content-Type": "application/json",
                       "Authorization": self.authkey}
            # headers["Authorizaion"] = self.authkey
            response = requests.request(method=method, url=url,
                                        headers=headers, data=data, json=json_data, params=params,
                                        verify=self.verify_ssl)

            if response.ok:
                if 'json' in str(response.headers):
                    return response.json()
                else:
                    return response.text
            else:
                logger.error("Error: {0}".format(response.json()))
                raise ConnectorError('{0}'.format(error_msg.get(response.status_code, response.text)))
        except requests.exceptions.SSLError as e:
            logger.exception('{0}'.format(e))
            raise ConnectorError('{0}'.format(error_msg.get('ssl_error')))
        except requests.exceptions.ConnectionError as e:
            logger.exception('{0}'.format(e))
            raise ConnectorError('{0}'.format(error_msg.get('time_out')))
        except Exception as e:
            logger.error('{0}'.format(e))
            raise ConnectorError('{0}'.format(e))


def _check_health(config: dict) -> bool:
    try:
        endpoint = "/orgs"
        method = "GET"
        MS = MakeRestApiCall(config=config)
        MS.make_request(endpoint=endpoint, method=method)
        return True
    except Exception as e:
        raise Exception(e)


def get_alert_details_by_id(config: dict, params: dict) -> dict:
    org_id = params.pop("org_id")
    alert_id = params.pop("id")
    endpoint = f"/bp/{org_id}/alerts/{alert_id}"  # edit endpoint
    method = "GET"  # GET/POST/PUT/DELETE

    MK = MakeRestApiCall(config=config)
    response = MK.make_request(endpoint=endpoint, method=method, params=params)
    return response


def get_phishing_campaigns(config: dict, params: dict) -> dict:
    org_id = params.pop("org_id")
    endpoint = f"/bp/{org_id}/phishing_campaigns"  # edit endpoint

    method = "GET"  # GET/POST/PUT/DELETE
    # write your code here, if needed.

    MK = MakeRestApiCall(config=config)
    response = MK.make_request(endpoint=endpoint, method=method, params=params)
    return response


def get_phishing_campaigns_by_id(config: dict, params: dict) -> dict:
    endpoint = "/bp/{0}/phishing_campaigns/{1}".format(params.pop("org_id"), params.pop("id"))  # edit endpoint
    method = "GET"  # GET/POST/PUT/DELETE
    # write your code here, if needed.

    MK = MakeRestApiCall(config=config)
    response = MK.make_request(endpoint=endpoint, method=method, params=params)
    return response


def get_rogue_app_by_id(config: dict, params: dict) -> dict:
    endpoint = "/bp/{0}/rogue_apps/{1}".format(params.pop("org_id"), params.pop("id"))  # edit endpoint
    method = "GET"  # GET/POST/PUT/DELETE
    # write your code here, if needed.

    MK = MakeRestApiCall(config=config)
    response = MK.make_request(endpoint=endpoint, method=method, params=params)
    return response


def get_rogue_apps(config: dict, params: dict) -> dict:
    org_id = params.pop("org_id")
    endpoint = f"/bp/{org_id}/rogue_apps"  # edit endpoint
    method = "GET"  # GET/POST/PUT/DELETE
    # write your code here, if needed.
    MK = MakeRestApiCall(config=config)
    response = MK.make_request(endpoint=endpoint, method=method, params=params)
    return response


def get_takedown_requests(config: dict, params: dict) -> dict:
    org_id = params.pop("org_id")
    endpoint = f"/bp/{org_id}/takedowns"  # edit endpoint
    method = "GET"  # GET/POST/PUT/DELETE

    MK = MakeRestApiCall(config=config)
    response = MK.make_request(endpoint=endpoint, method=method, params=params)
    return response


def get_typo_domain_by_id(config: dict, params: dict) -> dict:
    endpoint = "/bp/{0}/typo_domains/{1}".format(params.pop("org_id"), params.pop("id"))  # edit endpoint
    method = "GET"  # GET/POST/PUT/DELETE
    # write your code here, if needed.

    MK = MakeRestApiCall(config=config)
    response = MK.make_request(endpoint=endpoint, method=method, params=params)
    return response


def get_typo_domains(config: dict, params: dict) -> dict:
    org_id = params.pop("org_id")
    endpoint = f"/bp/{org_id}/typo_domains"  # edit endpoint
    method = "GET"  # GET/POST/PUT/DELETE
    # write your code here, if needed.
    if params.get("start_date"):
        params["start_date"] = handle_date(params.get("start_date"))
    if params.get("end_date"):
        params["end_date"] = handle_date(params.get("end_date"))

    MK = MakeRestApiCall(config=config)
    response = MK.make_request(endpoint=endpoint, method=method, params=params)
    return response


def handle_date(str_date):
    return datetime.strptime(str_date, "%Y-%m-%dT%H:%M:%S.%fZ").date()


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


operations = {
    "search_alerts": search_alerts,
    "get_alert_details_by_id": get_alert_details_by_id,
    "get_phishing_campaigns": get_phishing_campaigns,
    "get_phishing_campaigns_by_id": get_phishing_campaigns_by_id,
    "get_rogue_apps": get_rogue_apps,
    "get_takedown_requests": get_takedown_requests,
    "get_typo_domains": get_typo_domains,
    "get_rogue_app_by_id": get_rogue_app_by_id,
    "get_typo_domain_by_id": get_typo_domain_by_id,
}
