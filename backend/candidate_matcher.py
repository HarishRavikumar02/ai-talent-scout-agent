import pandas as pd

from backend.scoring import compute_match_score
from backend.conversation_agent import simulate_conversation, compute_interest_score
from backend.explainer import generate_match_explanation


def load_candidates(path="data/candidates_structured.csv"):
    return pd.read_csv(path)


def preprocess_candidates(df):

    def split_safe(x):
        return x.split(";") if isinstance(x, str) and x else []

    df["skills_required"] = df["skills_required"].apply(split_safe)
    df["skills_preferred"] = df["skills_preferred"].apply(split_safe)
    df["tools_technologies"] = df["tools_technologies"].apply(split_safe)
    df["soft_skills"] = df["soft_skills"].apply(split_safe)

    return df


def get_hiring_recommendation(score):
    if score >= 85:
        return "🟢 Approved"
    elif score >= 70:
        return "🟡 Consider"
    else:
        return "🔴 Reject"


def score_all_candidates(jd, df):

    results = []

    for _, row in df.iterrows():

        candidate = {
            "skills": row.get("skills_required", []),
            "tools": row.get("tools_technologies", []),
            "soft_skills": row.get("soft_skills", []),
            "experience_years": row.get("experience_years", 0),
            "current_role": row.get("role", "")
        }

        scores = compute_match_score(jd, candidate)

        convo = simulate_conversation(row["name"], jd.get("role", ""))
        interest_score, engagement_reasons = compute_interest_score(convo)

        explanation = generate_match_explanation(jd, candidate)

        final_score = (
            0.7 * scores.get("final_score", 0) +
            0.3 * interest_score
        )

        results.append({
            "id": row["id"],
            "name": row["name"],
            "role": row.get("role", ""),
            "experience_years": row.get("experience_years", 0),

            "skill_score": scores.get("skill_score", 0),
            "tool_score": scores.get("tool_score", 0),
            "soft_skill_score": scores.get("soft_skill_score", 0),
            "experience_score": scores.get("experience_score", 0),

            "interest_score": interest_score,
            "engagement_reasons": engagement_reasons,

            "matched_skills": explanation["matched_skills"],
            "missing_skills": explanation["missing_skills"],
            "match_explanation": explanation["explanation"],

            "final_score": round(final_score, 2),
            "recommendation": get_hiring_recommendation(final_score)
        })

    return sorted(results, key=lambda x: x["final_score"], reverse=True)