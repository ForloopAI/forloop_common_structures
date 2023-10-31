import datetime
from dataclasses import dataclass
from enum import Enum
from typing import Optional


class TriggerFrequencyEnum(str, Enum):
    HOURLY = "hourly"
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"

@dataclass
class Trigger:
    name: str
    first_run: datetime.datetime
    frequency: TriggerFrequencyEnum
    pipeline_uid: int
    project_uid: str
    uid: Optional[str] = None
