from cal.models.unified_calendar import *
from cal.routes import Routes

class UnifiedCalendarAPI:
    """
    A unified calendar is an API resource that represents a calendar integration.
    """

    def __init__(self, client):
        self.client = client

    def get(self, calendar: str, eventUid: str):
        """
        Retrieve a unified calendar by its calendar and event UID.
        """
        response = self.client._request("GET", Routes.unified_calendar.get(calendar, eventUid))
        return UnifiedCalendar.model_validate(response)
    