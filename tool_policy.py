from tool_registry import TOOL_DEFINITIONS


# ============================================================
# TOOL ACCESS POLICY
# ============================================================
#
# This defines which customer-data tools the AI investigation
# agent is allowed to use for each investigation type.
#
# IMPORTANT:
# The LLM does NOT decide which tools it has access to.
# Our application controls that through this policy.
#
# This is a prototype permission layer and should be extended
# with authentication, authorization, PII controls and audit
# logging in a production banking environment.
# ============================================================


TOOL_ACCESS_POLICY = {

    # --------------------------------------------------------
    # ACCOUNT
    # --------------------------------------------------------
    # Examples:
    # - MPIN issue
    # - Login problem
    # - Account blocked
    # - Account access issue
    # --------------------------------------------------------
    "account": [
        "get_customer_profile",
        "get_customer_accounts",
        "get_account_details",
        "get_customer_cards",
        "get_customer_service_requests",
        "get_customer_case_overview",
    ],


    # --------------------------------------------------------
    # TRANSACTION
    # --------------------------------------------------------
    # General transaction investigation where the customer
    # has referred to a specific transaction or payment.
    # --------------------------------------------------------
    "transaction": [
        "get_customer_profile",
        "search_customer_transactions",
        "get_transaction_details",
        "get_customer_refunds",
        "get_customer_disputes",
        "get_customer_case_overview",
    ],


    # --------------------------------------------------------
    # UPI
    # --------------------------------------------------------
    # Examples:
    # - UPI payment pending
    # - UPI debited but beneficiary not received
    # - UPI payment reversed
    # --------------------------------------------------------
    "upi": [
        "get_customer_profile",
        "search_customer_transactions",
        "get_transaction_details",
        "get_upi_profile",
        "get_customer_refunds",
        "get_customer_disputes",
        "get_customer_case_overview",
    ],


    # --------------------------------------------------------
    # CARD
    # --------------------------------------------------------
    # Examples:
    # - Card payment declined
    # - Duplicate card payment
    # - Card payment reversed
    # - Card payment dispute
    # --------------------------------------------------------
    "card": [
        "get_customer_profile",
        "get_customer_cards",
        "get_card_details",
        "search_customer_transactions",
        "get_transaction_details",
        "get_customer_disputes",
        "get_customer_refunds",
        "get_customer_case_overview",
    ],


    # --------------------------------------------------------
    # REFUND
    # --------------------------------------------------------
    # Examples:
    # - Refund pending
    # - Refund not received
    # - Refund status enquiry
    # --------------------------------------------------------
    "refund": [
        "get_customer_profile",
        "search_customer_transactions",
        "get_transaction_details",
        "get_customer_refunds",
        "get_refund_status",
        "get_customer_disputes",
        "get_customer_case_overview",
    ],


    # --------------------------------------------------------
    # DISPUTE
    # --------------------------------------------------------
    # Examples:
    # - Customer raised a dispute
    # - Dispute status
    # - Card/transaction dispute
    # --------------------------------------------------------
    "dispute": [
        "get_customer_profile",
        "search_customer_transactions",
        "get_transaction_details",
        "get_customer_disputes",
        "get_dispute_status",
        "get_customer_refunds",
        "get_customer_case_overview",
    ],


    # --------------------------------------------------------
    # ATM
    # --------------------------------------------------------
    # Examples:
    # - Cash not received
    # - Cash partially received
    # - Account debited but ATM didn't dispense cash
    # --------------------------------------------------------
    "atm": [
        "get_customer_profile",
        "search_customer_transactions",
        "get_transaction_details",
        "get_customer_disputes",
        "get_customer_refunds",
        "get_customer_case_overview",
    ],


    # --------------------------------------------------------
    # LOAN
    # --------------------------------------------------------
    # Examples:
    # - Loan details
    # - Loan status
    # - Outstanding loan information
    # --------------------------------------------------------
    "loan": [
        "get_customer_profile",
        "get_customer_loans",
        "get_customer_accounts",
        "get_account_details",
        "get_customer_emi_history",
        "get_customer_case_overview",
    ],


    # --------------------------------------------------------
    # EMI
    # --------------------------------------------------------
    # Examples:
    # - EMI history
    # - EMI payment issue
    # - EMI status
    # --------------------------------------------------------
    "emi": [
        "get_customer_profile",
        "get_customer_loans",
        "get_customer_emi_history",
        "get_customer_accounts",
        "get_customer_case_overview",
    ],


    # --------------------------------------------------------
    # FEES
    # --------------------------------------------------------
    # Examples:
    # - Unexpected fee
    # - Account charges
    # - Fee dispute
    # --------------------------------------------------------
    "fees": [
        "get_customer_profile",
        "get_customer_fees",
        "get_customer_accounts",
        "get_customer_case_overview",
    ],


    # --------------------------------------------------------
    # STATEMENT
    # --------------------------------------------------------
    # Examples:
    # - Statement issue
    # - Missing statement
    # - Statement-related customer request
    # --------------------------------------------------------
    "statement": [
        "get_customer_profile",
        "get_customer_statements",
        "get_customer_accounts",
        "get_customer_case_overview",
    ],


    # --------------------------------------------------------
    # BENEFICIARY
    # --------------------------------------------------------
    # Examples:
    # - Beneficiary issue
    # - Beneficiary not visible
    # - Beneficiary-related transaction issue
    # --------------------------------------------------------
    "beneficiary": [
        "get_customer_profile",
        "get_customer_beneficiaries",
        "get_customer_accounts",
        "search_customer_transactions",
        "get_customer_case_overview",
    ],


    # --------------------------------------------------------
    # SERVICE REQUEST
    # --------------------------------------------------------
    # Examples:
    # - Existing service request status
    # - Complaint/request follow-up
    # --------------------------------------------------------
    "service_request": [
        "get_customer_profile",
        "get_customer_service_requests",
        "get_customer_case_overview",
    ],


    # --------------------------------------------------------
    # NONE
    # --------------------------------------------------------
    # No customer investigation required.
    #
    # Example:
    # "How do I set my MPIN?"
    # --------------------------------------------------------
    "none": [],
}


def get_allowed_tool_definitions(investigation_type):
    """
    Return Gemini tool definitions allowed for the
    specified investigation type.
    """

    allowed_tools = TOOL_ACCESS_POLICY.get(
        investigation_type,
        []
    )

    return [
        tool
        for tool in TOOL_DEFINITIONS
        if tool["name"] in allowed_tools
    ]