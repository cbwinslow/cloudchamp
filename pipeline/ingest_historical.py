import requests
from datetime import datetime, timedelta
from config import API_CONFIG

def fetch_historical_data(sport, date):
    url = API_CONFIG[sport]["historical_url"].format(date=date)
    headers = {"Ocp-Apim-Subscription-Key": API_CONFIG[sport]["api_key"]}
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    return resp.json()

# Example: Fetch yesterday's baseball games
if __name__ == "__main__":
    sport = "baseball"
    date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    data = fetch_historical_data(sport, date)
    print(data)