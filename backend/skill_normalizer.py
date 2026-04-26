import re
from difflib import get_close_matches


CANONICAL_SKILLS = {
    "react": ["reactjs", "react.js", "react js"],
    "javascript": ["js", "node js"],
    "css": ["css3"],
    "html": ["html5"],
    "node": ["nodejs", "node.js"],
    "machine learning": ["ml"],
    "deep learning": ["dl"],
    "natural language processing": ["nlp"],
    "postgresql": ["postgres", "psql"],
    "amazon web services": ["aws"],
    "google cloud platform": ["gcp"],
    "microsoft azure": ["azure"],
    "power bi": ["powerbi"],
}


# 🔁 BUILD REVERSE MAP
REVERSE_MAP = {}
for canonical, variants in CANONICAL_SKILLS.items():
    for v in variants:
        REVERSE_MAP[v] = canonical


def clean_skill(skill):
    skill = skill.lower().strip()

    # remove punctuation
    skill = re.sub(r"[^a-z0-9\s]", "", skill)

    # remove extra spaces
    skill = re.sub(r"\s+", " ", skill)

    return skill


def rule_based_normalization(skill):
    """
    General rules that work across domains
    """

    # remove common suffixes
    skill = skill.replace("framework", "")
    skill = skill.replace("library", "")
    skill = skill.replace("tool", "")

    skill = skill.strip()

    return skill


def normalize_skill(skill):
    skill = clean_skill(skill)

    # 1️⃣ direct mapping
    if skill in REVERSE_MAP:
        return REVERSE_MAP[skill]

    # 2️⃣ canonical already
    if skill in CANONICAL_SKILLS:
        return skill

    # 3️⃣ rule-based cleanup
    skill = rule_based_normalization(skill)

    # 4️⃣ fuzzy match against canonical
    match = get_close_matches(skill, CANONICAL_SKILLS.keys(), n=1, cutoff=0.8)
    if match:
        return match[0]

    return skill


def normalize_skill_list(skills):
    return list(set([normalize_skill(s) for s in skills if s]))