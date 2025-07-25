from cal.models.unified_calendar import *
from cal.routes import Routes

class UnifiedCalendarAPI:
    """
    A unified calendar is an API resource that represents a calendar integration.
    """

    def __init__(self, client):
        self.client = client
        self.routes = Routes()

    def get(self, calendar: str, eventUid: str):
        """
        Retrieve a unified calendar by its calendar and event UID.
        """
        response = self.client._request("GET", self.routes.unified_calendar.get(calendar, eventUid))
        return UnifiedCalendar.model_validate(response)
    