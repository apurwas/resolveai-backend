from pathlib import Path

BASE = Path("knowledge_base")

policies = {
    "upi/upi_payment_failed.txt": {
        "title": "UPI Payment Failed Policy",
        "id": "UPI-001",
        "domain": "UPI",
        "intent": "UPI_PAYMENT_FAILED",
        "issue": "Customer reports that a UPI payment failed.",
        "procedure": [
            "Verify the customer and retrieve the relevant UPI transaction.",
            "Check transaction status, amount, timestamp, and reference number.",
            "Determine whether the transaction is failed, pending, reversed, or successful.",
            "If the transaction is confirmed failed, follow the applicable retry or reversal process.",
        ],
        "resolution": "Do not ask the customer to make repeated payments until the transaction status has been verified.",
        "risk": "Medium",
        "escalation": "Escalate when transaction status is inconsistent or fraud is suspected.",
        "response": "Acknowledge the failed payment and explain that the transaction status is being verified.",
    },

    "upi/upi_payment_pending.txt": {
        "title": "UPI Payment Pending Policy",
        "id": "UPI-002",
        "domain": "UPI",
        "intent": "UPI_PAYMENT_PENDING",
        "issue": "Customer reports that a UPI transaction remains pending.",
        "procedure": [
            "Verify the customer and retrieve the UPI transaction.",
            "Check transaction timestamp, amount, reference number, and current status.",
            "Determine whether the transaction is still pending or has subsequently been completed or reversed.",
            "Follow the applicable pending-transaction resolution process.",
        ],
        "resolution": "Do not classify a pending transaction as failed or successful without verified transaction data.",
        "risk": "Medium",
        "escalation": "Escalate when the transaction remains unresolved or status information is inconsistent.",
        "response": "Acknowledge the pending transaction and confirm that its current status is being checked.",
    },

    "upi/upi_payment_reversed.txt": {
        "title": "UPI Payment Reversed Policy",
        "id": "UPI-003",
        "domain": "UPI",
        "intent": "UPI_PAYMENT_REVERSED",
        "issue": "Customer reports that a previously initiated UPI payment was reversed.",
        "procedure": [
            "Retrieve and verify the UPI transaction.",
            "Check the transaction status and reversal information.",
            "Confirm whether the amount has been returned to the customer's account.",
            "Follow the applicable reversal handling process.",
        ],
        "resolution": "Do not claim that funds have been returned until the transaction record confirms the reversal.",
        "risk": "Medium",
        "escalation": "Escalate if the transaction is reversed but the expected account credit cannot be verified.",
        "response": "Explain that the transaction status is being checked and avoid confirming a credit without transaction evidence.",
    },

    "upi/upi_debited_not_received.txt": {
        "title": "UPI Debited but Merchant Did Not Receive Funds Policy",
        "id": "UPI-004",
        "domain": "UPI",
        "intent": "UPI_DEBITED_NOT_RECEIVED",
        "issue": "Customer's account was debited but the merchant reports that the payment was not received.",
        "procedure": [
            "Retrieve and verify the UPI transaction.",
            "Check transaction status, amount, timestamp, reference number, and beneficiary information.",
            "Determine whether the transaction is successful, pending, failed, or reversed.",
            "Follow the applicable dispute or reversal process based on the verified status.",
        ],
        "resolution": "Do not ask the customer to make another payment until the original transaction status is established.",
        "risk": "High",
        "escalation": "Escalate when transaction data is inconsistent, funds cannot be traced, or fraud is suspected.",
        "response": "Acknowledge the debit and explain that the transaction status and recipient-side outcome are being investigated.",
    },

    "cards/card_payment_failed.txt": {
        "title": "Card Payment Failed Policy",
        "id": "CARD-001",
        "domain": "Cards",
        "intent": "CARD_PAYMENT_FAILED",
        "issue": "Customer reports that a card payment failed.",
        "procedure": [
            "Verify the customer and retrieve the card transaction.",
            "Check authorization status, merchant information, amount, and timestamp.",
            "Determine the reason or status of the failed authorization.",
            "Follow the applicable card troubleshooting process.",
        ],
        "resolution": "Do not advise repeated attempts when the transaction may involve a fraud or security restriction.",
        "risk": "Medium",
        "escalation": "Escalate when the failure is unexplained or security controls may be involved.",
        "response": "Acknowledge the failed card payment and explain that the transaction status is being checked.",
    },

    "cards/card_payment_dispute.txt": {
        "title": "Card Payment Dispute Policy",
        "id": "CARD-002",
        "domain": "Cards",
        "intent": "CARD_PAYMENT_DISPUTE",
        "issue": "Customer disputes a card transaction.",
        "procedure": [
            "Verify the customer and retrieve the disputed transaction.",
            "Confirm merchant, amount, date, and transaction status.",
            "Capture the customer's dispute reason.",
            "Follow the applicable card dispute process.",
        ],
        "resolution": "Do not guarantee a dispute outcome before the required investigation is completed.",
        "risk": "High",
        "escalation": "Escalate according to the applicable dispute or fraud procedure.",
        "response": "Acknowledge the disputed transaction and explain the next investigation step.",
    },

    "cards/card_payment_duplicate.txt": {
        "title": "Duplicate Card Payment Policy",
        "id": "CARD-003",
        "domain": "Cards",
        "intent": "CARD_PAYMENT_DUPLICATE",
        "issue": "Customer reports being charged more than once for the same purchase.",
        "procedure": [
            "Retrieve the relevant card transactions.",
            "Compare merchant, amount, timestamp, and authorization references.",
            "Determine whether the transactions are genuine duplicates or separate authorizations.",
            "Follow the applicable duplicate-transaction resolution process.",
        ],
        "resolution": "Do not classify transactions as duplicates solely because the amounts are identical.",
        "risk": "Medium",
        "escalation": "Escalate when transaction records cannot establish whether the charges are duplicates.",
        "response": "Acknowledge the duplicate-charge concern and explain that the transactions are being compared.",
    },

    "cards/card_payment_reversed.txt": {
        "title": "Card Payment Reversed Policy",
        "id": "CARD-004",
        "domain": "Cards",
        "intent": "CARD_PAYMENT_REVERSED",
        "issue": "Customer reports that a card transaction was reversed.",
        "procedure": [
            "Retrieve the card transaction.",
            "Verify authorization, reversal status, amount, and merchant information.",
            "Confirm whether the reversal has affected the customer's account.",
            "Follow the applicable reversal process.",
        ],
        "resolution": "Do not confirm a completed reversal without verified transaction data.",
        "risk": "Medium",
        "escalation": "Escalate when reversal status and account balance do not align.",
        "response": "Explain that the transaction and reversal status are being verified.",
    },

    "atm/atm_debited_no_cash.txt": {
        "title": "ATM Cash Dispensation — Debit Without Cash",
        "id": "ATM-001",
        "domain": "ATM",
        "intent": "ATM_DEBITED_NO_CASH",
        "issue": "ATM withdrawal was debited from the customer's account but no cash was dispensed.",
        "procedure": [
            "Verify the customer according to the applicable authentication procedure.",
            "Retrieve the ATM transaction using transaction reference, date, amount, ATM ID, and status.",
            "Check whether the transaction is successful, failed, reversed, or pending.",
            "If the account was debited and no cash was dispensed, initiate the applicable cash dispute or reversal process.",
        ],
        "resolution": "Do not promise an exact resolution timeline unless the applicable operational policy provides one.",
        "risk": "Medium to High",
        "escalation": "Escalate when transaction information is inconsistent, unavailable, or fraud is suspected.",
        "response": "Acknowledge the issue and confirm that the ATM transaction is being investigated.",
    },

    "atm/atm_partial_cash.txt": {
        "title": "ATM Partial Cash Dispensation Policy",
        "id": "ATM-002",
        "domain": "ATM",
        "intent": "ATM_PARTIAL_CASH",
        "issue": "Customer reports that the ATM dispensed less cash than the amount debited or requested.",
        "procedure": [
            "Retrieve the ATM transaction and verify requested amount.",
            "Capture the amount actually dispensed if available.",
            "Compare the transaction record with the customer's reported cash received.",
            "Follow the applicable partial-dispense dispute process.",
        ],
        "resolution": "Do not assume the missing amount without verifying transaction and ATM records.",
        "risk": "High",
        "escalation": "Escalate when the transaction and ATM records cannot establish the dispensed amount.",
        "response": "Acknowledge the partial-dispense issue and explain that transaction and ATM records are being checked.",
    },

    "atm/atm_cash_not_received.txt": {
        "title": "ATM Cash Not Received Policy",
        "id": "ATM-003",
        "domain": "ATM",
        "intent": "ATM_CASH_NOT_RECEIVED",
        "issue": "Customer reports an issue receiving cash from an ATM.",
        "procedure": [
            "Verify the customer and retrieve the relevant ATM transaction.",
            "Check transaction amount, status, ATM identifier, and timestamp.",
            "Determine whether the transaction was debited, reversed, failed, or remains unresolved.",
            "Follow the applicable ATM investigation process.",
        ],
        "resolution": "Do not confirm a refund or reversal without verified transaction evidence.",
        "risk": "High",
        "escalation": "Escalate when transaction data is unavailable, inconsistent, or indicates suspected fraud.",
        "response": "Acknowledge the cash issue and explain that the ATM transaction is being investigated.",
    },

    "account/account_blocked.txt": {
        "title": "Account Blocked Policy",
        "id": "ACC-001",
        "domain": "Account",
        "intent": "ACCOUNT_BLOCKED",
        "issue": "Customer reports that their account is blocked or restricted.",
        "procedure": [
            "Verify the customer's identity.",
            "Check the account status and applicable restriction reason.",
            "Determine whether the restriction can be resolved through a standard process.",
            "Follow the applicable account-access or compliance procedure.",
        ],
        "resolution": "Do not disclose sensitive internal risk or fraud-detection information.",
        "risk": "High",
        "escalation": "Escalate when the restriction requires compliance, fraud, or operations review.",
        "response": "Explain the available next step without revealing confidential internal controls.",
    },

    "account/login_issue.txt": {
        "title": "Login Issue Policy",
        "id": "ACC-002",
        "domain": "Account",
        "intent": "LOGIN_ISSUE",
        "issue": "Customer cannot log into the banking application or account.",
        "procedure": [
            "Verify the customer using the applicable authentication process.",
            "Identify whether the issue relates to credentials, account status, device, or application access.",
            "Guide the customer through the approved recovery process.",
            "Escalate if standard recovery does not resolve the issue.",
        ],
        "resolution": "Never request or expose passwords, OTPs, or other authentication secrets.",
        "risk": "High",
        "escalation": "Escalate suspected account takeover or unsuccessful recovery attempts.",
        "response": "Guide the customer through the approved secure account-recovery process.",
    },

    "account/mpin_issue.txt": {
        "title": "MPIN Issue Policy",
        "id": "ACC-003",
        "domain": "Account",
        "intent": "MPIN_ISSUE",
        "issue": "Customer reports an issue with their MPIN.",
        "procedure": [
            "Verify the customer using the approved authentication process.",
            "Determine whether the MPIN is forgotten, locked, or failing authentication.",
            "Guide the customer through the approved MPIN reset or unlock process.",
        ],
        "resolution": "Never request the customer's current MPIN.",
        "risk": "High",
        "escalation": "Escalate suspected account takeover or repeated authentication failures.",
        "response": "Guide the customer through the secure MPIN recovery process without requesting their MPIN.",
    },

    "refund_charges/refund_pending.txt": {
        "title": "Refund Pending Policy",
        "id": "REF-001",
        "domain": "Refunds & Charges",
        "intent": "REFUND_PENDING",
        "issue": "Customer reports that an expected refund has not yet been received.",
        "procedure": [
            "Retrieve the original transaction and refund reference if available.",
            "Verify refund status, amount, date, and originating merchant or service.",
            "Determine whether the refund has been initiated, processed, or rejected.",
            "Follow the applicable refund investigation process.",
        ],
        "resolution": "Do not state that a refund is completed unless the refund status is verified.",
        "risk": "Medium",
        "escalation": "Escalate when a confirmed refund cannot be traced to the customer's account.",
        "response": "Acknowledge the missing refund and explain that the refund status is being verified.",
    },

    "refund_charges/unexpected_charge.txt": {
        "title": "Unexpected Charge Policy",
        "id": "REF-002",
        "domain": "Refunds & Charges",
        "intent": "UNEXPECTED_CHARGE",
        "issue": "Customer reports an unexpected charge or debit.",
        "procedure": [
            "Verify the customer and retrieve the relevant transaction.",
            "Check transaction type, amount, date, merchant or charge description.",
            "Determine whether the charge is a known fee, merchant transaction, or potentially unauthorized transaction.",
            "Follow the applicable dispute or investigation process.",
        ],
        "resolution": "Do not label a transaction fraudulent without appropriate evidence and process.",
        "risk": "High",
        "escalation": "Escalate suspected unauthorized transactions according to the fraud procedure.",
        "response": "Acknowledge the unexpected charge and explain that the transaction is being investigated.",
    },

    "refund_charges/fee_dispute.txt": {
        "title": "Fee Dispute Policy",
        "id": "REF-003",
        "domain": "Refunds & Charges",
        "intent": "FEE_DISPUTE",
        "issue": "Customer disputes a bank fee or charge.",
        "procedure": [
            "Retrieve the relevant account or transaction record.",
            "Identify the fee type, amount, date, and applicable product or service.",
            "Check the applicable fee schedule or account terms.",
            "Determine whether the fee appears consistent with the applicable terms.",
        ],
        "resolution": "Do not promise a fee reversal without verifying eligibility and applicable policy.",
        "risk": "Medium",
        "escalation": "Escalate exceptions or cases where the applicable fee rule cannot be established.",
        "response": "Explain the fee being reviewed and provide the applicable next step.",
    },
}


def format_policy(data):
    procedure = "\n".join(
        f"{i}. {step}" for i, step in enumerate(data["procedure"], start=1)
    )

    return f"""MOCK BANKING POLICY — RESOLVEAI PROTOTYPE

Policy Title:
{data["title"]}

Policy ID:
{data["id"]}

Version:
1.0

Domain:
{data["domain"]}

Applicable Intent:
{data["intent"]}

Issue:
{data["issue"]}

Agent Procedure:
{procedure}

Resolution Guidance:
{data["resolution"]}

Risk Level:
{data["risk"]}

Human Escalation:
{data["escalation"]}

Agent Response Guidance:
{data["response"]}

IMPORTANT:
This document is fictional policy content created for the ResolveAI
portfolio prototype. It does not represent the actual policy of any bank.
"""


for relative_path, data in policies.items():
    file_path = BASE / relative_path
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(format_policy(data), encoding="utf-8")

print(f"Created/updated {len(policies)} mock policy documents.")