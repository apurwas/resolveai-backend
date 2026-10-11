from pathlib import Path
from dotenv import load_dotenv
from google import genai
import numpy as np
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

BASE = Path("knowledge_base")


def create_embedding(text):
    result = client.models.embed_content(
        model="gemini-embedding-001",
        contents=text
    )

    return np.array(result.embeddings[0].values)


# ---------------------------------------
# 1. Load all policies
# ---------------------------------------

policies = []

for file_path in BASE.rglob("*.txt"):

    text = file_path.read_text(encoding="utf-8")

    embedding = create_embedding(text)

    policies.append({
        "file": str(file_path),
        "text": text,
        "embedding": embedding
    })

    print(f"Embedded: {file_path}")


# ---------------------------------------
# 2. Customer query
# ---------------------------------------

query = """
My ATM deducted ₹5,000 from my account,
but I did not receive any cash.
"""

query_embedding = create_embedding(query)


# ---------------------------------------
# 3. Calculate similarity
# ---------------------------------------

def cosine_similarity(a, b):

    return np.dot(a, b) / (
        np.linalg.norm(a) * np.linalg.norm(b)
    )


results = []

for policy in policies:

    score = cosine_similarity(
        query_embedding,
        policy["embedding"]
    )

    results.append({
        "file": policy["file"],
        "score": score,
        "text": policy["text"]
    })


# ---------------------------------------
# 4. Sort by similarity
# ---------------------------------------

results.sort(
    key=lambda x: x["score"],
    reverse=True
)


# ---------------------------------------
# 5. Display top results
# ---------------------------------------

print("\nTop semantic matches:\n")

for result in results[:3]:

    print(f"Score: {result['score']:.4f}")
    print(f"Policy: {result['file']}")
    print("-" * 50)