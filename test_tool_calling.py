import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

from mock_banking_tools import (
    get_transaction_details,
    get_refund_status
)


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


# ---------------------------------------------------------
# 1. Define tools
# ---------------------------------------------------------

transaction_tool = {
    "name": "get_transaction_details",
    "description": (
        "Retrieve detailed information about a specific "
        "bank transaction."
    ),
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
}


refund_tool = {
    "name": "get_refund_status",
    "description": (
        "Retrieve the current status and details "
        "of a specific refund."
    ),
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
}


tools = [
    {
        "function_declarations": [
            transaction_tool,
            refund_tool
        ]
    }
]


# ---------------------------------------------------------
# 2. Map tool names to Python functions
# ---------------------------------------------------------

tool_functions = {
    "get_transaction_details": get_transaction_details,
    "get_refund_status": get_refund_status
}


# ---------------------------------------------------------
# 3. Customer complaint
# ---------------------------------------------------------

question = """
A customer says:

"My Flipkart card payment of ₹46,125.36 failed.
Transaction ID is TXN-0000003.
I was told a refund was initiated, but I have
not received it.
Refund ID is REF-00052.

Tell me what happened to the payment and
what is the current refund status."
"""


# ---------------------------------------------------------
# 4. Start the conversation
# ---------------------------------------------------------

conversation = [question]


# ---------------------------------------------------------
# 5. AGENTIC TOOL LOOP
# ---------------------------------------------------------

while True:

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=conversation,
        config={
            "tools": tools
        }
    )


    # Keep Gemini's response in the conversation
    conversation.append(
        response.candidates[0].content
    )


    # Collect tool results from this round
    function_response_parts = []

    tool_was_requested = False


    # -----------------------------------------------------
    # 6. Check whether Gemini wants any tools
    # -----------------------------------------------------

    for candidate in response.candidates:

        for part in candidate.content.parts:

            if not part.function_call:
                continue


            tool_was_requested = True

            function_call = part.function_call

            tool_name = function_call.name
            arguments = dict(function_call.args)


            print("\n===== TOOL REQUESTED =====")
            print("Tool:", tool_name)
            print("Arguments:", arguments)


            # -------------------------------------------------
            # 7. Find the corresponding Python function
            # -------------------------------------------------

            tool_function = tool_functions.get(tool_name)


            if tool_function is None:

                print("Unknown tool:", tool_name)

                continue


            # -------------------------------------------------
            # 8. Execute the Python function
            # -------------------------------------------------

            tool_result = tool_function(
                **arguments
            )


            print("\n===== TOOL RESULT =====")
            print(tool_result)


            # -------------------------------------------------
            # 9. Prepare result for Gemini
            # -------------------------------------------------

            function_response_parts.append(
                types.Part.from_function_response(
                    name=tool_name,
                    response={
                        "result": tool_result
                    }
                )
            )


    # -----------------------------------------------------
    # 10. If no tool was requested, we're finished
    # -----------------------------------------------------

    if not tool_was_requested:

        print("\n===== FINAL GEMINI ANSWER =====")
        print(response.text)

        break


    # -----------------------------------------------------
    # 11. Send tool results back to Gemini
    # -----------------------------------------------------

    conversation.append(
        types.Content(
            role="user",
            parts=function_response_parts
        )
    )