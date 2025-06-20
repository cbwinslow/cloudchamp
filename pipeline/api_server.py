from fastapi import FastAPI, Query
import psycopg2

app = FastAPI()

@app.get("/games")
def get_games(sport: str = None, date: str = None):
    conn = psycopg2.connect("dbname=sports user=postgres")
    cur = conn.cursor()
    query = "SELECT * FROM games WHERE 1=1"
    params = []
    if sport:
        query += " AND sport = %s"
        params.append(sport)
    if date:
        query += " AND date = %s"
        params.append(date)
    cur.execute(query, params)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return {"games": rows}