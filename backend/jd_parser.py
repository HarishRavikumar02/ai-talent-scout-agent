from backend.llm_client import call_llm
from backend.utils import extract_json


def parse_jd(jd_text):

    prompt = f"""
You are an expert AI recruiter.

Extract structured information from the job description.

Return ONLY valid JSON:

{{
  "role": "",
  "experience": "",
  "experience_years": 0,
  "skills_required": [],
  "skills_preferred": [],
  "tools_technologies": [],
  "responsibilities": [],
  "soft_skills": [],
  "seniority_level": ""
}}

Rules:
- Normalize skill names
- Keep lists concise (max 8)
- Extract experience_years if possible

Job Description:
{jd_text}
"""

    response = call_llm(prompt)
    return extract_json(response)