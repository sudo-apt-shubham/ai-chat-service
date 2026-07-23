from app.prompts import SYSTEM_PROMPT
from app.llm import generate

def chat(user_message):

    prompt = f"""
{SYSTEM_PROMPT}

User:

{user_message}
"""

    return generate(prompt)

