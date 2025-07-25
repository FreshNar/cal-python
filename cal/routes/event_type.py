from cal.urls.event_type import EVENT_TYPE_ROUTES

class EventTypeRoutes:
    """
    A class to manage event type routes.
    
    """

    @staticmethod
    def list():
        # Get all event types
        return EVENT_TYPE_ROUTES["list"]