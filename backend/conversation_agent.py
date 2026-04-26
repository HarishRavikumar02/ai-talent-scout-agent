from backend.llm_client import call_llm
from backend.utils import extract_json


def simulate_conversation(candidate_name, role):
    """
    Simulates recruiter-candidate interaction using LLM
    """

    prompt = f"""
You are simulating a recruiter interacting with a candidate.

Candidate Name: {candidate_name}
Role: {role}

Return ONLY valid JSON.

Format:
{{
  "interest_level": "high/medium/low",
  "response_quality": "good/average/poor",
  "availability": "immediate/1 month/3 months",
  "expected_salary": "number in LPA"
}}

Rules:
- Be realistic (not always high interest)
"""

    response = call_llm(prompt)
    parsed = extract_json(response)

    if "error" in parsed:
        return {
            "interest_level": "medium",
            "response_quality": "average",
            "availability": "1 month",
            "expected_salary": "8"
        }

    return parsed


def compute_interest_score(convo):
    """
    Returns:
    - score (0–100)
    - explanation reasons
    """

    score = 0
    reasons = []

    if convo.get("interest_level") == "high":
        score += 40
        reasons.append("Strong interest expressed")
    elif convo.get("interest_level") == "medium":
        score += 25
        reasons.append("Moderate interest")
    else:
        score += 10
        reasons.append("Low interest")

    if convo.get("response_quality") == "good":
        score += 30
        reasons.append("Clear and confident responses")
    elif convo.get("response_quality") == "average":
        score += 20
        reasons.append("Average response quality")
    else:
        score += 10
        reasons.append("Weak communication")

    if convo.get("availability") == "immediate":
        score += 30
        reasons.append("Immediate availability")
    elif convo.get("availability") == "1 month":
        score += 20
        reasons.append("Available within 1 month")
    else:
        score += 10
        reasons.append("Longer notice period")

    return score, reasons