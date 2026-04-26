import fitz
from backend.llm_client import call_llm
from backend.utils import extract_json


def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text


def parse_resume(file):

    text = extract_text_from_pdf(file)

    prompt = f"""
Extract structured candidate profile.

Return ONLY JSON:

{{
  "name": "",
  "role": "",
  "experience_years": 0,
  "skills_required": [],
  "skills_preferred": [],
  "tools_technologies": [],
  "soft_skills": [],
  "seniority_level": ""
}}

Resume:
{text}
"""

    response = call_llm(prompt)
    return extract_json(response)