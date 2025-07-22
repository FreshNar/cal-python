BOOKING_ROUTES = {
    "get": "/bookings/{bookingUid}",
    "list": "/bookings",
    "create": "/bookings",
    "get_recordings": "/bookings/{bookingUid}/recordings",
    "get_transcript": "/bookings/{bookingUid}/transcript",
    "reschedule": "/bookings/{bookingUid}/reschedule",
    "cancel": "/bookings/{bookingUid}/cancel",
    "mark_absent": "/bookings/{bookingUid}/mark-absence",
    "reassign_auto": "/bookings/{bookingUid}/reassign",
    "reassign_specific": "/bookings/{bookingUid}/reassign/{userId}",
    "confirm": "/bookings/{bookingUid}/confirm",
    "decline": "/bookings/{bookingUid}/decline",
    "add_to_calendar_links": "/bookings/{bookingUid}/calendar-links",
    "references" : "/bookings/{bookingUid}/references"
}

UNIFIED_CALENDAR_ROUTES = {
    "get": "/calendars/{calendar}/event/{eventUid}",
}
