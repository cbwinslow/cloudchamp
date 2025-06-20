import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY", "")

def ask_llm(prompt, model="gpt-3.5-turbo"):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        max_tokens=500,
    )
    return response.choices[0].message["content"]