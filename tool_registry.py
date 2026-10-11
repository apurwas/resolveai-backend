from mock_banking_tools import (
    get_customer_profile,
    get_customer_accounts,
    get_customer_cards,
    get_transaction_details,
    search_customer_transactions,
    get_refund_status,
    get_customer_refunds,
    get_dispute_status,
    get_customer_disputes,
    get_customer_service_requests,
    get_customer_loans,
    get_customer_emi_history,
    get_customer_fees,
    get_customer_statements,
    get_relationship_manager,
    get_customer_offers,
    get_customer_case_overview,
    get_account_details,
    get_card_details,
    get_upi_profile,
    get_customer_beneficiaries,
)


# =========================================================
# PYTHON FUNCTION REGISTRY
# =========================================================

TOOL_FUNCTIONS = {
    "get_customer_profile": get_customer_profile,
    "get_customer_accounts": get_customer_accounts,
    "get_customer_cards": get_customer_cards,
    "get_transaction_details": get_transaction_details,
    "search_customer_transactions": search_customer_transactions,
    "get_refund_status": get_refund_status,
    "get_customer_refunds": get_customer_refunds,
    "get_dispute_status": get_dispute_status,
    "get_customer_disputes": get_customer_disputes,
    "get_customer_service_requests": get_customer_service_requests,
    "get_customer_loans": get_customer_loans,
    "get_customer_emi_history": get_customer_emi_history,
    "get_customer_fees": get_customer_fees,
    "get_customer_statements": get_customer_statements,
    "get_relationship_manager": get_relationship_manager,
    "get_customer_offers": get_customer_offers,
    "get_customer_case_overview": get_customer_case_overview,
    "get_account_details": get_account_details,
    "get_card_details": get_card_details,
    "get_upi_profile": get_upi_profile,
    "get_customer_beneficiaries": get_customer_beneficiaries,
}


# =========================================================
# GEMINI TOOL DEFINITIONS
# =========================================================

