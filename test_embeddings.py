from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

text = """
The customer's bank account was debited at an ATM,
but no cash was dispensed.
"""

result = client.models.embed_content(
    model="gemini-embedding-001",
    contents=text
)

embedding = result.embeddings[0].values

print("Embedding created successfully!")
print("Number of dimensions:", len(embedding))
print("First 10 numbers:", embedding[:10])