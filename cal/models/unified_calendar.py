from typing import Optional, List
from pydantic import BaseModel
from models.booking import Host, Attendee

class UnifiedCalendar(BaseModel):
    start: str
    end: str
    id: str
    status: str
    title: str
    source: List[str]
    description: Optional[str] = None
    locations: Optional[List[str]] = None
    attendees: Optional[List[Attendee]] = None
    status: Optional[str] = None
    hosts: Optional[List[Host]] = None


