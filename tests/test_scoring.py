from backend.scoring import compute_match_score

jd = {
    "skills": ["Python", "SQL"],
    "experience": "2-5 years",
    "role": "Data Analyst"
}

candidate = {
    "skills": ["python", "sql", "power bi"],
    "experience_years": 3,
    "current_role": "data analyst"
}

print(compute_match_score(jd, candidate))