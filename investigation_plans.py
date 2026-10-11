# ============================================================
# INVESTIGATION PLANS
# ============================================================
#
# This file defines WHAT evidence the AI investigation agent
# should collect for each investigation type.
#
# tool_policy.py answers:
#   "Which tools can the agent use?"
#
# investigation_plans.py answers:
#   "What should the agent verify?"
#
# This separation gives us:
#   1. Controlled tool access
#   2. Structured investigation objectives
#   3. More reliable AI reasoning
#   4. Better auditability
# ============================================================


INVESTIGATION_PLANS = {

    # --------------------------------------------------------
    # ACCOUNT
    # --------------------------------------------------------
    "account": {
        "objective": (
            "Investigate the customer's account or account-access "
            "issue and determine the relevant customer-specific "
            "facts needed to explain or resolve the issue."
        ),
        "required_evidence": [
            "Customer/account status",
            "Relevant account details",
            "Relevant cards or instruments if connected to the issue",
            "Existing service requests related to the issue",
            "Relevant case information",
        ],
    },


    # --------------------------------------------------------
    # TRANSACTION
    # --------------------------------------------------------
    "transaction": {
        "objective": (
            "Investigate the customer's specific transaction and "
            "determine its actual status and relevant transaction facts."
        ),
        "required_evidence": [
            "Relevant transaction identified",
            "Transaction status",
            "Transaction amount",
            "Transaction timestamp",
            "Transaction/reference identifier",
            "Related refund information if relevant",
            "Related dispute information if relevant",
            "Relevant case information",
        ],
    },


    # --------------------------------------------------------
    # UPI
    # --------------------------------------------------------
    "upi": {
        "objective": (
            "Investigate the customer's UPI issue and determine "
            "the actual transaction and UPI status using customer data."
        ),
        "required_evidence": [
            "Relevant UPI transaction identified",
            "Transaction status",
            "Transaction amount",
            "Transaction timestamp",
            "Transaction/reference identifier",
            "Whether the beneficiary was credited, when available",
            "UPI/customer profile status",
            "Related refund information if relevant",
            "Related dispute information if relevant",
            "Relevant case information",
        ],
    },


    # --------------------------------------------------------
    # CARD
    # --------------------------------------------------------
    "card": {
        "objective": (
            "Investigate the customer's card-related issue and "
            "determine the relevant card and transaction facts."
        ),
        "required_evidence": [
            "Relevant card identified",
            "Card status",
            "Relevant transaction identified",
            "Transaction status",
            "Transaction amount",
            "Transaction timestamp",
            "Transaction/reference identifier",
            "Related dispute information if relevant",
            "Related refund information if relevant",
            "Relevant case information",
        ],
    },


    # --------------------------------------------------------
    # REFUND
    # --------------------------------------------------------
    "refund": {
        "objective": (
            "Investigate the customer's refund issue and verify "
            "the underlying transaction and current refund status."
        ),
        "required_evidence": [
            "Relevant transaction identified",
            "Transaction status",
            "Refund record identified",
            "Refund status",
            "Refund amount",
            "Refund date or expected timing when available",
            "Refund/reference identifier",
            "Related dispute information if relevant",
            "Relevant case information",
        ],
    },


    # --------------------------------------------------------
    # DISPUTE
    # --------------------------------------------------------
    "dispute": {
        "objective": (
            "Investigate the customer's dispute and determine "
            "the current dispute status and relevant underlying "
            "transaction information."
        ),
        "required_evidence": [
            "Relevant transaction identified if applicable",
            "Transaction status",
            "Transaction amount",
            "Transaction timestamp",
            "Transaction/reference identifier",
            "Relevant dispute identified",
            "Dispute status",
            "Dispute/reference identifier",
            "Related refund information if relevant",
            "Relevant case information",
        ],
    },


    # --------------------------------------------------------
    # ATM
    # --------------------------------------------------------
    "atm": {
        "objective": (
            "Investigate the customer's ATM transaction issue and "
            "determine what happened to the relevant cash withdrawal."
        ),
        "required_evidence": [
            "Relevant ATM transaction identified",
            "Transaction status",
            "Withdrawal amount",
            "Transaction timestamp",
            "Transaction/reference identifier",
            "Whether cash was dispensed when available",
            "Related dispute information if relevant",
            "Related refund information if relevant",
            "Relevant case information",
        ],
    },


    # --------------------------------------------------------
    # LOAN
    # --------------------------------------------------------
    "loan": {
        "objective": (
            "Investigate the customer's loan-related query and "
            "retrieve the relevant loan and repayment information."
        ),
        "required_evidence": [
            "Relevant loan identified",
            "Loan status",
            "Relevant loan details",
            "Outstanding information when available",
            "Related EMI history when relevant",
            "Relevant account information when needed",
            "Relevant case information",
        ],
    },


    # --------------------------------------------------------
    # EMI
    # --------------------------------------------------------
    "emi": {
        "objective": (
            "Investigate the customer's EMI-related issue and "
            "verify the relevant loan and EMI history."
        ),
        "required_evidence": [
            "Relevant loan identified",
            "Loan status",
            "Relevant EMI record or history",
            "EMI status",
            "Relevant EMI amount or payment information",
            "Relevant account information when needed",
            "Relevant case information",
        ],
    },


    # --------------------------------------------------------
    # FEES
    # --------------------------------------------------------
    "fees": {
        "objective": (
            "Investigate the customer's fee or charge-related "
            "issue and identify the relevant customer-specific fee."
        ),
        "required_evidence": [
            "Relevant fee or charge identified",
            "Fee amount",
            "Fee type or description",
            "Relevant account information",
            "Relevant case information",
        ],
    },


    # --------------------------------------------------------
    # STATEMENT
    # --------------------------------------------------------
    "statement": {
        "objective": (
            "Investigate the customer's statement-related issue "
            "and verify the relevant statement information."
        ),
        "required_evidence": [
            "Relevant account identified",
            "Relevant statement record",
            "Statement period or date when available",
            "Statement status or availability",
            "Relevant case information",
        ],
    },


    # --------------------------------------------------------
    # BENEFICIARY
    # --------------------------------------------------------
    "beneficiary": {
        "objective": (
            "Investigate the customer's beneficiary-related issue "
            "and determine the relevant beneficiary and transaction "
            "information."
        ),
        "required_evidence": [
            "Relevant beneficiary identified",
            "Beneficiary status or details",
            "Relevant account information",
            "Related transaction information if applicable",
            "Relevant case information",
        ],
    },


    # --------------------------------------------------------
    # SERVICE REQUEST
    # --------------------------------------------------------
    "service_request": {
        "objective": (
            "Investigate the customer's existing service request "
            "and determine its current status and relevant details."
        ),
        "required_evidence": [
            "Relevant service request identified",
            "Service request type",
            "Current service request status",
            "Relevant dates or timestamps when available",
            "Relevant customer/account information",
            "Relevant case information",
        ],
    },


    # --------------------------------------------------------
    # NONE
    # --------------------------------------------------------
    "none": {
        "objective": (
            "No customer-specific investigation is required."
        ),
        "required_evidence": [],
    },
}


def get_investigation_plan(investigation_type):
    """
    Return the investigation plan for the requested type.

    If an unknown investigation type is supplied, fall back
    to the 'none' plan rather than creating an unrestricted
    investigation.
    """

    return INVESTIGATION_PLANS.get(
        investigation_type,
        INVESTIGATION_PLANS["none"]
    )