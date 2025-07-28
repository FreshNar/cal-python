from cal.urls.event_type import EVENT_TYPE_ROUTES

class EventTypeRoutes:
    """
    A class to manage event type routes.
    
    """

    @staticmethod
    def list():
        # Get all event types
        return EVENT_TYPE_ROUTES["list"]
    
    @staticmethod
    def create():
        # Create a new event type
        return EVENT_TYPE_ROUTES["create"]
    
    @staticmethod
    def get(eventTypeId):
        # Get a specific event type by ID
        return EVENT_TYPE_ROUTES["get"].format(eventTypeId=eventTypeId)
    
    @staticmethod
    def delete(eventTypeId):
        # Delete a specific event type by ID
        return EVENT_TYPE_ROUTES["delete"].format(eventTypeId=eventTypeId)
    
    @staticmethod
    def update(eventTypeId):
        # Update a specific event type by ID
        return EVENT_TYPE_ROUTES["get"].format(eventTypeId=eventTypeId)
    