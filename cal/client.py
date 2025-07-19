import requests

def serialize_to_csv(value):
    if isinstance(value, list):
        return ",".join(value)
    return value

def remove_empty_values(data):
    return {k: v for k, v in data.items() if v is not None}

class CalClient:

    def __init__(self, api_key: str, base_url: str = "https://api.cal.com/v2"):
        self.api_key = api_key
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            "cal-api-version": "2024-08-13",
            "Authorization": f"{self.api_key}",
        })

    def _request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        response = self.session.request(method, url, **kwargs)
        if not response.ok:
            raise Exception(f"API Error {response.status_code}: {response.text}")
        return response.json()['data'] if 'data' in response.json() else response.json()
