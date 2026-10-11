"""
ResolveAI Mock Banking Tool Layer

This file provides functions that ResolveAI can use
to retrieve information from the synthetic banking dataset.

The actual fictional banking data is stored separately
inside the mock_data/ folder.

In production, these functions could be replaced by
authenticated APIs connected to real banking systems.
"""

import json
from pathlib import Path


# =========================================================
# DATA LOCATION
# =========================================================

DATA_DIR = Path("mock_data")


# =========================================================
# GENERIC DATA LOADER
# =========================================================

def load_data(filename):
    """
    Load one JSON dataset from the mock banking sandbox.
    """

    file_path = DATA_DIR / filename

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


# =========================================================
# TOOL 1 — CUSTOMER PROFILE
# =========================================================

def get_customer_profile(customer_id: str):
    """
    Retrieve a customer's profile, KYC status,
    segment and relationship manager.
    """

    customers = load_data("customers.json")

    for customer in customers:

        if customer["customer_id"] == customer_id:
            return customer

    return {
        "error": "Customer not found",
        "customer_id": customer_id
    }


# =========================================================
# TOOL 2 — CUSTOMER ACCOUNTS
# =========================================================

def get_customer_accounts(customer_id: str):
    """
    Retrieve all accounts belonging to a customer.
    """

    accounts = load_data("accounts.json")

    results = [
        account
        for account in accounts
        if account["customer_id"] == customer_id
    ]

    return {
        "customer_id": customer_id,
        "count": len(results),
        "accounts": results
    }


# =========================================================
# TOOL 3 — ACCOUNT DETAILS
# =========================================================

def get_account_details(account_id: str):
    """
    Retrieve details for one specific account.
    """

    accounts = load_data("accounts.json")

    for account in accounts:

        if account["account_id"] == account_id:
            return account

    return {
        "error": "Account not found",
        "account_id": account_id
    }


# =========================================================
# TOOL 4 — CUSTOMER CARDS
# =========================================================

def get_customer_cards(customer_id: str):
    """
    Retrieve all cards associated with a customer.
    """

    cards = load_data("cards.json")

    results = [
        card
        for card in cards
        if card["customer_id"] == customer_id
    ]

    return {
        "customer_id": customer_id,
        "count": len(results),
        "cards": results
    }


# =========================================================
# TOOL 5 — CARD DETAILS
# =========================================================

def get_card_details(card_last4: str):
    """
    Retrieve non-sensitive information about a card
    using its last four digits.
    """

    cards = load_data("cards.json")

    results = [
        card
        for card in cards
        if card["card_last4"] == card_last4
    ]

    if not results:

        return {
            "error": "Card not found",
            "card_last4": card_last4
        }

    return results[0]


# =========================================================
# TOOL 6 — TRANSACTION DETAILS
# =========================================================

def get_transaction_details(transaction_id: str):
    """
    Retrieve one specific transaction.
    """

    transactions = load_data(
        "transactions.json"
    )

    for transaction in transactions:

        if transaction["transaction_id"] == transaction_id:
            return transaction

    return {
        "error": "Transaction not found",
        "transaction_id": transaction_id
    }


# =========================================================
# TOOL 7 — SEARCH CUSTOMER TRANSACTIONS
# =========================================================

