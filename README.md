# ResolveAI — Backend API

ResolveAI is an AI-powered customer service resolution copilot for banking and financial services (BFSI). This repository contains the Python backend that processes customer complaints, retrieves relevant banking policies, investigates synthetic banking data, and generates structured resolution recommendations for human agents.

## Key Capabilities

- **Complaint routing:** Classifies incoming complaints and selects an investigation type.
- **Policy retrieval (RAG):** Retrieves relevant policy information using semantic similarity.
- **AI tool calling:** Allows the model to request approved investigation tools.
- **Synthetic banking tools:** Simulates banking operations and returns mock customer evidence.
- **Structured recommendations:** Produces an agent explanation, recommended action, customer-response draft, risk level, and escalation recommendation.
- **Human review:** Supports an agent-in-the-loop workflow rather than automatically executing banking actions.

## Architecture

```text
Next.js Frontend
       |
       | POST /analyze
       v
FastAPI Backend
       |
       v
Case Router
       |
       v
Policy Retrieval (RAG)
       |
       v
Investigation Tools
       |
       v
Evidence Summary
       |
       v
Gemini AI
       |
       v
Structured Resolution
```

## Technology Stack

- Python
- FastAPI and Uvicorn
- Google Gemini API
- Pydantic
- Semantic embeddings and cosine similarity
- Synthetic banking data stored locally as JSON
- Policy documents used for retrieval-augmented generation (RAG)

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/health` | Checks backend health |
| POST | `/analyze` | Analyzes a customer complaint |

### Example request

```json
{
  "customer_id": "CUST-1001",
  "message": "My UPI payment failed, but the money was debited."
}
```

The analysis endpoint returns a structured result containing complaint classification, retrieved policy information, investigation evidence, recommended action, agent explanation, customer-response draft, risk level, escalation flag, and workflow status.

## Run Locally

### 1. Create and activate a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```powershell
pip install -r requirements.txt
```

### 3. Configure the API key

Create a `.env` file in the project root:

```text
GEMINI_API_KEY=your_gemini_api_key
```

Use your own API key locally. Never commit `.env` or publish your secret key.

### 4. Start the API

```powershell
uvicorn main:app --reload
```

The local API runs at `http://127.0.0.1:8000`.

Interactive API documentation is available at `http://127.0.0.1:8000/docs`.

## Project Structure

- `main.py` — FastAPI application and HTTP endpoints
- `resolve_service.py` — Main resolution orchestration
- `case_router.py` — Complaint classification and investigation routing
- `tool_policy.py` — Investigation-specific tool permissions
- `investigation_plans.py` — Investigation objectives and evidence checklists
- `tool_registry.py` — Tool schemas and Python function registry
- `mock_banking_tools.py` — Synthetic banking investigation functions
- `mock_data/` — Synthetic banking records
- `knowledge_base/` — Fictional banking policy documents
- `build_embeddings.py` — Policy embedding generation
- `policy_embeddings.pkl` — Precomputed policy embeddings
- `guardrails.py` — Prototype safety and escalation rules
- `requirements.txt` — Python dependencies

## Important Limitations

- Uses synthetic banking records, not live banking systems.
- AI-generated recommendations require human review.
- Investigation completeness, evidence grounding, risk handling, and escalation behavior require continued testing and improvement.
- This is a portfolio prototype, not a production-ready banking system.

## Future Improvements

- Improve investigation completeness and tool-selection reliability.
- Display evidence more clearly, including missing or unverified evidence.
- Strengthen deterministic grounding and escalation checks.
- Add automated tests across complaint scenarios.
- Deploy the frontend and backend for a public portfolio demonstration.

## Project Goal

Demonstrate practical AI product building through an agent-assist workflow that combines LLM orchestration, retrieval-augmented generation, tool calling, structured outputs, and human oversight.