from crewai import Agent, Task
from llm import ask_llm
from ingest import fetch_historical_data, fetch_realtime_data, fetch_realtime_player_data
from e2b_context import get_e2b_context, write_to_e2b_file
from storage import store_game, store_player_event
from process import process_game_data, process_player_event

class SportAgent(Agent):
    def __init__(self, sport, api_config):
        super().__init__(name=f"{sport.capitalize()}Agent")
        self.sport = sport
        self.api_config = api_config

    def run(self, task: Task):
        ctx = get_e2b_context()
        # LLM decides what to fetch
        llm_prompt = (
            f"You are the {self.sport} agent. Task: {task.name}. "
            f"e2b context: {ctx}. Should you fetch historical, realtime, or player_realtime data? "
            f"Provide a one-word answer: 'historical', 'realtime', or 'player'."
        )
        decision = ask_llm(llm_prompt).strip().lower()
        if decision == "historical" or task.name == "fetch_historical":
            data = fetch_historical_data(self.sport, self.api_config)
            processed = [process_game_data(game) for game in data if isinstance(game, dict) and game.get("GameID")]
            for game in processed:
                store_game(game, self.sport)
            if ctx:
                write_to_e2b_file(f"{self.sport}_historical.json", str(processed))
            summary = ask_llm(f"Summarize the following {self.sport} game data:\n{str(processed)[:1000]}")
            return {"data": processed, "summary": summary}
        elif decision == "realtime" or task.name == "fetch_realtime":
            data = fetch_realtime_data(self.sport, self.api_config)
            if ctx:
                write_to_e2b_file(f"{self.sport}_realtime.json", str(data))
            return {"data": data, "note": "Realtime data (stub/demo)"}
        elif decision == "player" or task.name == "fetch_player_realtime":
            player_events = fetch_realtime_player_data(self.sport, self.api_config)
            processed = [process_player_event(ev) for ev in player_events]
            for ev in processed:
                store_player_event(ev, self.sport)
            if ctx:
                write_to_e2b_file(f"{self.sport}_player_realtime.json", str(processed))
            summary = ask_llm(f"Summarize the following {self.sport} player event data:\n{str(processed)[:1000]}")
            return {"player_events": processed, "summary": summary}
        else:
            return {"error": "Unknown task."}