import json
import random
from pathlib import Path
from datetime import datetime, timedelta


# =========================================================
# CONFIGURATION
# =========================================================

random.seed(42)

OUTPUT_DIR = Path("mock_data")
OUTPUT_DIR.mkdir(exist_ok=True)

NUM_CUSTOMERS = 100


# =========================================================
# HELPER FUNCTIONS
# =========================================================

def save_json(filename, data):
    path = OUTPUT_DIR / filename

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

    print(f"Created {filename}: {len(data)} records")


def random_date(days_back=180):
    today = datetime(2026, 10, 3)

    date = today - timedelta(
        days=random.randint(0, days_back)
    )

    return date.strftime("%Y-%m-%d")


def random_amount(minimum=100, maximum=50000):
    return round(
        random.uniform(minimum, maximum),
        2
    )


# =========================================================
# MASTER DATA
# =========================================================

CUSTOMER_SEGMENTS = [
    "MASS",
    "MASS_AFFLUENT",
    "AFFLUENT",
    "PREMIUM"
]

CITIES = [
    "Mumbai",
    "Pune",
    "Nagpur",
    "Delhi",
    "Bengaluru",
    "Hyderabad",
    "Chennai",
    "Ahmedabad",
    "Kolkata",
    "Jaipur"
]

ACCOUNT_TYPES = [
    "SAVINGS",
    "SALARY",
    "CURRENT"
]

TRANSACTION_TYPES = [
    "UPI",
    "CARD_PAYMENT",
    "ATM_WITHDRAWAL",
    "NEFT",
    "IMPS"
]

MERCHANTS = [
    "Amazon",
    "Flipkart",
    "Swiggy",
    "Zomato",
    "BigBasket",
    "Demo Electronics",
    "Apollo Pharmacy",
    "Reliance Retail",
    "Myntra",
    "Uber"
]

RM_NAMES = [
    "Aarav Mehta",
    "Priya Sharma",
    "Rahul Kapoor",
    "Sneha Joshi",
    "Vikram Rao",
    "Ananya Singh",
    "Rohan Deshmukh",
    "Neha Patel"
]


# =========================================================
# DATA CONTAINERS
# =========================================================

customers = []
accounts = []
cards = []
upi_profiles = []
beneficiaries = []
transactions = []
refunds = []
disputes = []
service_requests = []
loans = []
emis = []
fees = []
statements = []
relationship_managers = []
offers = []


# =========================================================
# RELATIONSHIP MANAGERS
# =========================================================

for index, name in enumerate(RM_NAMES, start=1):

    relationship_managers.append({
        "rm_id": f"RM-{index:04d}",
        "name": name,
        "city": random.choice(CITIES),
        "specialization": random.choice([
            "RETAIL_BANKING",
            "AFFLUENT_BANKING",
            "DIGITAL_BANKING"
        ]),
        "active": True
    })


# =========================================================
# CUSTOMERS + PRODUCTS
# =========================================================

