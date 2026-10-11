from case_router import route_case


test_cases = [
    "How do I set my MPIN?",
    "I cannot set my MPIN and it keeps failing.",
    "My UPI payment was debited but the merchant didn't receive it.",
    "What is the process for disputing a card payment?",
    "Why was my card payment declined?"
]


for message in test_cases:

    print("\n" + "=" * 60)
    print("CUSTOMER:", message)

    result = route_case(message)

    print("INTENT:", result.intent)
    print("REQUIRES CUSTOMER DATA:", result.requires_customer_data)
    print("INVESTIGATION TYPE:", result.investigation_type)
    print("REASONING:", result.reasoning)