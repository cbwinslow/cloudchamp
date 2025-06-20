# Run this script to publish a test event to Redis
import redis
import json
import time

r = redis.Redis(host="localhost", port=6379, decode_responses=True)
channel = "sports_events"

event = {
    "sport": "basketball",
    "event": "player_update",
    "player": "John Doe",
    "stat": "points",
    "value": 2,
    "timestamp": "2025-06-20T23:00:00Z"
}

while True:
    r.publish(channel, json.dumps(event))
    print("Published event to Redis")
    time.sleep(3)