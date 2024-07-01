from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class SubscriptionPlan:
    name: str
    stripe_id: str
    lookup_key: str
    price: float
    total_credits: int
    max_concurrent_pipelines: int
    max_collaborators: int
    description: str
    uid: Optional[str] = None

@dataclass
class UserSubscriptionPlan:
    user_uid: str # Foreign Key Many-to-1
    subscription_plan_uid: str # Foreign Key Many-to-1
    end_datetime_utc: datetime
    # total_credits: int
    consumed_credits: int = 0
    start_datetime_utc: datetime = field(default_factory=datetime.utcnow)
    uid: Optional[str] = None

