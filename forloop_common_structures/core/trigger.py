import datetime
from dataclasses import dataclass
from typing import Optional


@dataclass
class Trigger:
    trigger_name: str
    pipeline_uid: int
    frequency: int
    project_uid: str
    first_run: datetime.datetime
    uid: Optional[str] = None
