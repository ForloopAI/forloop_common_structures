from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

from forloop_modules.queries.db_model_templates import UserSubscriptionPlanPaymentStatusEnum


@dataclass
class SubscriptionPlan:
    name: str
    system_unique_name: str
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
    consumed_credits: int = 0
    # total_credits: int
    status: UserSubscriptionPlanPaymentStatusEnum
    start_datetime_utc: datetime = field(default_factory=datetime.utcnow)
    uid: Optional[str] = None

