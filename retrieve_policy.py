from pathlib import Path
import re

# Our policy folder
BASE = Path("knowledge_base")

# Example customer case
query = """
I made a UPI payment yesterday. The money was deducted from my account,
but the merchant says they have not received it.
"""

# Words that don't help us identify the policy
STOP_WORDS = {
    "the", "was", "but", "did", "not", "any",
    "my", "i", "a", "an", "is", "to", "from",
    "and", "for", "of", "on", "in"
}


# Convert text into useful words
def get_words(text):
    words = re.findall(r"\b[a-zA-Z]+\b", text.lower())
    return set(words) - STOP_WORDS


query_words = get_words(query)

results = []

# Find every .txt policy inside knowledge_base
for file_path in BASE.rglob("*.txt"):

    policy_text = file_path.read_text(encoding="utf-8")

    policy_words = get_words(policy_text)

    # Count how many words overlap
    matching_words = query_words & policy_words
    score = len(matching_words)

    results.append(
        (score, file_path, matching_words)
    )


# Highest score first
results.sort(reverse=True, key=lambda x: x[0])


print("\nTop matching policies:\n")

for score, file_path, matching_words in results[:3]:

    print(f"Score: {score}")
    print(f"Policy: {file_path}")
    print(f"Matching words: {matching_words}")
    print("-" * 50)