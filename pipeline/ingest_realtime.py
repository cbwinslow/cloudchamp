import asyncio
import websockets
import json
from config import API_CONFIG

async def ingest_realtime(sport):
    url = API_CONFIG[sport]["realtime_url"]
    api_key = API_CONFIG[sport]["api_key"]
    async with websockets.connect(url, extra_headers={"Ocp-Apim-Subscription-Key": api_key}) as ws:
        while True:
            msg = await ws.recv()
            event = json.loads(msg)
            print(f"Realtime {sport} event:", event)

# Example: Start real-time basketball ingestion
if __name__ == "__main__":
    asyncio.run(ingest_realtime("basketball"))