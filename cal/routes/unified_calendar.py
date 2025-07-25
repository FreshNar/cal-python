from cal.urls.unified_calendar import UNIFIED_CALENDAR_ROUTES

class UnifiedCalendarRoutes:
    """
    A class to manage unified calendar routes.
    This class provides methods to build URLs for unified calendar-related API endpoints.
    """

    @staticmethod
    def get(calendar, eventUid): 
        return UNIFIED_CALENDAR_ROUTES["get"].format(calendar=calendar, eventUid=eventUid)