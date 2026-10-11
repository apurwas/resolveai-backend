from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel
from typing import Literal
import numpy as np
import pickle
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

EMBEDDING_FILE = "policy_embeddings.pkl"


# ---------- Structured AI output ----------

class Resolution(BaseModel):
    recommended_action: str
    agent_explanation: str
    customer_response: str
    escalation_required: bool
    risk_level: Literal["low", "medium", "high"]


# ---------- Embeddings ----------

def create_embedding(text):
    result = client.models.embed_content(
        model="gemini-embedding-001",
        contents=text
    )

    return np.array(result.embeddings[0].values)


# ---------- Similarity ----------

def cosine_similarity(a, b):
    return np.dot(a, b) / (
        np.linalg.norm(a) * np.linalg.norm(b)
    )


# ---------- Load saved policies ----------

with open(EMBEDDING_FILE, "rb") as file:
    policies = pickle.load(file)


# ---------- Customer case ----------

customer_query = """
My ATM deducted ₹5,000 from my account,
but I did not receive any cash.
"""


# ---------- Retrieve policy ----------

query_embedding = create_embedding(customer_query)

results = []

for policy in policies:

    score = cosine_similarity(
        query_embedding,
        policy["embedding"]
    )

    results.append({
        "file": policy["file"],
        "text": policy["text"],
        "score": score
    })

results.sort(
    key=lambda x: x["score"],
    reverse=True
)

best_policy = results[0]

print("Retrieved policy:")
print(best_policy["file"])
print(f"Similarity: {best_policy['score']:.4f}")


# ---------- Generate resolution ----------

prompt = f"""
You are ResolveAI, an AI customer-service copilot
for a banking agent.

Use ONLY the policy provided below.
Do not invent policies, fees, timelines, or procedures.

CUSTOMER QUERY:
{customer_query}

APPROVED POLICY:
{best_policy["text"]}

Generate a resolution for the banking agent.

Determine:
- recommended action
- explanation for the agent
- suggested customer response
- whether human escalation is required
- risk level

High-risk cases should require human escalation.
"""


response = client.interactions.create(
    model="gemini-3.5-flash-lite",
    input=prompt,
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": Resolution.model_json_schema()
    }
)


resolution = Resolution.model_validate_json(
    response.output_text
)


# ---------- Guardrails ----------

if resolution.risk_level == "high":
    status = "ESCALATE"
elif resolution.escalation_required:
    status = "ESCALATE"
else:
    status = "AGENT_REVIEW"


print("\n--- RESOLVEAI RESULT ---")

print("\nRecommended action:")
print(resolution.recommended_action)

print("\nAgent explanation:")
print(resolution.agent_explanation)

print("\nCustomer response:")
print(resolution.customer_response)

print("\nRisk level:")
print(resolution.risk_level)

print("\nStatus:")
print(status)
