from cal.client import CalClient
from cal.apis.bookings import BookingAPI
from cal.apis.api_keys import APIKeysAPI

class CalSDK:
    def __init__(self, api_key: str):
        self.client = CalClient(api_key)
        self.bookings = BookingAPI(self.client)
        self.api_keys = APIKeysAPI(self.client)