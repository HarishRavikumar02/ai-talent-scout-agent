from openai import OpenAI
from config.settings import OPENAI_API_KEY, OPENAI_MODEL, TEMPERATURE, MAX_TOKENS

client = OpenAI(api_key=OPENAI_API_KEY)

def call_llm(prompt):
    try:
        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a strict JSON generator. "
                        "Return ONLY valid JSON. No explanations."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=TEMPERATURE,
            max_tokens=MAX_TOKENS
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"ERROR: {str(e)}"