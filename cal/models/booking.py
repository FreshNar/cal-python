from pydantic import BaseModel
from typing import List, Optional, Dict, Any

class Host(BaseModel):
    id: int
    name: str
    email: str
    username: str
    timeZone: str


class EventType(BaseModel):
    id: int
    slug: str


class Attendee(BaseModel):
    name: str
    email: str
    timeZone: str
    language: str
    absent: bool


class BookingFieldsResponses(BaseModel):
    email: str
    name: str
    guests: Optional[List[Any]] = []
    attendeePhoneNumber: Optional[str] = None
    location: Dict[str, Any]


class Booking(BaseModel):
    id: int
    uid: str
    title: str
    description: str
    hosts: List[Host]
    status: str
    start: str
    end: str
    duration: int
    eventTypeId: Optional[int] = None
    eventType: Optional[EventType] = None
    location: str
    absentHost: bool
    createdAt: str
    updatedAt: Optional[str] = None
    attendees: List[Attendee]
    bookingFieldsResponses: BookingFieldsResponses
    cancellationReason: Optional[str] = None
    cancelledByEmail: Optional[str] = None
    reschedulingReason: Optional[str] = None
    rescheduledByEmail: Optional[str] = None
    rescheduledFromUid: Optional[str] = None
    rescheduledToUid: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    rating: Optional[int] = None
    icsUid: str
    guests: Optional[List[str]] = None
    error: Optional[str] = None


class BookingRecording(BaseModel):
    id: str
    roomName: str
    startTs: int
    status: str
    maxParticipants: Optional[int] = None
    duration: int
    shareToken: str
    downloadLink: Optional[str] = None
    error: Optional[str] = None

class BookingTranscript(BaseModel):
    id: str
    data: str
    status: str

class CalendarLink(BaseModel):
    label: str
    link: str


class Reference(BaseModel):
    type: str
    eventUid: str
    destinationCalendarId: str
    id: str