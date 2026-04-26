from backend.skill_normalizer import normalize_skill_list


def generate_match_explanation(jd, candidate):

    # 🔥 USE SAME NORMALIZATION AS SCORING
    jd_skills = set(normalize_skill_list(jd.get("skills_required", [])))
    candidate_skills = set(normalize_skill_list(candidate.get("skills", [])))

    matched = sorted(list(jd_skills & candidate_skills))
    missing = sorted(list(jd_skills - candidate_skills))

    # ---------------- EXPLANATION ----------------
    explanation = ""

    if matched:
        explanation += f"Strong match in {len(matched)} key skills: {', '.join(matched[:3])}. "
    else:
        explanation += "Limited overlap in required skills. "

    if missing:
        explanation += f"Missing {len(missing)} important skills."

    return {
        "matched_skills": matched,
        "missing_skills": missing,
        "explanation": explanation
    }