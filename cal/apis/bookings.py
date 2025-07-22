from typing import Optional, List, Union

from cal.utils import serialize_to_csv, remove_empty_values
from cal.models.booking import *
from cal.routes import Routes

class BookingAPI:
    """
    A booking is an API resource that represents a scheduled event between an attendee and a host.
    
    Related API resources:
    - [Booking](https://cal.com/docs/api-reference/v2/bookings/)
    """

    def __init__(self, client):
        self.client = client

    def get(self, bookingUid: str):
        """
        Retrieve a booking by its UID.
        """
        response = self.client._request("GET", Routes.booking.get(bookingUid))
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
        """
        Retrieve a list of bookings with optional filters.
        """

        raw_params = {
            k: serialize_to_csv(v) if k in {"status", "eventTypeIds", "teamsIds"} else v
            for k, v in locals().items()
            if k not in {"self"}
        }

        response = self.client._request("GET", Routes.booking.list(), params=remove_empty_values(raw_params))

        if isinstance(response, list):
            return [Booking.model_validate(booking) for booking in response]

        return Booking.model_validate(response)

    def create(
            self,
            start: str,  # Expecting ISO 8601 string
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
        """
        Create a new booking.
        
        """

        data = {
            "start": start,  # Should be ISO 8601 string
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

        response = self.client._request("POST", Routes.booking.create(), json=remove_empty_values(data))
        return Booking.model_validate(response)
    
    def get_recordings(self, bookingUid: str):
        """
        Retrieve recordings for a booking by its UID.
        """
        response = self.client._request("GET", Routes.booking.get_recordings(bookingUid))
        return BookingRecording.model_validate(response)
    
    def get_transcript(self, bookingUid: str):
        """
        Retrieve the transcript for a booking by its UID.
        """ 
        response = self.client._request("GET", Routes.booking.get_transcript(bookingUid))
        return BookingTranscript.model_validate(response) if response else None
    
    def reschedule(
            self, 
            start: str,  # Expecting ISO 8601 string
            bookingUid: str, 
            rescheduledBy: Optional[str] = None,
            seatUid: Optional[str] = None,
            reschedulingReason: Optional[str] = None
        ):
        """
        Reschedule a booking to a new start time.
        """

        data = {
            "start": start,  # Should be ISO 8601 string
            "rescheduledBy": rescheduledBy,
            "seatUid": seatUid,
            "reschedulingReason": reschedulingReason
        }

        response = self.client._request("POST", Routes.booking.reschedule(bookingUid), json=remove_empty_values(data))
        return Booking.model_validate(response)
    
    def cancel(
            self, 
            bookingUid: str, 
            cancellationReason: Optional[str] = None, 
            cancelSubsequentBookings: bool = False,
            seatUid: Optional[str] = None
        ):
        """
        Cancel a booking.
        """
        data = {
            "cancellationReason": cancellationReason,
            "cancelSubsequentBookings": cancelSubsequentBookings,   
            "seatUid": seatUid
        }

        response = self.client._request("POST", Routes.booking.cancel(bookingUid), json=remove_empty_values(data))
        return Booking.model_validate(response)
    
    def mark_absent(
            self,
            bookingUid: str,
            attendees: dict,
            host: Optional[bool] = None,
        ):
        """
        Mark an attendee as absent for the specified booking.
        """
        data = {
            "host": host,
            "attendees": attendees
        }

        response = self.client._request("POST", Routes.booking.mark_absent(bookingUid), json=data)
        return Booking.model_validate(response)
    
    def reassign_auto(
            self,
            bookingUid: str,
    ):
        """
        Reassign a booking automatically to a different host.

        """
        response = self.client._request("POST", Routes.booking.reassign_auto(bookingUid))
        return response

    def reassign_specific(
            self,
            bookingUid: str,
            userId: int,
    ):
        """
        Reassign a booking to a specific user by their ID.

        NOTE: Currently only supports reassigning host for round robin bookings
        """
        data = {
            "userId": userId
        }

        response = self.client._request("POST", Routes.booking.reassign_specific(bookingUid, userId), json=data)
        return Booking.model_validate(response)
    
    def confirm(
            self,
            bookingUid : str,
    ):
        """
        Confirm a booking by its UID.
        """

        response = self.client._request("POST", Routes.booking.confirm(bookingUid))
        return response
    
    def decline(
            self,
            bookingUid: str,
            reason: Optional[str] = None,
    ):
        """
        Decline a booking by its UID.
        """

        data = {
            "reason": reason
        }

        response = self.client._request("POST", Routes.booking.decline(bookingUid), json=data)
        return response
    
    def add_to_calendar_links(
            self,
            bookingUid: str,
    ):
        """
        Retrieve add to calendar links for a booking.
        """

        response = self.client._request("GET", Routes.booking.add_to_calendar_links(bookingUid))
        return [CalendarLink.model_validate(link) for link in response] if isinstance(response, list) else CalendarLink.model_validate(response)
    
    def references(
            self,
            bookingUid: str,
            type: Optional[str] = None,
    ):
        """
        Retrieve references for a booking.
        """
        data = {
            "type": type
        }

        response = self.client._request("GET", Routes.booking.references(bookingUid), params=data)
        return [Reference.model_validate(ref) for ref in response] if isinstance(response, list) else Reference.model_validate(response)
    
