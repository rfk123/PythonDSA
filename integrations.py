
# Import a common library for HTTP requests called requests
import requests
import os

# api_key = "asdfm2134kjd2hb2jkd"
# We dont want to include the secret in our git repo for people to steal so we should import os
url = "http://api.example.com/companies"
api_key = os.environ("DATACO_API_KEY")
# response = requests.get()
"""
The response object gives us access to things like status code, headers, json, and text
This python program is our client sending out an HTTP request to a server (external API) who will inturn send a response back to this client
"""

params = {
    "domain": "borant.com",
    "include": "funding"
}

headers = {
    "Authorization": f"Bearer {api_key}",
    "Accept": "application/json"
}

response = requests.get(
    url,
    headers=headers,
    params=params,
    timeout=10
)
# The timeout is included to say " if the service doesnt return a response within this time frame, stop waiting and deal with the error code that we have"

# We want to ensure/validate our response before doing anything with it
if response.status_code == 200:
    data = response.json()
else:
    pass

# data = response.json()


def enrich_company(domain):
    """
    The workflow of this function is to take the domain, send an http request to DATACO, receive the data and return it.
    DataCo expects GET https://api.example.com/companies with ?domain=<domain>
    It also expects and Authorization and Accept header
    If successfull, the external api will respond with the fields: name, employee_count, industry, and location.
    """
    # Validate the input
    if not domain or not isinstance(domain, str):
        raise ValueError("domain must be a non-empty string")

    url = "https://api.example.com/companies"
    api_key = os.environ["DATACO_API_KEY"]
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/json"
    }
    params = {
        "domain": domain
    }

    response = requests.get(
        url,
        headers=headers,
        params=params,
        timeout=10
    )

    if response.status_code == 200:
        data = response.json()
    else:
        return None

    return data
