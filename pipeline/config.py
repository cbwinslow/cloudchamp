SPORTS = ["baseball", "basketball", "football", "hockey"]

API_CONFIG = {
    "baseball": {
        "historical_url": "https://api.sportsdata.io/v3/mlb/scores/json/GamesByDate/{date}",
        "realtime_url": "wss://realtime.sportsdata.io/mlb",
        "api_key": "YOUR_API_KEY",
    },
    "basketball": {
        "historical_url": "https://api.sportsdata.io/v3/nba/scores/json/GamesByDate/{date}",
        "realtime_url": "wss://realtime.sportsdata.io/nba",
        "api_key": "YOUR_API_KEY",
    },
    "football": {
        "historical_url": "https://api.sportsdata.io/v3/nfl/scores/json/GamesByDate/{date}",
        "realtime_url": "wss://realtime.sportsdata.io/nfl",
        "api_key": "YOUR_API_KEY",
    },
    "hockey": {
        "historical_url": "https://api.sportsdata.io/v3/nhl/scores/json/GamesByDate/{date}",
        "realtime_url": "wss://realtime.sportsdata.io/nhl",
        "api_key": "YOUR_API_KEY",
    },
}