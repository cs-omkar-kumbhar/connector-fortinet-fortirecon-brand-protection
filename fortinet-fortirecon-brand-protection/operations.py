""" Copyright start
  Copyright (C) 2008 - 2021 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """

from datetime import datetime
import requests
from connectors.core.connector import get_logger, ConnectorError

logger = get_logger("fortinet-fortirecon-brand-protection")


class MakeRestApiCall:

    def __init__(self, config):
        self.server_url = config.get('server_url', '').strip().strip('/')
        if not self.server_url.startswith('http') or not self.server_url.startswith('https'):
            self.server_url = 'https://' + self.server_url
        self.org_id = config.get("org_id")
        self.authkey = config.get("api_key", '')
        self.verify_ssl = config.get("verify_ssl", True)

    def make_request(self, endpoint='', params=None, data=None, method='GET', headers=None, url=None, json_data=None):
        try:
            if url is None:
                url = self.server_url + endpoint.format(org_id=self.org_id)

            headers = {"Content-Type": "application/json",
                       "Authorization": self.authkey}
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
                raise ConnectorError('{0}:{1}'.format(response.status_code, response.text))
        except requests.exceptions.SSLError as e:
            logger.exception('{0}'.format(e))
            raise ConnectorError('{0}'.format(e))
        except requests.exceptions.ConnectionError as e:
            logger.exception('{0}'.format(e))
            raise ConnectorError('{0}'.format(e))
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


def search_alerts(config: dict, params: dict) -> dict:
    # deprecated action
    MK = MakeRestApiCall(config=config)
    endpoint = "/bp/{org_id}/alerts"
    method = "GET"
    if params.get("start_date"):
        params["start_date"] = handle_date(params.get("start_date"))
    if params.get("end_date"):
        params["end_date"] = handle_date(params.get("end_date"))
    multiselect = ["source_category", "report_type", "source_reliability", "information_reliability"]
    payload = build_payload(params, multiselect)
    response = MK.make_request(endpoint=endpoint, method=method, params=payload)
    return response


def get_alert_details_by_id(config: dict, params: dict) -> dict:
    # deprecated action
    MK = MakeRestApiCall(config=config)
    alert_id = params.pop("id")
    endpoint = "/bp/{org_id}/alerts/"+"{0}".format(alert_id)
    method = "GET"
    response = MK.make_request(endpoint=endpoint, method=method, params=params)
    return response


def get_phishing_campaigns(config: dict, params: dict) -> dict:
    # deprecated action
    MK = MakeRestApiCall(config=config)
    endpoint = "/bp/{org_id}/phishing_campaigns"
    method = "GET"
    response = MK.make_request(endpoint=endpoint, method=method, params=params)
    return response


def get_phishing_campaigns_by_id(config: dict, params: dict) -> dict:
    # deprecated action
    MK = MakeRestApiCall(config=config)
    endpoint = "/bp/{org_id}/phishing_campaigns"+"/{0}".format(params.pop("id"))
    method = "GET"
    response = MK.make_request(endpoint=endpoint, method=method, params=params)
    return response


def get_rogue_app_by_id(config: dict, params: dict) -> dict:
    MK = MakeRestApiCall(config=config)
    endpoint = "/bp/{org_id}/rogue_apps" + "/{0}".format(params.get("id"))
    method = "GET"
    response = MK.make_request(endpoint=endpoint, method=method, params={})
    return response


def get_rogue_apps(config: dict, params: dict) -> dict:
    MK = MakeRestApiCall(config=config)
    endpoint = "/bp/{org_id}/rogue_apps"
    method = "GET"
    payload = build_payload(params=params, multiselect=["status"])
    response = MK.make_request(endpoint=endpoint, method=method, params=payload)
    return response


def get_takedown_requests(config: dict, params: dict) -> dict:
    MK = MakeRestApiCall(config=config)
    endpoint = "/bp/{org_id}/takedowns"
    method = "GET"
    if params.get("start_date"):
        params["start_date"] = handle_date(params.get("start_date"))
    if params.get("end_date"):
        params["end_date"] = handle_date(params.get("end_date"))
    multiselect = ["status", "category"]
    payload = build_payload(params=params, multiselect=multiselect)
    response = MK.make_request(endpoint=endpoint, method=method, params=payload)
    return response


def get_typo_domain_by_id(config: dict, params: dict) -> dict:
    # deprecated action
    MK = MakeRestApiCall(config=config)
    endpoint = "/bp/{org_id}/typo_domains"+"/{0}".format(params.pop("id"))
    method = "GET"
    response = MK.make_request(endpoint=endpoint, method=method, params=params)
    return response


def get_typo_domains(config: dict, params: dict) -> dict:
    # deprecated action
    MK = MakeRestApiCall(config=config)
    endpoint = "/bp/{org_id}/typo_domains"
    method = "GET"
    if params.get("start_date"):
        params["start_date"] = handle_date(params.get("start_date"))
    if params.get("end_date"):
        params["end_date"] = handle_date(params.get("end_date"))
    multiselect = ["status"]
    payload = build_payload(params=params, multiselect=multiselect)
    response = MK.make_request(endpoint=endpoint, method=method, params=payload)
    return response


def handle_date(str_date):
    return datetime.strptime(str_date, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d")


def build_payload(params={}, multiselect=[]):
    for k in multiselect:
        v = params.get(k)
        if v is not None:
            params[k] = ",".join(v)
    return params


operations = {
    "get_rogue_apps": get_rogue_apps,
    "get_takedown_requests": get_takedown_requests,
    "get_rogue_app_by_id": get_rogue_app_by_id
}
