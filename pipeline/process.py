def process_game_data(raw_game):
    # Clean/standardize fields, e.g., ensuring consistent datetime, team names, scores
    return {
        "game_id": raw_game.get("GameID"),
        "date": raw_game.get("Day"),
        "home_team": raw_game.get("HomeTeam"),
        "away_team": raw_game.get("AwayTeam"),
        "home_score": raw_game.get("HomeTeamScore"),
        "away_score": raw_game.get("AwayTeamScore"),
        # add more standardized fields as needed
    }