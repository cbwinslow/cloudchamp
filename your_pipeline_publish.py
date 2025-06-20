import redis
import json

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
r.publish(channel, json.dumps(event))