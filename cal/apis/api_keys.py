from typing import Optional

class APIKeysAPI:

    def __init__(self, client):
        self.client = client

    def refresh(self, daysValid: int, neverExpires: Optional[bool] = None):
        """
        Generate a new API key and delete the current one.
        """
        return self.client._request("POST", f"/api-keys/refresh", params={
            "daysValid": daysValid,
            "neverExpires": neverExpires
        })