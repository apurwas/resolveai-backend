import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

from tool_registry import TOOL_DEFINITIONS, TOOL_FUNCTIONS


load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


tools = [
    types.Tool(
        function_declarations=TOOL_DEFINITIONS
    )
]


chat = client.chats.create(
    model="gemini-3.5-flash-lite",
    config=types.GenerateContentConfig(
        tools=tools,
        automatic_function_calling=types.AutomaticFunctionCallingConfig(
            disable=True
        )
    )
)


prompt = """
You are ResolveAI, an AI banking customer-service agent.

Customer ID: CUST-1001

Customer says:
"My EMI payment looks incorrect. Can you check what is happening?"

Use the appropriate banking tools to investigate the case.

Do not answer the customer until you have retrieved the information
necessary to understand the issue.
"""


response = chat.send_message(prompt)


MAX_TOOL_CALLS = 5
tool_call_count = 0


while tool_call_count < MAX_TOOL_CALLS:

    function_calls = []

    for candidate in response.candidates:
        for part in candidate.content.parts:

            if part.function_call:
                function_calls.append(part.function_call)


    # No tool call means Gemini has finished
    if not function_calls:

        print("\nGemini's final response:")
        print(response.text)
        break


    # Execute requested tools
    tool_response_parts = []

    for function_call in function_calls:

        tool_call_count += 1

        tool_name = function_call.name
        arguments = dict(function_call.args)

        print(f"\n--- Tool Call {tool_call_count} ---")

        print("Gemini selected tool:")
        print(tool_name)

        print("Arguments:")
        print(arguments)


        tool_function = TOOL_FUNCTIONS.get(tool_name)

        if tool_function is None:

            print("ERROR: Tool not found:", tool_name)

            tool_result = {
                "error": f"Tool '{tool_name}' is not available."
            }

        else:

            tool_result = tool_function(**arguments)

            print("Tool result:")
            print(tool_result)


        tool_response_parts.append(
            types.Part.from_function_response(
                name=tool_name,
                response={
                    "result": tool_result
                }
            )
        )


    # Send ALL tool results back to Gemini
    response = chat.send_message(
        tool_response_parts
    )


else:

    print("\nAgent stopped because maximum tool calls were reached.")