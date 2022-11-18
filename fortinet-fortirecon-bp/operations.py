"""
This file will be auto-generated on each "new operation action", so avoid editing in this file.
"""


from .search_alerts import search_alerts
from .get_alert_details_by_id import get_alert_details_by_id
from .get_phishing_campaigns import get_phishing_campaigns
from .get_rogue_apps import get_rogue_apps
from .get_takedown_requests import get_takedown_requests
from .get_typo_domains import get_typo_domains


operations = {
    "search_alerts": search_alerts,
    "get_alert_details_by_id": get_alert_details_by_id,
    "get_phishing_campaigns": get_phishing_campaigns,
    "get_rogue_apps": get_rogue_apps,
    "get_takedown_requests": get_takedown_requests,
    "get_typo_domains": get_typo_domains,
}