for i in range(1, NUM_CUSTOMERS + 1):

    customer_id = f"CUST-{1000 + i}"

    customer = {
        "customer_id": customer_id,
        "name": f"Demo Customer {i}",
        "age": random.randint(21, 65),
        "city": random.choice(CITIES),
        "customer_segment": random.choice(CUSTOMER_SEGMENTS),
        "kyc_status": random.choice([
            "FULL_KYC",
            "FULL_KYC",
            "FULL_KYC",
            "RE_KYC_PENDING"
        ]),
        "customer_status": random.choice([
            "ACTIVE",
            "ACTIVE",
            "ACTIVE",
            "ACTIVE",
            "RESTRICTED"
        ]),
        "preferred_channel": random.choice([
            "MOBILE_APP",
            "INTERNET_BANKING",
            "BRANCH",
            "PHONE_BANKING"
        ]),
        "registered_mobile": f"XXXXXX{random.randint(1000, 9999)}",
        "email": f"customer{i}@example.com",
        "rm_id": f"RM-{random.randint(1, len(RM_NAMES)):04d}",
        "created_date": random_date(1500)
    }

    customers.append(customer)

    # -----------------------------------------------------
    # ACCOUNTS
    # -----------------------------------------------------

    number_of_accounts = random.choices(
        [1, 2, 3],
        weights=[65, 30, 5]
    )[0]

    for account_number in range(number_of_accounts):

        account_id = (
            f"ACC-{i:04d}-{account_number + 1:02d}"
        )

        accounts.append({
            "account_id": account_id,
            "customer_id": customer_id,
            "account_type": random.choice(ACCOUNT_TYPES),
            "status": random.choice([
                "ACTIVE",
                "ACTIVE",
                "ACTIVE",
                "BLOCKED"
            ]),
            "available_balance": random_amount(
                5000,
                500000
            ),
            "currency": "INR",
            "opened_date": random_date(2000)
        })

    # -----------------------------------------------------
    # CARDS
    # -----------------------------------------------------

    if random.random() < 0.90:

        card_last4 = str(
            random.randint(1000, 9999)
        )

        cards.append({
            "card_id": f"CARD-{i:05d}",
            "customer_id": customer_id,
            "card_last4": card_last4,
            "card_type": random.choice([
                "DEBIT",
                "CREDIT"
            ]),
            "status": random.choice([
                "ACTIVE",
                "ACTIVE",
                "ACTIVE",
                "BLOCKED"
            ]),
            "international_enabled": random.choice([
                True,
                False
            ]),
            "online_enabled": True,
            "contactless_enabled": True,
            "credit_limit": random.choice([
                None,
                100000,
                200000,
                300000
            ])
        })

    # -----------------------------------------------------
    # UPI PROFILE
    # -----------------------------------------------------

    upi_profiles.append({
        "upi_profile_id": f"UPI-{i:05d}",
        "customer_id": customer_id,
        "vpa": f"customer{i}@upi",
        "status": random.choice([
            "ACTIVE",
            "ACTIVE",
            "ACTIVE",
            "BLOCKED"
        ]),
        "daily_limit": random.choice([
            50000,
            100000,
            200000
        ])
    })

    # -----------------------------------------------------
    # BENEFICIARIES
    # -----------------------------------------------------

    beneficiary_count = random.randint(1, 4)

    for b in range(beneficiary_count):

        beneficiaries.append({
            "beneficiary_id": (
                f"BEN-{i:04d}-{b + 1:02d}"
            ),
            "customer_id": customer_id,
            "name": f"Beneficiary {b + 1}",
            "bank_name": random.choice([
                "Demo Bank",
                "National Bank",
                "Digital Bank",
                "Unity Bank"
            ]),
            "account_last4": str(
                random.randint(1000, 9999)
            ),
            "ifsc": "DEMO0001234",
            "status": random.choice([
                "ACTIVE",
                "ACTIVE",
                "PENDING"
            ])
        })

    # -----------------------------------------------------
    # LOAN
    # -----------------------------------------------------

    if random.random() < 0.35:

        loan_id = f"LOAN-{i:05d}"

        loan_type = random.choice([
            "PERSONAL_LOAN",
            "HOME_LOAN",
            "AUTO_LOAN"
        ])

        principal = random.choice([
            200000,
            500000,
            1000000,
            2500000,
            5000000
        ])

        loans.append({
            "loan_id": loan_id,
            "customer_id": customer_id,
            "loan_type": loan_type,
            "principal_amount": principal,
            "outstanding_amount": round(
                principal * random.uniform(0.3, 0.95),
                2
            ),
            "interest_rate": random.choice([
                8.5,
                9.25,
                10.5,
                11.75,
                12.5
            ]),
            "status": random.choice([
                "ACTIVE",
                "ACTIVE",
                "ACTIVE",
                "CLOSED"
            ])
        })

        # -------------------------------------------------
        # EMI RECORDS
        # -------------------------------------------------

        for month in range(1, 7):

            emi_status = random.choices(
                [
                    "PAID",
                    "PAID",
                    "PAID",
                    "PENDING",
                    "FAILED"
                ],
                weights=[40, 25, 15, 10, 10]
            )[0]

            emis.append({
                "emi_id": (
                    f"EMI-{i:04d}-{month:02d}"
                ),
                "loan_id": loan_id,
                "customer_id": customer_id,
                "amount": random.choice([
                    8500,
                    12000,
                    18500,
                    25000,
                    42000
                ]),
                "due_date": random_date(120),
                "status": emi_status
            })

    # -----------------------------------------------------
    # OFFERS
    # -----------------------------------------------------

    for offer_number in range(
        random.randint(1, 3)
    ):

        offers.append({
            "offer_id": (
                f"OFFER-{i:04d}-{offer_number + 1:02d}"
            ),
            "customer_id": customer_id,
            "product": random.choice([
                "PERSONAL_LOAN",
                "CREDIT_CARD",
                "FD",
                "INSURANCE",
                "SAVINGS_ACCOUNT"
            ]),
            "eligible": random.choice([
                True,
                True,
                False
            ]),
            "max_amount": random.choice([
                50000,
                100000,
                250000,
                500000
            ])
        })


