from datetime import datetime, timedelta
import requests
import logging

def fetch_historical_data(sport, api_config):
    date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    url = api_config["historical_url"].format(date=date)
    headers = {"Ocp-Apim-Subscription-Key": api_config["api_key"]}
    try:
        resp = requests.get(url, headers=headers, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        logging.info(f"{sport.capitalize()} historical data: {data[:1]}")
        return data
    except Exception as e:
        logging.error(f"Error fetching {sport} historical: {e}")
        return [{"error": str(e)}]

def fetch_realtime_data(sport, api_config):
    # Placeholder: would be a websocket or webhook in production
    return [{"event": f"Dummy real-time {sport} event"}]

def fetch_realtime_player_data(sport, api_config):
    # Real implementation would connect to a websocket or stream
    # For demo, we provide a stub player event
    return [{
        "event": f"Dummy real-time {sport} player event",
        "player_id": "1234",
        "player_name": "John Doe",
        "stat_type": "points",
        "value": 2,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }]