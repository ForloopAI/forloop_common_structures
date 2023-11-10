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
    first_run_utc: datetime.datetime
    frequency: TriggerFrequencyEnum
    pipeline_uid: str
    project_uid: str
    uid: Optional[str] = None
