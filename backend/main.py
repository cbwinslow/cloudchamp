import asyncio
import json
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import redis.asyncio as aioredis

from utils import run_chatbot, save_workspace, load_workspace, run_pipeline_script

app = FastAPI()

# CORS for local frontend dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

REDIS_URL = "redis://redis:6379"
REDIS_CHANNEL = "sports_events"

frontend_dir = Path(__file__).parent.parent / "frontend" / "build"

@app.get("/")
def root():
    index_file = frontend_dir / "index.html"
    return FileResponse(str(index_file))

# --- WebSocket that relays events from Redis Pub/Sub ---
async def redis_event_stream():
    redis = aioredis.from_url(REDIS_URL, decode_responses=True)
    pubsub = redis.pubsub()
    await pubsub.subscribe(REDIS_CHANNEL)
    try:
        async for message in pubsub.listen():
            if message["type"] == "message":
                yield message["data"]
    finally:
        await pubsub.unsubscribe(REDIS_CHANNEL)
        await pubsub.close()

@app.websocket("/ws/stream")
async def ws_stream(websocket: WebSocket):
    await websocket.accept()
    try:
        async for event_json in redis_event_stream():
            await websocket.send_text(event_json)
    except WebSocketDisconnect:
        pass

# --- Script/query runner endpoint (dummy for now, hook up your pipeline logic here) ---
@app.post("/api/script")
async def run_script(req: Request):
    data = await req.json()
    code = data.get("code")
    params = data.get("params")
    result = run_pipeline_script(code, params)
    return {"result": result}

# --- Chatbot endpoint ---
@app.post("/api/chatbot")
async def chatbot_endpoint(req: Request):
    data = await req.json()
    prompt = data.get("prompt", "")
    response = run_chatbot(prompt)
    return {"response": response}

# --- Workspace save/load ---
@app.post("/api/workspace/save")
async def save_ws(req: Request):
    data = await req.json()
    name = data.get("name")
    content = data.get("content")
    save_workspace(name, content)
    return {"status": "ok"}

@app.get("/api/workspace/load")
async def load_ws(name: str):
    content = load_workspace(name)
    return {"content": content}