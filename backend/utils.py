import os
import openai

WORKSPACE_DIR = "workspaces"
os.makedirs(WORKSPACE_DIR, exist_ok=True)

def run_chatbot(prompt):
    # Stub: Replace with OpenAI/LLM call
    try:
        openai.api_key = os.getenv("OPENAI_API_KEY", "")
        resp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
            max_tokens=200,
        )
        return resp.choices[0].message["content"]
    except Exception as e:
        return f"Chatbot error: {e}"

def save_workspace(name, content):
    with open(f"{WORKSPACE_DIR}/{name}.json", "w") as f:
        f.write(content)

def load_workspace(name):
    try:
        with open(f"{WORKSPACE_DIR}/{name}.json", "r") as f:
            return f.read()
    except Exception:
        return ""

def run_pipeline_script(code, params):
    # Here you can actually run scripts/queries against your pipeline.
    # For now, just echo.
    return f"Ran code: {code}\nWith params: {params}"