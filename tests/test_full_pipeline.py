from backend.candidate_matcher import (
    load_candidates,
    preprocess_candidates,
    score_all_candidates
)

jd = {
    "skills": ["Python", "SQL"],
    "experience": "2-5 years",
    "role": "Data Analyst"
}

df = load_candidates()
df = preprocess_candidates(df)

results = score_all_candidates(jd, df)

for r in results[:5]:
    print(r)