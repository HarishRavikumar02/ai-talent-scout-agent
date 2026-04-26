from backend.llm_client import call_llm
from backend.utils import extract_json

prompt = open("prompts/jd_parser_prompt.txt").read().replace(
    "{jd_text}",
    "Looking for a Data Analyst with 3 years experience in Python, SQL, and Power BI"
)

response = call_llm(prompt)

parsed = extract_json(response)

print(parsed)