# =========================================================
# TRANSACTIONS
# =========================================================

transaction_counter = 1

for customer in customers:

    customer_id = customer["customer_id"]

    customer_accounts = [
        a for a in accounts
        if a["customer_id"] == customer_id
    ]

    customer_cards = [
        c for c in cards
        if c["customer_id"] == customer_id
    ]

    for _ in range(random.randint(15, 30)):

        transaction_type = random.choice(
            TRANSACTION_TYPES
        )

        transaction_id = (
            f"TXN-{transaction_counter:07d}"
        )

        transaction_counter += 1

        transaction = {
            "transaction_id": transaction_id,
            "customer_id": customer_id,
            "account_id": random.choice(
                customer_accounts
            )["account_id"],
            "type": transaction_type,
            "amount": random_amount(100, 50000),
            "currency": "INR",
            "status": random.choice([
                "SUCCESS",
                "SUCCESS",
                "SUCCESS",
                "PENDING",
                "FAILED",
                "REVERSED"
            ]),
            "date": random_date(),
            "merchant": random.choice(MERCHANTS),
            "reference_number": (
                f"REF{random.randint(10000000, 99999999)}"
            )
        }

        if transaction_type == "ATM_WITHDRAWAL":

            transaction.update({
                "atm_id": f"ATM-{random.choice(CITIES).upper()}-{random.randint(100,999)}",
                "cash_dispensed": True
            })

        elif transaction_type == "CARD_PAYMENT":

            transaction.update({
                "card_last4": (
                    random.choice(customer_cards)["card_last4"]
                    if customer_cards
                    else None
                )
            })

        elif transaction_type == "UPI":

            transaction.update({
                "upi_vpa": f"merchant{random.randint(1,100)}@upi",
                "beneficiary_credited": (
                    transaction["status"] == "SUCCESS"
                )
            })

        transactions.append(transaction)


# =========================================================
# REFUNDS
# =========================================================

for i in range(1, 101):

    transaction = random.choice(transactions)

    if transaction["type"] in [
        "CARD_PAYMENT",
        "UPI"
    ]:

        refunds.append({
            "refund_id": f"REF-{i:05d}",
            "customer_id": transaction["customer_id"],
            "transaction_id": transaction["transaction_id"],
            "amount": transaction["amount"],
            "status": random.choice([
                "INITIATED",
                "PROCESSING",
                "COMPLETED",
                "PENDING"
            ]),
            "initiated_date": random_date(60),
            "last_updated": random_date(30)
        })


# =========================================================
# DISPUTES
# =========================================================

DISPUTE_TYPES = [
    "ATM_DEBITED_NO_CASH",
    "CARD_PAYMENT_DISPUTE",
    "CARD_PAYMENT_DUPLICATE",
    "UPI_DEBITED_NOT_RECEIVED",
    "UNAUTHORIZED_TRANSACTION",
    "REFUND_NOT_RECEIVED"
]

for i in range(1, 101):

    transaction = random.choice(transactions)

    disputes.append({
        "dispute_id": f"DSP-{i:05d}",
        "customer_id": transaction["customer_id"],
        "transaction_id": transaction["transaction_id"],
        "dispute_type": random.choice(
            DISPUTE_TYPES
        ),
        "status": random.choice([
            "OPEN",
            "UNDER_REVIEW",
            "RESOLVED",
            "CLOSED"
        ]),
        "created_date": random_date(120),
        "last_updated": random_date(30)
    })


