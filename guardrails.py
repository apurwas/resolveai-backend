def apply_guardrails(
    priority,
    policy_text,
    ai_response
):

    # Rule 1: High-priority cases require human review
    if priority == "high":
        return {
            "status": "ESCALATE",
            "reason": "High-priority banking case requires human review.",
            "response": ai_response
        }

    # Rule 2: No policy = don't allow AI resolution
    if not policy_text.strip():
        return {
            "status": "ESCALATE",
            "reason": "No approved policy was retrieved.",
            "response": ai_response
        }

    # Rule 3: Basic check that the AI actually produced something
    if not ai_response.strip():
        return {
            "status": "ESCALATE",
            "reason": "AI did not produce a valid response.",
            "response": ""
        }

    # Otherwise allow agent review
    return {
        "status": "AGENT_REVIEW",
        "reason": "Response generated using approved policy.",
        "response": ai_response
    }