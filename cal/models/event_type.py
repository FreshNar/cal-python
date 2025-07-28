from typing import Any, Dict, Optional, List
from pydantic import BaseModel, Field

class EventType(BaseModel):
    id: int
    lengthInMinutes: int
    title: str = Field(..., min_length=1)
    slug: str
    description: str
    locations: List[dict]
    bookingFields: List[dict]
    disableGuests: bool
    recurrence: Any
    metadata: dict
    price: int
    currency: str
    lockTimeZoneToggleOnBookingPage: bool
    successRedirectUrl: Optional[str] = None
    isInstantEvent: bool
    scheduleId: Optional[int] = None
    ownerId: int
    users: List[dict]
    lengthInMinutesOptions: Optional[List[int]] = None
    slotInterval: Optional[int] = None
    minimumBookingNtoice: Optional[int] = None
    beforeEventBuffer: Optional[int] = None
    afterEventBuffer: Optional[int] = None
    seatsPerTimeSlot: Optional[int] = None
    seatsShowAvailabilityCount: Optional[bool] = None
    bookingLimitsCount: Optional[dict] = None
    onlyShowFirstAvailableSlot: Optional[bool] = None
    bookingLimitsDuration: Optional[dict] = None
    bookingWindow: Optional[dict] = None
    bookerLayouts: Optional[List[dict]] = None
    confirmationPolicy: Optional[dict] = None
    requiresBookerEmailVerification: Optional[bool] = None
    hideCalendarNotes: Optional[bool] = None
    color: Optional[List[dict]] = None
    seats: Optional[dict] = None
    offsetStart: Optional[int] = None
    customName: Optional[str] = None
    destinationCalendar: Optional[dict] = None
    useDestinationCalendarEmail: Optional[bool] = None
    hideCalendarEventDetails: Optional[bool] = None
    hideOrganizerEmail: Optional[bool] = None
    calVideoSettings: Optional[dict] = None

class EventTypeWebhook(BaseModel):
    payloadTemplate: Optional[str] = None
    eventTypeId: int
    id: str
    triggers: List[str]
    subscriberUrl: str
    active: bool
    secret: Optional[str] = None
    