import logging

import requests

OUTAGE_URL = "https://api.krakenflex.systems/interview-tests-mock-api/v1/outages"
SITE_INFO_URL = "https://api.krakenflex.systems/interview-tests-mock-api/v1/site-info"
SITE_OUTAGES_URL = (
    "https://api.krakenflex.systems/interview-tests-mock-api/v1/site-outages"
)
BEGIN_DATE = "2022-01-01T00:00:00.000Z"
SITE = "norwich-pear-tree"
API_KEY = "EltgJ5G8m44IzwE6UN2Y4B4NjPW77Zk6FJK3lL23"

logger = logging.getLogger(__name__)


def get_all_outages(api_key):
    response = requests.get(
        OUTAGE_URL, headers={"Content-Type": "application/json", "x-api-key": api_key}
    )
    return response.json()


def get_site_info(site, api_key):
    response = requests.get(
        f"{SITE_INFO_URL}/{site}",
        headers={"Content-Type": "application/json", "x-api-key": api_key},
    )
    return response.json()


def detect_site_outages(site, begin_date, api_key):
    outages = get_all_outages(api_key)
    site_info = get_site_info(site, api_key)
    site_outages = []
    for device in site_info["devices"]:
        for outage in outages:
            if outage["begin"] >= begin_date and device["id"] == outage["id"]:
                site_outage = {
                    "id": outage["id"],
                    "name": device["name"],
                    "begin": outage["begin"],
                    "end": outage["end"],
                }
                site_outages.append(site_outage)
                continue

    response = requests.post(
        f"{SITE_OUTAGES_URL}/{site}",
        headers={
            "Content-Type": "application/json",
            "x-api-key": api_key,
            "accept": "*/*",
        },
        json=site_outages,
    )
    if response.status_code == 200:
        logger.info("Site outages are posted for %s", site)


detect_site_outages(SITE, BEGIN_DATE, API_KEY)
