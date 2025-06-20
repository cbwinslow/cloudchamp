import psycopg2

def store_game(game, sport):
    conn = psycopg2.connect("dbname=sports user=postgres")
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO games (game_id, sport, date, home_team, away_team, home_score, away_score)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (game_id) DO NOTHING
        """, (
        game["game_id"], sport, game["date"],
        game["home_team"], game["away_team"],
        game["home_score"], game["away_score"]
    ))
    conn.commit()
    cur.close()
    conn.close()