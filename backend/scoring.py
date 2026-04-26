import re
from difflib import SequenceMatcher

from backend.skill_normalizer import normalize_skill_list


# ---------------- LIST MATCH ----------------
def list_match_score(jd_list, candidate_list):

    jd_list = normalize_skill_list(jd_list)
    candidate_list = normalize_skill_list(candidate_list)

    if not jd_list:
        return 0

    match = len(set(jd_list) & set(candidate_list))
    return match / len(jd_list)


# ---------------- EXPERIENCE ----------------
def experience_match_score(jd_experience, candidate_experience):

    match = re.findall(r"\d+", str(jd_experience))

    if len(match) >= 2:
        min_exp, max_exp = int(match[0]), int(match[1])
    elif len(match) == 1:
        min_exp, max_exp = int(match[0]), int(match[0]) + 2
    else:
        return 0.5

    if min_exp <= candidate_experience <= max_exp:
        return 1.0
    elif candidate_experience < min_exp:
        return candidate_experience / max(min_exp, 1)
    else:
        return max_exp / candidate_experience


# ---------------- ROLE SIMILARITY ----------------
def role_similarity_score(jd_role, candidate_role):
    return SequenceMatcher(None, jd_role.lower(), candidate_role.lower()).ratio()


# ---------------- MAIN ----------------
def compute_match_score(jd, candidate):

    # 🔥 IMPORTANT: use proper fields
    skill_score = list_match_score(
        jd.get("skills_required", []),
        candidate.get("skills", [])
    )

    tool_score = list_match_score(
        jd.get("tools_technologies", []),
        candidate.get("tools", [])  # FIXED (was skills before)
    )

    soft_skill_score = list_match_score(
        jd.get("soft_skills", []),
        candidate.get("soft_skills", [])  # FIXED
    )

    exp_score = experience_match_score(
        jd.get("experience", ""),
        candidate.get("experience_years", 0)
    )

    role_score = role_similarity_score(
        jd.get("role", ""),
        candidate.get("current_role", "")
    )

    # ---------------- WEIGHTED FINAL ----------------
    final_score = (
        0.4 * skill_score +
        0.2 * tool_score +
        0.1 * soft_skill_score +
        0.15 * exp_score +
        0.15 * role_score
    )

    return {
        "final_score": round(final_score * 100, 2),
        "skill_score": round(skill_score * 100, 2),
        "tool_score": round(tool_score * 100, 2),
        "soft_skill_score": round(soft_skill_score * 100, 2),
        "experience_score": round(exp_score * 100, 2),
        "role_score": round(role_score * 100, 2)
    }