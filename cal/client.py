import requests

cal_api_version = "2024-08-13"
cal_base_url = "https://api.cal.com/v2"

class CalClient:

    def __init__(self, api_key: str, base_url: str = cal_base_url):
        self.api_key = api_key
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            "cal-api-version": cal_api_version,
            "Authorization": f"{self.api_key}",
        })

    def _request(self, method, endpoint, api_version=None, **kwargs):
        url = f"{self.base_url}{endpoint}"
        if api_version:
            self.session.headers.update({"cal-api-version": api_version})
        response = self.session.request(method, url, **kwargs)
        if not response.ok:
            raise Exception(f"API Error {response.status_code}: {response.text}")
        return response.json()['data'] if 'data' in response.json() else response.json()
