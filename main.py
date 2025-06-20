from agents import SportAgent, OrchestratorAgent
from config import API_CONFIG
from crewai import Task

def run_swarm(task_type="fetch_historical"):
    agents = [SportAgent(sport, API_CONFIG[sport]) for sport in API_CONFIG]
    orchestrator = OrchestratorAgent(agents)
    results = orchestrator.run(Task(name=task_type))
    return results

if __name__ == "__main__":
    print(run_swarm())