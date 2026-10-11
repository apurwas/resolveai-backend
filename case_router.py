import os

from pydantic import BaseModel
from typing import Literal

from dotenv import load_dotenv
from google import genai


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


class CaseRoute(BaseModel):
    intent: str

    requires_customer_data: bool

    investigation_type: Literal[
        "none",
        "account",
        "transaction",
        "upi",
        "card",
        "refund",
        "dispute",
        "atm",
        "loan",
        "emi",
        "fees",
        "statement",
        "beneficiary",
        "service_request"
    ]

    reasoning: str


def route_case(customer_message):

    prompt = f"""
You are the case-routing engine for ResolveAI,
an AI customer-service resolution copilot for a bank.

Your job is to understand the customer's request BEFORE
customer-specific banking data is accessed.

CUSTOMER MESSAGE:
{customer_message}

Determine:

1. intent
   - Describe the customer's main issue briefly.

2. requires_customer_data
   - true when resolving the request requires information
     specific to this customer.
   - false for general how-to, informational, or policy questions.

3. investigation_type

Choose exactly ONE:

- none
- account
- transaction
- upi
- card
- refund
- dispute
- atm
- loan
- emi
- fees
- statement
- beneficiary
- service_request

Definitions:

none:
General information, policy, or how-to question.

account:
Account access, account status, login, MPIN, account restrictions,
or other account-level problems.

transaction:
A general transaction-specific investigation where the payment
rail is not clearly UPI, card, or ATM.

upi:
UPI payment, UPI transfer, UPI debit, UPI pending/reversed/failed,
or recipient-not-received issues.

card:
Card-specific problems, card payment failures, card declines,
card usage, or card-related transactions.

refund:
Questions about a refund that has already been initiated or
is expected.

dispute:
A transaction dispute, unauthorized transaction, or request
to raise/check a dispute.

atm:
ATM cash withdrawal, cash not received, partial cash,
or ATM debit issues.

loan:
Loan account, loan status, loan details, or loan-related problems.

emi:
EMI amount, EMI payment, EMI schedule, or EMI-related issues.

fees:
A customer-specific fee or charge that needs investigation.

statement:
Customer-specific account statement or statement-related request.

beneficiary:
Adding, removing, updating, or troubleshooting a beneficiary.

service_request:
Status or details of an existing customer service request.

Examples:

"How do I set my MPIN?"
→ requires_customer_data = false
→ investigation_type = none

"I cannot set my MPIN and it keeps failing."
→ requires_customer_data = true
→ investigation_type = account

"My UPI payment was debited but the merchant didn't receive it."
→ requires_customer_data = true
→ investigation_type = upi

"What is the process for disputing a card payment?"
→ requires_customer_data = false
→ investigation_type = none

"I don't recognize this card transaction."
→ requires_customer_data = true
→ investigation_type = dispute

"Why was my card payment declined?"
→ requires_customer_data = true
→ investigation_type = card

"The ATM debited my account but didn't give me cash."
→ requires_customer_data = true
→ investigation_type = atm

"How can I get an account statement?"
→ requires_customer_data = false
→ investigation_type = none

"I need my account statement for last month."
→ requires_customer_data = true
→ investigation_type = statement

"Why was I charged this fee?"
→ requires_customer_data = true
→ investigation_type = fees

"How do I add a beneficiary?"
→ requires_customer_data = false
→ investigation_type = none

"I can't add my beneficiary."
→ requires_customer_data = true
→ investigation_type = beneficiary

"What's the status of my complaint?"
→ requires_customer_data = true
→ investigation_type = service_request

Important rules:

- Classify the customer's actual request, not just keywords.
- A general question about a banking process does not require
  customer-specific data.
- A problem involving the customer's own account, transaction,
  payment, fee, refund, or service request generally requires
  customer-specific data.
- Do not invent customer information.
- Return only the requested structured fields.
"""

    response = client.interactions.create(
        model="gemini-3.5-flash-lite",
        input=prompt,
        response_format={
            "type": "text",
            "mime_type": "application/json",
            "schema": CaseRoute.model_json_schema()
        }
    )

    return CaseRoute.model_validate_json(
        response.output_text
    )