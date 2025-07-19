from cal.client import serialize_to_csv, remove_empty_values
from typing import Optional, List, Union
from datetime import datetime
from cal.models.booking import Booking, BookingRecording, BookingTranscript

class BookingAPI:

    def __init__(self, client):
        self.client = client

    def get(self, bookingUid: str):
        response = self.client._request("GET", f"/bookings/{bookingUid}")
        return Booking.model_validate(response)

    def list(
        self,
        status: Optional[Union[str, List[str]]] = None,
        attendeeEmail: Optional[str] = None,
        attendeeName: Optional[str] = None,
        bookingUid: Optional[str] = None,
        eventTypeIds: Optional[Union[str, List[str]]] = None,
        eventTypeId: Optional[str] = None,
        teamsIds: Optional[Union[str, List[str]]] = None,
        teamId: Optional[str] = None,
        afterStart: Optional[str] = None,
        beforeEnd: Optional[str] = None,
        afterCreatedAt: Optional[str] = None,
        beforeCreatedAt: Optional[str] = None,
        afterUpdatedAt: Optional[str] = None,
        beforeUpdatedAt: Optional[str] = None,
        sortStart: Optional[str] = None,
        sortEnd: Optional[str] = None,
        sortCreated: Optional[str] = None,
        sortUpdatedAt: Optional[str] = None,
        take: Optional[int] = 100,
        skip: Optional[int] = 0
    ):

        data = {
            "status": serialize_to_csv(status),
            "attendeeEmail": attendeeEmail,
            "attendeeName": attendeeName,
            "bookingUid": bookingUid,
            "eventTypeIds": serialize_to_csv(eventTypeIds),
            "eventTypeId": eventTypeId,
            "teamsIds": serialize_to_csv(teamsIds),
            "teamId": teamId,
            "afterStart": afterStart,
            "beforeEnd": beforeEnd,
            "afterCreatedAt": afterCreatedAt,
            "beforeCreatedAt": beforeCreatedAt,
            "afterUpdatedAt": afterUpdatedAt,
            "beforeUpdatedAt": beforeUpdatedAt,
            "sortStart": sortStart,
            "sortEnd": sortEnd,
            "sortCreated": sortCreated,
            "sortUpdatedAt": sortUpdatedAt,
            "take": take,
            "skip": skip
        }

        response = self.client._request("GET", "/bookings", params=remove_empty_values(data))

        if isinstance(response, list):
            return [Booking.model_validate(booking) for booking in response]

        return Booking.model_validate(response)

    def create(
            self,
            start: datetime,
            attendeeName: str,
            attendeeTimeZone: str,
            attendeeEmail: Optional[str] = None,
            attendeePhoneNumber: Optional[str] = None,
            attendeeLanguage: Optional[Union[str, List[str]]] = None,
            bookingFieldResponses: Optional[dict] = None,
            eventTypeId: Optional[int] = None,
            eventTypeSlug: Optional[str] = None,
            username: Optional[str] = None,
            teamSlug: Optional[str] = None,
            organizationSlug: Optional[str] = None,
            guests: Optional[Union[str, List[str]]] = None,
            locationType: str = "online",
            locationAddress: Optional[str] = None,
            locationPhone: Optional[str] = None,
            locationIntegration: Optional[Union[str, List[str]]] = None,
            metadata: Optional[dict] = None,
            lengthInMinutes: Optional[int] = None,
    ):

        data = {
            "start": start.isoformat(),
            "attendee": {
                "name": attendeeName,
                "timeZone": attendeeTimeZone,
                "email": attendeeEmail,
                "phoneNumber": attendeePhoneNumber,
                "language": serialize_to_csv(attendeeLanguage),
            },
            "bookingFieldsResponses": bookingFieldResponses,
            "eventTypeId": eventTypeId,
            "eventTypeSlug": eventTypeSlug,
            "username": username,
            "teamSlug": teamSlug,
            "organizationSlug": organizationSlug,
            "guests": serialize_to_csv(guests),
            "location" : {
                "type": locationType,
                "address": locationAddress,
                "phone": locationPhone,
                "integration": serialize_to_csv(locationIntegration)
            },
            "metadata": metadata,
            "lengthInMinutes": lengthInMinutes
        }

        response = self.client._request("POST", "/bookings", json=remove_empty_values(data))
        return Booking.model_validate(response)
    
    def get_recordings(self, bookingUid: str):
        response = self.client._request("GET", f"/bookings/{bookingUid}/recordings")
        return BookingRecording.model_validate(response)
    
    def get_transcript(self, bookingUid: str):
        response = self.client._request("GET", f"/bookings/{bookingUid}/transcript")
        return BookingTranscript.model_validate(response) if response else None
    
    def reschedule(
            self, 
            bookingUid: str, 
            start: datetime,
            rescheduledBy: Optional[str] = None,
            seatUid: Optional[str] = None,
            reschedulingReason: Optional[str] = None
        ):

        data = {
            "start": start.isoformat(),
            "rescheduledBy": rescheduledBy,
            "seatUid": seatUid,
            "reschedulingReason": reschedulingReason
        }

        response = self.client._request("POST", f"/bookings/{bookingUid}/reschedule", json=remove_empty_values(data))
        return Booking.model_validate(response)
    
    def cancel(
            self, 
            bookingUid: str, 
            cancellationReason: Optional[str] = None, 
            cancelSubsequentBookings: bool = False,
            seatUid: Optional[str] = None
        ):
        data = {
            "cancellationReason": cancellationReason,
            "cancelSubsequentBookings": cancelSubsequentBookings,   
            "seatUid": seatUid
        }

        response = self.client._request("POST", f"/bookings/{bookingUid}/cancel", json=remove_empty_values(data))
        return Booking.model_validate(response)
    
    def mark_absent(
            self,
            bookingUid: str,
            attendees: dict,
            host: Optional[bool] = None,
        ):
        data = {
            "host": host,
            "attendees": attendees
        }

        response = self.client._request("POST", f"/bookings/{bookingUid}/mark-absence", json=data)
        return Booking.model_validate(response)
    
    def reassign(
            self,
            bookingUid: str,
    ):
        response = self.client._request("POST", f"/bookings/{bookingUid}/reassign")
        return response
        