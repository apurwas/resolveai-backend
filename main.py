from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from resolve_service import resolve_case


app = FastAPI(
    title="ResolveAI API",
    description="AI Customer Service Resolution Copilot",
    version="1.0.0"
)


# Allow the local Next.js frontend to communicate with this API.
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "https://resolveai-frontend-kohl.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class CustomerRequest(BaseModel):
    customer_id: str
    message: str


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "ResolveAI"
    }


@app.post("/analyze")
def analyze_case(request: CustomerRequest):

    result = resolve_case(
        customer_id=request.customer_id,
        customer_message=request.message
    )

    return result