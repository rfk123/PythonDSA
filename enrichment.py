import logging
import os
import time
import requests

DATACO_BASE_URL = os.getenv(
    "DATACO_BASE_URL",
    "https://api.example.com"
)
logger = logging.getLogger(__name__)

# Create labels for different errors so my prgram can distinguish between them


class DataCoError(Exception):
    pass


class DataCoAuthError(DataCoError):
    pass


class DataCoRateLimitError(DataCoError):
    pass


class DataCoNotFoundError(DataCoError):
    pass


def enrich_company(domain):

    if not domain or not isinstance(domain, str):
        raise ValueError("Function requires domain to be a non-empty string")

    params = {
        "domain": domain,
    }

    headers = {
        "Authentication": f"Bearer {os.environ['DATACO_API_KEY']}",
        "Accept": "application/json"
    }

    max_attempts = 3
    for attempt in max_attempts:
        try:
            # Do something that might fail
            response = requests.get(
                DATACO_BASE_URL,
                headers=headers,
                params=params,
                timeout=10
            )
            # put the more specific exceptions first
        except requests.exceptions.Timeout:
            # Handle the specific failure (if the failure is a timeout)
            if attempt == max_attempts - 1:
                raise DataCoError("DataCo request timed out")
            delay = 2 * attempt
            time.sleep(delay)
            continue
        except requests.exceptions.RequestException:
            # Handle the specific failure (if some other request related failure happens)
            raise DataCoError("DataCo request failed")

        status_code = response.status_code

        if status_code == 200:
            required_fields = [
                "name",
                "employee_count",
                "industry",
                "location"
            ]
            try:
                data = response.json()
            except requests.exceptions.JSONDecodeError:
                raise DataCoError("DataCo returned invalid JSON")
            for field in required_fields:
                if field not in data:
                    raise DataCoError(f"CataCo response missing field {field}")

            if not isinstance(data["name"], str):
                raise DataCoError("Invalid name")

            if data["employee_count"] is not None and not isinstance(data["employee_count"], int):
                raise DataCoError("Invalid employee count")

            return data
        elif status_code in (403, 401):
            raise DataCoAuthError(
                "DataCo authentication or authorization failed")
        elif status_code == 404:
            raise DataCoNotFoundError("Company not found")
        elif status_code == 429:
            if attempt == max_attempts - 1:
                raise DataCoRateLimitError("DataCo rate limit exceeded")
            delay = 2 * attempt
            time.sleep(delay)
            continue
        elif 500 <= status_code <= 599:
            if attempt == max_attempts - 1:
                raise DataCoError("DataCo server error")
            delay = 2 * attempt
            time.sleep(delay)
            continue
        else:
            raise DataCoError("Unexpected DataCo status code")


def transform_for_crm(enrichment_data):
    crm_data = {}

    if enrichment_data["name"] is not None:
        crm_data["company_name"] = enrichment_data["name"]

    if enrichment_data["employee_count"] is not None:
        crm_data["number_of_employees"] = enrichment_data["employee_count"]

    if enrichment_data["industry"] is not None:
        crm_data["company_industry"] = enrichment_data["industry"]

    if enrichment_data["location"] is not None:
        crm_data["company_location"] = enrichment_data["location"]

    return crm_data
