import json
from cal import CalSDK
from datetime import datetime

cal = CalSDK(api_key="")

## Example usage of the BookingAPI to create a new booking

# ## Get event types
# event_types = cal.event_types.list(
#     username='flipwedge'
# )

# print("Event Types:")
# for event_type in event_types:
#     print(f"ID: {event_type.id}, Name: {event_type.title}, Length: {event_type.lengthInMinutes} minutes")

# Create a new event type
# new_event_type = cal.event_types.create(
#     lengthInMinutes=30,
#     title="Practice Session",
#     slug="practice-session",
#     description="A session for practice and skill development.",
#     lengthInMinutesOptions=[30, 60, 90],
#     bookingFields=[
#         {
#             "name": "booking_desire",
#             "slug" : "booking_desire",
#             "type": "text",
#             "required": True,
#             "label": "What would you like to achieve in this session?"
#         }
#     ],
#     bookingLimitsCount={
#         "day": 1,
#     }
# )

# ## Get an event type by ID
# event_type = cal.event_types.get(eventTypeId=new_event_type.id)
# print(f"Event Type ID: {event_type.id}, Title: {event_type.title}, Length: {event_type.lengthInMinutes} minutes")

## Delete the event type
# delete_event = cal.event_types.delete(eventTypeId=)

# print(f"Event Type Deleted: {delete_event}")

## Update an event type
# updated_event_type = cal.event_types.update(
#     event_id=2936109,
#     title="Updated Again Practice Session",
#     description="An updated session for practice and skill development.",
#     lengthInMinutes=45,
# ) 

# print(f"Event Type Deleted: {delete}")

# print(f"New Event Type Created: ID: {new_event_type.id}, Title: {new_event_type.title}")

# for event_type in event_types:
#     print(event_type)

## Get all webhooks for an event type
# webhooks = cal.event_types.list_webhooks(eventTypeId=1893785)

# print("Webhooks for Event Type:")
# for webhook in webhooks:
#     print(f"ID: {webhook.id}, URL: {webhook.url}, Event Type ID: {webhook.eventTypeId}")

## Create a webhook for an event type
# new_webhook = cal.event_types.create_webhook(
#     eventTypeId=1893785,
#     active=False,
#     subscriberUrl="https://example.com/webhook",
#     triggers=["BOOKING_CREATED"],
# )

# get_webhook = cal.event_types.get_webhook(
#     eventTypeId=1893785,
#     webhookId=new_webhook.id
# )

# print(f"Webhook Created: ID: {get_webhook.id}, URL: {get_webhook.subscriberUrl}, Event Type ID: {get_webhook.eventTypeId}")

# # Update a webhook for an event type
# updated_webhook = cal.event_types.update_webhook(
#     eventTypeId=1893785,
#     webhookId=new_webhook.id,
#     active=True,
# )
# print(f"Webhook Updated: ID: {updated_webhook.id}, URL: {updated_webhook.subscriberUrl}, Event Type ID: {updated_webhook.eventTypeId}")

# print(f"Webhook Created: ID: {new_webhook.id}, URL: {new_webhook.subscriberUrl}, Event Type ID: {new_webhook.eventTypeId}")

# ## Delete all webhooks for an event type
# delete_webhooks = cal.event_types.delete_all_webhooks(eventTypeId=1893785)

# print(f"All Webhooks Deleted for Event Type ID: {delete_webhooks}")
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

# #Get a booking by UID
# booking = cal.bookings.get("nKJmqU9stG8dJQdSUmeVE8")
# print(booking)

## Get all bookings
# bookings = cal.bookings.list(
#     status="cancelled"
# )
# print(bookings)

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
# cancelled_booking = cal.bookings.cancel(
#     bookingUid="",
#     cancellationReason="Personal reasons",
#     cancelSubsequentBookings=False
# )

## Calendar Links
# calendar_links = cal.bookings.add_to_calendar_links(bookingUid="nKJmqU9stG8dJQdSUmeVE8")

# for link in calendar_links:
#     print(f"Label: {link.label}, Link: {link.link}")

