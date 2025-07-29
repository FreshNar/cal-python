from pydantic import BaseModel
from typing import List, Optional, Dict, Any

class Me(BaseModel):
    id: int
    username: str
    email: str
    timeFormat: int
    defaultScheduleId: Optional[int] = None
    weekStart: str
    timeZone: str
    organizationId: Optional[int] = None
    organization: Optional[Dict[str, Any]] = None