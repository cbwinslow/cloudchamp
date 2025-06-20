import os

SPORTS = ["baseball", "basketball", "football", "hockey"]

API_CONFIG = {
    "baseball": {
        "historical_url": os.getenv("BASEBALL_HISTORICAL_URL", "https://api.sportsdata.io/v3/mlb/scores/json/GamesByDate/{date}"),
        "realtime_url": os.getenv("BASEBALL_REALTIME_URL", "wss://realtime.sportsdata.io/mlb"),
        "player_realtime_url": os.getenv("BASEBALL_PLAYER_REALTIME_URL", "wss://realtime.sportsdata.io/mlb/players"),
        "api_key": os.getenv("BASEBALL_API_KEY", ""),
    },
    "basketball": {
        "historical_url": os.getenv("BASKETBALL_HISTORICAL_URL", "https://api.sportsdata.io/v3/nba/scores/json/GamesByDate/{date}"),
        "realtime_url": os.getenv("BASKETBALL_REALTIME_URL", "wss://realtime.sportsdata.io/nba"),
        "player_realtime_url": os.getenv("BASKETBALL_PLAYER_REALTIME_URL", "wss://realtime.sportsdata.io/nba/players"),
        "api_key": os.getenv("BASKETBALL_API_KEY", ""),
    },
    "football": {
        "historical_url": os.getenv("FOOTBALL_HISTORICAL_URL", "https://api.sportsdata.io/v3/nfl/scores/json/GamesByDate/{date}"),
        "realtime_url": os.getenv("FOOTBALL_REALTIME_URL", "wss://realtime.sportsdata.io/nfl"),
        "player_realtime_url": os.getenv("FOOTBALL_PLAYER_REALTIME_URL", "wss://realtime.sportsdata.io/nfl/players"),
        "api_key": os.getenv("FOOTBALL_API_KEY", ""),
    },
    "hockey": {
        "historical_url": os.getenv("HOCKEY_HISTORICAL_URL", "https://api.sportsdata.io/v3/nhl/scores/json/GamesByDate/{date}"),
        "realtime_url": os.getenv("HOCKEY_REALTIME_URL", "wss://realtime.sportsdata.io/nhl"),
        "player_realtime_url": os.getenv("HOCKEY_PLAYER_REALTIME_URL", "wss://realtime.sportsdata.io/nhl/players"),
        "api_key": os.getenv("HOCKEY_API_KEY", ""),
    },
}

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
E2B_API_KEY = os.getenv("E2B_API_KEY", "")