from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel
from typing import Literal
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("ERROR: GEMINI_API_KEY was not found.")
    exit()

client = genai.Client(api_key=api_key)


class CustomerCase(BaseModel):
    intent: Literal[
        "UPI_PAYMENT_FAILED",
        "UPI_PAYMENT_PENDING",
        "UPI_PAYMENT_REVERSED",
        "UPI_DEBITED_NOT_RECEIVED",
        "CARD_PAYMENT_FAILED",
        "CARD_PAYMENT_DISPUTE",
        "CARD_PAYMENT_DUPLICATE",
        "CARD_PAYMENT_REVERSED",
        "ATM_DEBITED_NO_CASH",
        "ATM_PARTIAL_CASH",
        "ATM_CASH_NOT_RECEIVED",
        "ACCOUNT_BLOCKED",
        "LOGIN_ISSUE",
        "MPIN_ISSUE",
        "REFUND_PENDING",
        "UNEXPECTED_CHARGE",
        "FEE_DISPUTE",
        "OTHER",
    ]

    priority: Literal["low", "medium", "high"]
    summary: str
    sentiment: Literal["positive", "neutral", "negative", "frustrated"]


customer_message = """
I tried to withdraw cash from an ATM this morning. My account
was debited ₹5,000, but the ATM did not dispense any cash.
"""


prompt = f"""
You are a banking customer-service AI assistant.

Analyze the customer's message and classify it into exactly ONE
of the approved intent categories below.

APPROVED INTENTS:

UPI_PAYMENT_FAILED:
The customer's UPI payment failed.

UPI_PAYMENT_PENDING:
The customer's UPI payment is still pending.

UPI_PAYMENT_REVERSED:
A previously completed UPI payment was reversed.

UPI_DEBITED_NOT_RECEIVED:
The customer's account was debited, but the merchant did not receive the money.

CARD_PAYMENT_FAILED:
A card payment failed.

CARD_PAYMENT_DISPUTE:
The customer disputes a card transaction.

CARD_PAYMENT_DUPLICATE:
The customer appears to have been charged twice for the same card transaction.

CARD_PAYMENT_REVERSED:
A card transaction was reversed.

ATM_DEBITED_NO_CASH:
The customer's account was debited, but the ATM dispensed no cash.

ATM_PARTIAL_CASH:
The customer's account was debited, but the ATM dispensed only part of the requested cash.

ATM_CASH_NOT_RECEIVED:
The customer reports an issue with receiving cash from an ATM.

ACCOUNT_BLOCKED:
The customer's account is blocked.

LOGIN_ISSUE:
The customer cannot log into their banking account or application.

MPIN_ISSUE:
The customer has an issue with their MPIN.

REFUND_PENDING:
The customer is waiting for a refund.

UNEXPECTED_CHARGE:
The customer reports an unexpected charge.

FEE_DISPUTE:
The customer disputes a fee or charge.

OTHER:
The customer's issue does not clearly match any of the categories above.

IMPORTANT:
- Choose exactly ONE approved intent.
- Do not create a new intent.
- Use the exact intent code provided above.

Also identify:
- the priority
- a concise summary
- the customer's sentiment

Customer message:
{customer_message}
"""


interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=prompt,
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": CustomerCase.model_json_schema()
    },
)


case = CustomerCase.model_validate_json(interaction.output_text)

print(case)