# =========================================================
# SERVICE REQUESTS
# =========================================================

REQUEST_TYPES = [
    "LOGIN_ISSUE",
    "MPIN_ISSUE",
    "ACCOUNT_BLOCKED",
    "CARD_ISSUE",
    "ADDRESS_UPDATE",
    "KYC_UPDATE",
    "TRANSACTION_DISPUTE",
    "REFUND_QUERY",
    "FEE_QUERY",
    "LOAN_QUERY"
]

for i in range(1, 201):

    customer = random.choice(customers)

    service_requests.append({
        "request_id": f"SR-{i:06d}",
        "customer_id": customer["customer_id"],
        "request_type": random.choice(
            REQUEST_TYPES
        ),
        "priority": random.choice([
            "LOW",
            "MEDIUM",
            "HIGH"
        ]),
        "status": random.choice([
            "OPEN",
            "IN_PROGRESS",
            "RESOLVED",
            "CLOSED"
        ]),
        "created_date": random_date(120),
        "sla_hours": random.choice([
            4,
            8,
            24,
            48,
            72
        ])
    })


# =========================================================
# FEES / CHARGES
# =========================================================

FEE_TYPES = [
    "ATM_FEE",
    "CARD_ANNUAL_FEE",
    "SMS_CHARGE",
    "NEFT_FEE",
    "IMPS_FEE",
    "ACCOUNT_MAINTENANCE_FEE",
    "LATE_PAYMENT_FEE"
]

for i in range(1, 200):

    customer = random.choice(customers)

    fees.append({
        "fee_id": f"FEE-{i:06d}",
        "customer_id": customer["customer_id"],
        "fee_type": random.choice(FEE_TYPES),
        "amount": random.choice([
            25,
            50,
            100,
            150,
            250,
            500
        ]),
        "date": random_date(180),
        "status": "CHARGED"
    })


# =========================================================
# STATEMENTS
# =========================================================

for customer in customers:

    customer_accounts = [
        a for a in accounts
        if a["customer_id"] == customer["customer_id"]
    ]

    for account in customer_accounts:

        statements.append({
            "statement_id": (
                f"STMT-{customer['customer_id']}-"
                f"{account['account_id']}"
            ),
            "customer_id": customer["customer_id"],
            "account_id": account["account_id"],
            "period": "2026-09",
            "opening_balance": random_amount(
                10000,
                300000
            ),
            "closing_balance": account[
                "available_balance"
            ],
            "transaction_count": random.randint(
                10,
                50
            )
        })


# =========================================================
# SAVE DATA
# =========================================================

save_json("customers.json", customers)
save_json("accounts.json", accounts)
save_json("cards.json", cards)
save_json("upi_profiles.json", upi_profiles)
save_json("beneficiaries.json", beneficiaries)
save_json("transactions.json", transactions)
save_json("refunds.json", refunds)
save_json("disputes.json", disputes)
save_json("service_requests.json", service_requests)
save_json("loans.json", loans)
save_json("emis.json", emis)
save_json("fees.json", fees)
save_json("statements.json", statements)
save_json(
    "relationship_managers.json",
    relationship_managers
)
save_json("offers.json", offers)


# =========================================================
# SUMMARY
# =========================================================

print("\n========================================")
print("MOCK BANKING SANDBOX CREATED")
print("========================================")

print(f"Customers:            {len(customers)}")
print(f"Accounts:             {len(accounts)}")
print(f"Cards:                {len(cards)}")
print(f"UPI profiles:         {len(upi_profiles)}")
print(f"Beneficiaries:        {len(beneficiaries)}")
print(f"Transactions:         {len(transactions)}")
print(f"Refunds:              {len(refunds)}")
print(f"Disputes:             {len(disputes)}")
print(f"Service requests:     {len(service_requests)}")
print(f"Loans:                {len(loans)}")
print(f"EMIs:                 {len(emis)}")
print(f"Fees:                 {len(fees)}")
print(f"Statements:           {len(statements)}")
print(f"Relationship managers:{len(relationship_managers)}")
print(f"Offers:               {len(offers)}")

print("\nAll data is synthetic.")