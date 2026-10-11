from mock_banking_tools import (
    get_customer_profile,
    get_customer_accounts,
    search_customer_transactions,
    get_customer_loans,
    get_customer_emi_history,
    get_customer_refunds,
    get_customer_disputes,
    get_customer_offers,
    get_customer_case_overview,
)


# ---------------------------------------------------------
# CUSTOMER WE ARE TESTING
# ---------------------------------------------------------

CUSTOMER_ID = "CUST-1001"


# ---------------------------------------------------------
# 1. CUSTOMER PROFILE
# ---------------------------------------------------------

print("\n===== CUSTOMER PROFILE =====")

print(
    get_customer_profile(CUSTOMER_ID)
)


# ---------------------------------------------------------
# 2. ACCOUNTS
# ---------------------------------------------------------

print("\n===== ACCOUNTS =====")

print(
    get_customer_accounts(CUSTOMER_ID)
)


# ---------------------------------------------------------
# 3. TRANSACTIONS
# ---------------------------------------------------------

print("\n===== TRANSACTIONS =====")

print(
    search_customer_transactions(
        CUSTOMER_ID
    )
)


# ---------------------------------------------------------
# 4. LOANS
# ---------------------------------------------------------

print("\n===== LOANS =====")

print(
    get_customer_loans(
        CUSTOMER_ID
    )
)


# ---------------------------------------------------------
# 5. EMI HISTORY
# ---------------------------------------------------------

print("\n===== EMI HISTORY =====")

print(
    get_customer_emi_history(
        CUSTOMER_ID
    )
)


# ---------------------------------------------------------
# 6. REFUNDS
# ---------------------------------------------------------

print("\n===== REFUNDS =====")

print(
    get_customer_refunds(
        CUSTOMER_ID
    )
)


# ---------------------------------------------------------
# 7. DISPUTES
# ---------------------------------------------------------

print("\n===== DISPUTES =====")

print(
    get_customer_disputes(
        CUSTOMER_ID
    )
)


# ---------------------------------------------------------
# 8. OFFERS
# ---------------------------------------------------------

print("\n===== OFFERS =====")

print(
    get_customer_offers(
        CUSTOMER_ID
    )
)


# ---------------------------------------------------------
# 9. COMPOSITE CUSTOMER CASE OVERVIEW
# ---------------------------------------------------------

print("\n===== CUSTOMER CASE OVERVIEW =====")

overview = get_customer_case_overview(
    CUSTOMER_ID
)

print(overview)