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
    
    @staticmethod
    def get_webhook(eventTypeId, webhookId):
        # Get a specific webhook for a specific event type
        return EVENT_TYPE_ROUTES["get_webhook"].format(eventTypeId=eventTypeId, webhookId=webhookId)
    
    @staticmethod
    def list_webhooks(eventTypeId):
        # List webhooks for a specific event type
        return EVENT_TYPE_ROUTES["list_webhooks"].format(eventTypeId=eventTypeId)
    
    @staticmethod
    def create_webhook(eventTypeId):
        # Create a webhook for a specific event type
        return EVENT_TYPE_ROUTES["create_webhook"].format(eventTypeId=eventTypeId)
    
    @staticmethod
    def update_webhook(eventTypeId, webhookId):
        # Update a specific webhook for a specific event type
        return EVENT_TYPE_ROUTES["update_webhook"].format(eventTypeId=eventTypeId, webhookId=webhookId)
    
    @staticmethod
    def delete_webhook(eventTypeId, webhookId):
        # Delete a specific webhook for a specific event type
        return EVENT_TYPE_ROUTES["delete_webhook"].format(eventTypeId=eventTypeId, webhookId=webhookId)
    
    @staticmethod
    def delete_all_webhooks(eventTypeId):
        # Delete all webhooks for a specific event type
        return EVENT_TYPE_ROUTES["delete_all_webhooks"].format(eventTypeId=eventTypeId)