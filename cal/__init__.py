from cal.client import CalClient
from cal.apis.bookings import BookingAPI
from cal.apis.api_keys import APIKeysAPI
from cal.apis.event_type import EventTypeAPI
from cal.apis.me import MeAPI

class CalSDK:
    def __init__(self, api_key: str):
        self.client = CalClient(api_key)
        self.bookings = BookingAPI(self.client)
        self.api_keys = APIKeysAPI(self.client)
        self.event_types = EventTypeAPI(self.client)
        self.me = MeAPI(self.client)