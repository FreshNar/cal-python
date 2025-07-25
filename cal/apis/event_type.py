from typing import Optional, List, Union

from cal.utils import serialize_to_csv, remove_empty_values
from cal.models.event_type import EventType
from cal.routes import Routes

api_version = "2024-06-14"

class EventTypeAPI:
    """
    An event type is an API resource that represents a specific type of event that can be booked.
    """

    def __init__(self, client):
        self.client = client
        self.routes = Routes()

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
        
