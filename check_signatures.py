import inspect
import mock_banking_tools

functions = [
    "get_customer_profile",
    "get_customer_accounts",
    "get_account_details",
    "get_customer_cards",
    "get_card_details",
    "get_transaction_details",
    "search_customer_transactions",
    "get_upi_profile",
    "get_customer_beneficiaries",
    "get_refund_status",
    "get_customer_refunds",
    "get_dispute_status",
    "get_customer_disputes",
    "get_customer_service_requests",
    "get_customer_loans",
    "get_customer_emi_history",
    "get_customer_fees",
    "get_customer_statements",
    "get_relationship_manager",
    "get_customer_offers",
    "get_customer_case_overview",
]

for name in functions:
    function = getattr(mock_banking_tools, name)
    print(f"{name}{inspect.signature(function)}")