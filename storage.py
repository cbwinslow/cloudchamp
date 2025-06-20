import psycopg2
import os

def get_connection():
    return psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB", "sports"),
        user=os.getenv("POSTGRES_USER", "postgres"),
        password=os.getenv("POSTGRES_PASSWORD", "postgres"),
        host=os.getenv("POSTGRES_HOST", "db"),
        port=int(os.getenv("POSTGRES_PORT", 5432))
    )

def store_game(game, sport):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS games (
            game_id TEXT PRIMARY KEY,
            sport TEXT,
            date TEXT,
            home_team TEXT,
            away_team TEXT,
            home_score INTEGER,
            away_score INTEGER
        );
    """)
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

def store_player_event(ev, sport):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS player_events (
            id SERIAL PRIMARY KEY,
            player_id TEXT,
            player_name TEXT,
            sport TEXT,
            stat_type TEXT,
            value INTEGER,
            timestamp TEXT
        );
    """)
    cur.execute("""
        INSERT INTO player_events (player_id, player_name, sport, stat_type, value, timestamp)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        ev["player_id"], ev["player_name"], sport,
        ev["stat_type"], ev["value"], ev["timestamp"]
    ))
    conn.commit()
    cur.close()
    conn.close()