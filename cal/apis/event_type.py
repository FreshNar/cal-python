from typing import Optional, List, Union

from cal.utils import serialize_to_csv, remove_empty_values
from cal.models.event_type import EventType, EventTypeWebhook
from cal.routes import Routes

api_version = "2024-06-14"

class EventTypeAPI:
    """
    An event type is an API resource that represents a specific type of event that can be booked.
    """

    def __init__(self, client):
        self.client = client
        self.routes = Routes()

    def get(self, eventTypeId: int):
        if not eventTypeId:
            raise ValueError("eventTypeId is required.")

        response = self.client._request("GET", self.routes.event_type.get(eventTypeId=eventTypeId), api_version=api_version)
        return EventType.model_validate(response)

    def list(
            self,
            username: Optional[str] = None,
            eventSlug: Optional[str] = None,
            usernames: Optional[Union[str, List[str]]] = None,
            orgSlug: Optional[str] = None,
            orgId: Optional[str] = None, 
    ):
        if not any([username, eventSlug, usernames, orgSlug, orgId]):
            raise ValueError("At least one of 'username', 'eventSlug', 'usernames', 'orgSlug', or 'orgId' is required.")

        raw_params = {
            k: serialize_to_csv(v) if k in {"usernames"} else v
            for k, v in locals().items()
            if k not in {"self"}
        }

        response = self.client._request("GET", self.routes.event_type.list(), api_version=api_version, params=remove_empty_values(raw_params))
        return [EventType.model_validate(item) for item in response]
        
    def create(
            self,
            lengthInMinutes: int,
            title: str,
            slug: str,
            lengthInMinutesOptions: Optional[List[int]] = None,
            description: Optional[str] = None,
            bookingFields: Optional[List[dict]] = None,
            disableGuests: Optional[bool] = None,
            slotInterval: Optional[int] = None,
            minimumBookingNotice: Optional[int] = None,
            beforeEventBuffer: Optional[int] = None,
            afterEventBuffer: Optional[int] = None,
            scheduleId: Optional[int] = None,
            bookingLimitsCount: Optional[dict] = None,
            onlyShowFirstAvailableSlot: Optional[bool] = None,
            bookingLimitsDuration: Optional[List[dict]] = None,
            bookingWindow: Optional[dict] = None,
            offsetStart: Optional[int] = None,
            bookerLayouts: Optional[dict] = None,
            confirmationPolicy: Optional[dict] = None,
            recurrence: Optional[dict] = None,
            requiresBookerEmailVerification: Optional[bool] = None,
            hideCalendarNotes: Optional[bool] = None,
            lockTimeZoneToggleOnBookingPage: Optional[bool] = None,
            color: Optional[dict] = None,
            seats: Optional[dict] = None,
            customName: Optional[str] = None,
            destinationCalendars: Optional[List[dict]] = None,
            useDestinationCalendarEmail: Optional[bool] = None,
            hideCalendarEventDetails: Optional[bool] = None,
            successRedirectUrl: Optional[str] = None,
            hideOrganizerEmail: Optional[bool] = None,
            calVideoSettings: Optional[dict] = None,
            locations: Optional[List[dict]] = None
    ):
        
        raw_params = {
            k: v
            for k, v in locals().items()
            if k not in {"self"}
        }

        response = self.client._request("POST", self.routes.event_type.create(), api_version=api_version, json=remove_empty_values(raw_params))
        return EventType.model_validate(response)
    
    def update(
        self,
        event_id: str,
        **kwargs
        ):
        payload = remove_empty_values(kwargs)

        response = self.client._request(
            "PATCH",
            self.routes.event_type.update(event_id),
            api_version=api_version,
            json=payload
        )

        return EventType.model_validate(response)

    
    def delete(self, eventTypeId: int):
        if not eventTypeId:
            raise ValueError("eventTypeId is required.")

        response = self.client._request("DELETE", self.routes.event_type.delete(eventTypeId=eventTypeId), api_version=api_version)
        return response
    
    def get_webhook(self, eventTypeId: int, webhookId: int):
        if not eventTypeId or not webhookId:
            raise ValueError("Both eventTypeId and webhookId are required.")

        response = self.client._request("GET", self.routes.event_type.get_webhook(eventTypeId=eventTypeId, webhookId=webhookId), api_version=api_version)
        return EventTypeWebhook.model_validate(response)

    def list_webhooks(self, eventTypeId: int):
        if not eventTypeId:
            raise ValueError("eventTypeId is required.")

        response = self.client._request("GET", self.routes.event_type.list_webhooks(eventTypeId=eventTypeId), api_version=api_version)
        return response
    
    def create_webhook(
        self,
        eventTypeId: int,
        active: bool,
        subscriberUrl: str,
        triggers: List[str],
        payloadTemplate: Optional[str] = None,
        secret: Optional[str] = None,
    ):
        if not subscriberUrl or not triggers:
            raise ValueError("subscriberUrl and triggers are required.")

        payload = {
            "active": active,
            "subscriberUrl": subscriberUrl,
            "triggers": triggers,
            "payloadTemplate": payloadTemplate,
            "secret": secret
        }

        response = self.client._request(
            "POST",
            self.routes.event_type.create_webhook(eventTypeId=eventTypeId),
            api_version=api_version,
            json=remove_empty_values(payload)
        )

        return EventTypeWebhook.model_validate(response)
    
    def update_webhook(self, eventTypeId: int, webhookId: int, **kwargs):
        if not eventTypeId or not webhookId:
            raise ValueError("Both eventTypeId and webhookId are required.")

        payload = remove_empty_values(kwargs)

        response = self.client._request(
            "PATCH",
            self.routes.event_type.update_webhook(eventTypeId=eventTypeId, webhookId=webhookId),
            api_version=api_version,
            json=payload
        )
        return EventTypeWebhook.model_validate(response)
    
    def delete_webhook(self, eventTypeId: int, webhookId: int):
        if not eventTypeId or not webhookId:
            raise ValueError("Both eventTypeId and webhookId are required.")

        response = self.client._request(
            "DELETE",
            self.routes.event_type.delete_webhook(eventTypeId=eventTypeId, webhookId=webhookId),
            api_version=api_version
        )
        return response

    def delete_all_webhooks(self, eventTypeId: int):
        if not eventTypeId:
            raise ValueError("eventTypeId is required.")

        response = self.client._request(
            "DELETE",
            self.routes.event_type.delete_all_webhooks(eventTypeId=eventTypeId),
            api_version=api_version
        )
        return response