TOOL_DEFINITIONS = [

    {
        "name": "get_customer_profile",
        "description": "Retrieve the customer's basic profile information.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_id": {
                    "type": "string",
                    "description": "Unique customer ID."
                }
            },
            "required": ["customer_id"]
        }
    },

    {
        "name": "get_customer_accounts",
        "description": "Retrieve all bank accounts associated with the customer.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_id": {
                    "type": "string",
                    "description": "Unique customer ID."
                }
            },
            "required": ["customer_id"]
        }
    },

    {
        "name": "get_account_details",
        "description": "Retrieve detailed information about a specific bank account.",
        "parameters": {
            "type": "object",
            "properties": {
                "account_id": {
                    "type": "string",
                    "description": "Unique account ID."
                }
            },
            "required": ["account_id"]
        }
    },

    {
        "name": "get_customer_cards",
        "description": "Retrieve cards associated with the customer.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_id": {
                    "type": "string",
                    "description": "Unique customer ID."
                }
            },
            "required": ["customer_id"]
        }
    },

    {
        "name": "get_card_details",
        "description": "Retrieve details about a specific card using its last four digits.",
        "parameters": {
            "type": "object",
            "properties": {
                "card_last4": {
                    "type": "string",
                    "description": "Last four digits of the card."
                }
            },
            "required": ["card_last4"]
        }
    },

    {
        "name": "get_transaction_details",
        "description": "Retrieve detailed information about a specific banking transaction.",
        "parameters": {
            "type": "object",
            "properties": {
                "transaction_id": {
                    "type": "string",
                    "description": "Unique transaction ID."
                }
            },
            "required": ["transaction_id"]
        }
    },

    {
        "name": "search_customer_transactions",
        "description": (
            "Search the customer's transactions using optional "
            "transaction type, status, merchant, amount, date, "
            "reference number, card last four digits, transaction ID, "
            "or UPI VPA. Use multiple clues when available to identify "
            "the specific transaction. If multiple transactions remain, "
            "do not guess."
        ),
        "parameters": {
            "type": "object",
            "properties": {

                "customer_id": {
                    "type": "string",
                    "description": "Unique customer ID."
                },

                "transaction_type": {
                    "type": "string",
                    "description": (
                        "Optional transaction type such as "
                        "UPI, CARD_PAYMENT, ATM_WITHDRAWAL, NEFT or IMPS."
                    )
                },

                "status": {
                    "type": "string",
                    "description": (
                        "Optional transaction status such as "
                        "SUCCESS, PENDING, FAILED or REVERSED."
                    )
                },

                "merchant": {
                    "type": "string",
                    "description": (
                        "Optional merchant name or partial merchant name."
                    )
                },

                "amount": {
                    "type": "number",
                    "description": (
                        "Optional exact transaction amount in INR."
                    )
                },

                "transaction_date": {
                    "type": "string",
                    "description": (
                        "Optional exact transaction date in YYYY-MM-DD format."
                    )
                },

                "reference_number": {
                    "type": "string",
                    "description": (
                        "Optional exact bank transaction reference number."
                    )
                },

                "card_last4": {
                    "type": "string",
                    "description": (
                        "Optional last four digits of the card."
                    )
                },

                "transaction_id": {
                    "type": "string",
                    "description": (
                        "Optional exact transaction ID."
                    )
                },

                "upi_vpa": {
                    "type": "string",
                    "description": (
                        "Optional UPI beneficiary VPA."
                    )
                }
            },
            "required": ["customer_id"]
        }
    },

    {
        "name": "get_upi_profile",
        "description": "Retrieve the customer's UPI profile and UPI-related information.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_id": {
                    "type": "string",
                    "description": "Unique customer ID."
                }
            },
            "required": ["customer_id"]
        }
    },

    {
        "name": "get_customer_beneficiaries",
        "description": "Retrieve beneficiaries registered by the customer.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_id": {
                    "type": "string",
                    "description": "Unique customer ID."
                }
            },
            "required": ["customer_id"]
        }
    },

    {
        "name": "get_refund_status",
        "description": "Retrieve the current status of a specific refund.",
        "parameters": {
            "type": "object",
            "properties": {
                "refund_id": {
                    "type": "string",
                    "description": "Unique refund ID."
                }
            },
            "required": ["refund_id"]
        }
    },

    {
        "name": "get_customer_refunds",
        "description": "Retrieve refund records associated with the customer.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_id": {
                    "type": "string",
                    "description": "Unique customer ID."
                }
            },
            "required": ["customer_id"]
        }
    },

    {
        "name": "get_dispute_status",
        "description": "Retrieve the current status of a specific transaction dispute.",
        "parameters": {
            "type": "object",
            "properties": {
                "dispute_id": {
                    "type": "string",
                    "description": "Unique dispute ID."
                }
            },
            "required": ["dispute_id"]
        }
    },

    {
        "name": "get_customer_disputes",
        "description": "Retrieve disputes raised by the customer.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_id": {
                    "type": "string",
                    "description": "Unique customer ID."
                }
            },
            "required": ["customer_id"]
        }
    },

    {
        "name": "get_customer_service_requests",
        "description": "Retrieve customer service requests and their current status.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_id": {
                    "type": "string",
                    "description": "Unique customer ID."
                }
            },
            "required": ["customer_id"]
        }
    },

    {
        "name": "get_customer_loans",
        "description": "Retrieve loan accounts associated with the customer.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_id": {
                    "type": "string",
                    "description": "Unique customer ID."
                }
            },
            "required": ["customer_id"]
        }
    },

    {
        "name": "get_customer_emi_history",
        "description": "Retrieve the customer's EMI payment history and records.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_id": {
                    "type": "string",
                    "description": "Unique customer ID."
                }
            },
            "required": ["customer_id"]
        }
    },

    {
        "name": "get_customer_fees",
        "description": "Retrieve fees and charges associated with the customer's banking products or transactions.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_id": {
                    "type": "string",
                    "description": "Unique customer ID."
                }
            },
            "required": ["customer_id"]
        }
    },

    {
        "name": "get_customer_statements",
        "description": "Retrieve account statement information for the customer.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_id": {
                    "type": "string",
                    "description": "Unique customer ID."
                }
            },
            "required": ["customer_id"]
        }
    },

    {
        "name": "get_relationship_manager",
        "description": "Retrieve the relationship manager associated with the customer.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_id": {
                    "type": "string",
                    "description": "Unique customer ID."
                }
            },
            "required": ["customer_id"]
        }
    },

    {
        "name": "get_customer_offers",
        "description": "Retrieve offers and eligibility information available to the customer.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_id": {
                    "type": "string",
                    "description": "Unique customer ID."
                }
            },
            "required": ["customer_id"]
        }
    },

    {
        "name": "get_customer_case_overview",
        "description": (
            "Retrieve a consolidated overview of the customer's "
            "relevant banking information and case-related records."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "customer_id": {
                    "type": "string",
                    "description": "Unique customer ID."
                }
            },
            "required": ["customer_id"]
        }
    }
]