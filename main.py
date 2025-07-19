import json
from cal import CalSDK
from datetime import datetime

cal = CalSDK(api_key="")


## Example usage of the BookingAPI to create a new booking

# new_booking = cal.bookings.create(
#     start=datetime(2025, 7, 30, 16, 0),
#     attendeeName="John Doe",
#     attendeeTimeZone="America/New_York",
#     attendeeEmail="john.doe@example.com",
#     attendeePhoneNumber="+1234567890",
#     attendeeLanguage="en",
#     bookingFieldResponses={
#         "booking_desire" : "Practice Session",
#     },
#     locationType="address",
#     eventTypeId=1893785,
#     lengthInMinutes=30,
# )

## Get a booking by UID
# booking = cal.bookings.get("")

## Get all bookings
# bookings = cal.bookings.list(
#     status="cancelled"
# )

# # Refresh API Keys
# keys = cal.api_keys.refresh(
#     daysValid=30,
#     neverExpires=False
# )

## Get recordings for a booking
# recordings = cal.bookings.get_recordings("")
# print(recordings)

## Get transcript for a booking
# transcript = cal.bookings.get_transcript("")
# print(transcript)

## Reschedule a booking
# rescheduled_booking = cal.bookings.reschedule(
#     bookingUid="",
#     start=datetime(2025, 7, 29, 17, 0),
#     reschedulingReason="Schedule conflict"
# )

## Cancel a booking
cancelled_booking = cal.bookings.cancel(
    bookingUid="",
    cancellationReason="Personal reasons",
    cancelSubsequentBookings=False
)
print(cancelled_booking)