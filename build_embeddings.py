from pathlib import Path
from dotenv import load_dotenv
from google import genai
import numpy as np
import pickle
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

BASE = Path("knowledge_base")
OUTPUT_FILE = "policy_embeddings.pkl"


def create_embedding(text):
    result = client.models.embed_content(
        model="gemini-embedding-001",
        contents=text
    )

    return np.array(result.embeddings[0].values)


policies = []

for file_path in BASE.rglob("*.txt"):

    text = file_path.read_text(encoding="utf-8")

    print(f"Embedding: {file_path}")

    embedding = create_embedding(text)

    policies.append({
        "file": str(file_path),
        "text": text,
        "embedding": embedding
    })


with open(OUTPUT_FILE, "wb") as file:
    pickle.dump(policies, file)


print("\nDone!")
print(f"Saved {len(policies)} policy embeddings.")
print(f"File: {OUTPUT_FILE}")