from pydantic import BaseModel
from typing import Literal


class Resolution(BaseModel):

    recommended_action: str

    agent_explanation: str

    customer_response: str

    escalation_required: bool

    risk_level: Literal["low", "medium", "high"]