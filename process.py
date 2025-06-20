def process_game_data(raw_game):
    return {
        "game_id": raw_game.get("GameID"),
        "date": raw_game.get("Day"),
        "home_team": raw_game.get("HomeTeam"),
        "away_team": raw_game.get("AwayTeam"),
        "home_score": raw_game.get("HomeTeamScore"),
        "away_score": raw_game.get("AwayTeamScore"),
    }

def process_player_event(raw_event):
    # Normalize player event fields
    return {
        "player_id": raw_event.get("player_id"),
        "player_name": raw_event.get("player_name"),
        "sport": raw_event.get("sport"),
        "stat_type": raw_event.get("stat_type"),
        "value": raw_event.get("value"),
        "timestamp": raw_event.get("timestamp"),
    }