def search_customer_transactions(
    customer_id: str,
    transaction_type: str = "",
    status: str = "",
    merchant: str = "",
    amount: float = None,
    transaction_date: str = "",
    reference_number: str = "",
    card_last4: str = "",
    transaction_id: str = "",
    upi_vpa: str = ""
):
    """
    Search transactions belonging to a customer.

    The tool supports broad searches as well as
    increasingly specific transaction identification.

    Optional filters:

    transaction_type:
        UPI
        CARD_PAYMENT
        ATM_WITHDRAWAL
        NEFT
        IMPS

    status:
        SUCCESS
        PENDING
        FAILED
        REVERSED

    merchant:
        Merchant name or partial merchant name.

    amount:
        Exact transaction amount.

    transaction_date:
        Exact transaction date in YYYY-MM-DD format.

    reference_number:
        Exact bank transaction reference number.

    card_last4:
        Last four digits of the card.

    transaction_id:
        Exact transaction ID.

    upi_vpa:
        UPI beneficiary VPA.
    """

    transactions = load_data(
        "transactions.json"
    )

    results = []

    normalized_type = transaction_type.strip().upper()
    normalized_status = status.strip().upper()
    normalized_merchant = merchant.strip().lower()
    normalized_reference = reference_number.strip().lower()
    normalized_card_last4 = card_last4.strip()
    normalized_transaction_id = transaction_id.strip().lower()
    normalized_upi_vpa = upi_vpa.strip().lower()
    normalized_date = transaction_date.strip()

    for transaction in transactions:

        # -------------------------------------------------
        # Mandatory customer boundary
        # -------------------------------------------------

        if transaction["customer_id"] != customer_id:
            continue

        # -------------------------------------------------
        # Existing filters
        # -------------------------------------------------

        if normalized_type:

            if transaction["type"].upper() != normalized_type:
                continue

        if normalized_status:

            if transaction["status"].upper() != normalized_status:
                continue

        # -------------------------------------------------
        # Transaction ID
        # -------------------------------------------------

        if normalized_transaction_id:

            if transaction["transaction_id"].lower() != normalized_transaction_id:
                continue

        # -------------------------------------------------
        # Merchant
        # -------------------------------------------------

        if normalized_merchant:

            transaction_merchant = str(
                transaction.get("merchant", "")
            ).lower()

            if normalized_merchant not in transaction_merchant:
                continue

        # -------------------------------------------------
        # Amount
        # -------------------------------------------------

        if amount is not None:

            transaction_amount = transaction.get(
                "amount"
            )

            if transaction_amount is None:
                continue

            if float(transaction_amount) != float(amount):
                continue

        # -------------------------------------------------
        # Transaction date
        # -------------------------------------------------

        if normalized_date:

            if transaction.get("date", "") != normalized_date:
                continue

        # -------------------------------------------------
        # Reference number
        # -------------------------------------------------

        if normalized_reference:

            transaction_reference = str(
                transaction.get("reference_number", "")
            ).lower()

            if transaction_reference != normalized_reference:
                continue

        # -------------------------------------------------
        # Card last four
        # -------------------------------------------------

        if normalized_card_last4:

            if transaction.get("card_last4", "") != normalized_card_last4:
                continue

        # -------------------------------------------------
        # UPI VPA
        # -------------------------------------------------

        if normalized_upi_vpa:

            transaction_vpa = str(
                transaction.get("upi_vpa", "")
            ).lower()

            if transaction_vpa != normalized_upi_vpa:
                continue

        results.append(transaction)

    return {
        "customer_id": customer_id,
        "count": len(results),
        "applied_filters": {
            "transaction_type": transaction_type,
            "status": status,
            "merchant": merchant,
            "amount": amount,
            "transaction_date": transaction_date,
            "reference_number": reference_number,
            "card_last4": card_last4,
            "transaction_id": transaction_id,
            "upi_vpa": upi_vpa
        },
        "transactions": results
    }


# =========================================================
# TOOL 8 — UPI PROFILE
# =========================================================

def get_upi_profile(customer_id: str):
    """
    Retrieve the customer's UPI profile.
    """

    profiles = load_data(
        "upi_profiles.json"
    )

    results = [
        profile
        for profile in profiles
        if profile["customer_id"] == customer_id
    ]

    if not results:

        return {
            "error": "UPI profile not found",
            "customer_id": customer_id
        }

    return results[0]


# =========================================================
# TOOL 9 — BENEFICIARIES
# =========================================================

def get_customer_beneficiaries(
    customer_id: str
):
    """
    Retrieve beneficiaries registered by
    the customer.
    """

    beneficiaries = load_data(
        "beneficiaries.json"
    )

    results = [
        beneficiary
        for beneficiary in beneficiaries
        if beneficiary["customer_id"] == customer_id
    ]

    return {
        "customer_id": customer_id,
        "count": len(results),
        "beneficiaries": results
    }


# =========================================================
# TOOL 10 — REFUND STATUS
# =========================================================

def get_refund_status(refund_id: str):
    """
    Retrieve details for one refund.
    """

    refunds = load_data(
        "refunds.json"
    )

    for refund in refunds:

        if refund["refund_id"] == refund_id:
            return refund

    return {
        "error": "Refund not found",
        "refund_id": refund_id
    }


# =========================================================
# TOOL 11 — CUSTOMER REFUNDS
# =========================================================

def get_customer_refunds(
    customer_id: str
):
    """
    Retrieve all refunds associated with
    a customer.
    """

    refunds = load_data(
        "refunds.json"
    )

    results = [
        refund
        for refund in refunds
        if refund["customer_id"] == customer_id
    ]

    return {
        "customer_id": customer_id,
        "count": len(results),
        "refunds": results
    }


# =========================================================
# TOOL 12 — DISPUTE STATUS
# =========================================================

def get_dispute_status(dispute_id: str):
    """
    Retrieve one dispute and its current status.
    """

    disputes = load_data(
        "disputes.json"
    )

    for dispute in disputes:

        if dispute["dispute_id"] == dispute_id:
            return dispute

    return {
        "error": "Dispute not found",
        "dispute_id": dispute_id
    }


