from typing import Optional, List, Union

from cal.models.me import Me
from cal.routes import Routes

class MeAPI:
    """
    A class to manage user-related API calls.

    Related API resources:
    - [Me](https://cal.com/docs/api-reference/v2/me/)
    """

    def __init__(self, client):
        self.client = client
        self.routes = Routes()

    def get(self):
        """
        Retrieve the current user's profile.
        """
        response = self.client._request("GET", self.routes.me.get())
        return Me.model_validate(response)
    
    def update(
        self,
        email: str = None,
        name: str = None,
        timeFormat: int = None,
        defaultScheduleId: int = None,
        weekStart: str = None,
        timeZone: str = None,
        locale: str = None,
        avatarUrl: str = None,
        bio: str = None,
        metadata: dict = None,
    ):
        """
        Update the current user's profile.
        """
        data = {k: v for k, v in locals().items() if k != "self" and v is not None}
        response = self.client._request("PATCH", self.routes.me.update(), json=data)
        return Me.model_validate(response)