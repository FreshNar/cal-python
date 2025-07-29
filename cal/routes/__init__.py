from cal.routes.unified_calendar import UnifiedCalendarRoutes
from cal.routes.booking import BookingRoutes
from cal.routes.event_type import EventTypeRoutes
from cal.routes.me import MeRoutes

class Routes:
    """
    A class to manage all routes.

    """

    def __init__(self):
        self.booking = BookingRoutes()
        self.unified_calendar = UnifiedCalendarRoutes()
        self.event_type = EventTypeRoutes()
        self.me = MeRoutes()