# =========================================================
# TOOL 13 — CUSTOMER DISPUTES
# =========================================================

def get_customer_disputes(
    customer_id: str
):
    """
    Retrieve all disputes associated with
    a customer.
    """

    disputes = load_data(
        "disputes.json"
    )

    results = [
        dispute
        for dispute in disputes
        if dispute["customer_id"] == customer_id
    ]

    return {
        "customer_id": customer_id,
        "count": len(results),
        "disputes": results
    }


# =========================================================
# TOOL 14 — SERVICE REQUESTS
# =========================================================

def get_customer_service_requests(
    customer_id: str
):
    """
    Retrieve previous customer service requests.
    """

    requests = load_data(
        "service_requests.json"
    )

    results = [
        request
        for request in requests
        if request["customer_id"] == customer_id
    ]

    return {
        "customer_id": customer_id,
        "count": len(results),
        "service_requests": results
    }


# =========================================================
# TOOL 15 — LOANS
# =========================================================

def get_customer_loans(
    customer_id: str
):
    """
    Retrieve all loans belonging to a customer.
    """

    loans = load_data(
        "loans.json"
    )

    results = [
        loan
        for loan in loans
        if loan["customer_id"] == customer_id
    ]

    return {
        "customer_id": customer_id,
        "count": len(results),
        "loans": results
    }


# =========================================================
# TOOL 16 — EMI HISTORY
# =========================================================

def get_customer_emi_history(
    customer_id: str
):
    """
    Retrieve EMI payment history for a customer.
    """

    emis = load_data(
        "emis.json"
    )

    results = [
        emi
        for emi in emis
        if emi["customer_id"] == customer_id
    ]

    return {
        "customer_id": customer_id,
        "count": len(results),
        "emis": results
    }


# =========================================================
# TOOL 17 — FEES / CHARGES
# =========================================================

def get_customer_fees(
    customer_id: str
):
    """
    Retrieve fees and charges associated
    with a customer.
    """

    fees = load_data(
        "fees.json"
    )

    results = [
        fee
        for fee in fees
        if fee["customer_id"] == customer_id
    ]

    return {
        "customer_id": customer_id,
        "count": len(results),
        "fees": results
    }


# =========================================================
# TOOL 18 — STATEMENTS
# =========================================================

def get_customer_statements(
    customer_id: str
):
    """
    Retrieve available account statements.
    """

    statements = load_data(
        "statements.json"
    )

    results = [
        statement
        for statement in statements
        if statement["customer_id"] == customer_id
    ]

    return {
        "customer_id": customer_id,
        "count": len(results),
        "statements": results
    }


# =========================================================
# TOOL 19 — RELATIONSHIP MANAGER
# =========================================================

def get_relationship_manager(
    customer_id: str
):
    """
    Retrieve the relationship manager assigned
    to the customer.
    """

    customers = load_data(
        "customers.json"
    )

    managers = load_data(
        "relationship_managers.json"
    )

    customer = None

    for item in customers:

        if item["customer_id"] == customer_id:
            customer = item
            break

    if not customer:

        return {
            "error": "Customer not found"
        }

    rm_id = customer["rm_id"]

    for manager in managers:

        if manager["rm_id"] == rm_id:
            return manager

    return {
        "error": "Relationship manager not found",
        "rm_id": rm_id
    }


# =========================================================
# TOOL 20 — OFFERS / ELIGIBILITY
# =========================================================

def get_customer_offers(
    customer_id: str
):
    """
    Retrieve offers and eligibility information
    for a customer.
    """

    offers = load_data(
        "offers.json"
    )

    results = [
        offer
        for offer in offers
        if offer["customer_id"] == customer_id
    ]

    return {
        "customer_id": customer_id,
        "count": len(results),
        "offers": results
    }


# =========================================================
# TOOL 21 — CUSTOMER CASE OVERVIEW
# =========================================================

def get_customer_case_overview(
    customer_id: str
):
    """
    Retrieve a compact support-oriented overview
    of a customer's profile and related information.

    This combines multiple underlying data sources.
    """

    return {
        "customer": get_customer_profile(
            customer_id
        ),

        "accounts": get_customer_accounts(
            customer_id
        ),

        "cards": get_customer_cards(
            customer_id
        ),

        "upi": get_upi_profile(
            customer_id
        ),

        "recent_transactions":
            search_customer_transactions(
                customer_id
            ),

        "refunds": get_customer_refunds(
            customer_id
        ),

        "disputes": get_customer_disputes(
            customer_id
        ),

        "service_requests":
            get_customer_service_requests(
                customer_id
            )
    }