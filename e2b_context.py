import os
from e2b import Session

E2B_API_KEY = os.getenv("E2B_API_KEY", "")

def get_e2b_context():
    """Get e2b session context if running inside e2b."""
    if not E2B_API_KEY:
        return None
    try:
        session = Session(api_key=E2B_API_KEY)
        context = {
            "cwd": session.fs.getcwd(),
            "env_vars": session.env.list(),
        }
        # Example: read files from workspace
        # files = session.fs.ls(".")
        # context["files"] = files
        return context
    except Exception as e:
        print(f"e2b context error: {e}")
        return None

def write_to_e2b_file(filename, content):
    if not E2B_API_KEY:
        return
    try:
        session = Session(api_key=E2B_API_KEY)
        session.fs.write(filename, content)
    except Exception as e:
        print(f"e2b write error: {e}")