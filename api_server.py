from fastapi import FastAPI, Query
from main import run_swarm

app = FastAPI()

@app.post("/collect")
async def collect(task_type: str = Query("fetch_historical")):
    results = run_swarm(task_type)
    return {"results": results}

@app.post("/collect/player")
async def collect_player():
    results = run_swarm("fetch_player_realtime")
    return {"results": results}