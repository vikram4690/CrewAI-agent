from crewai import Agent, Task, Crew
import yaml
from pathlib import Path
from src.my_project.tools.custom_tool import hello_tool
from src.my_project.llm.gemini_llm import GeminiLLM

def load_yaml(file_path):
    with open(file_path, "r") as f: 
        return yaml.safe_load(f)

def create_crew():
    # Load YAML configs
    config_dir = Path(__file__).parent / "config"
    agents_config = load_yaml(config_dir / "agents.yaml")
    tasks_config = load_yaml(config_dir / "tasks.yaml")

    # Create Gemini LLM
    gemini_llm = GeminiLLM()

    # Define agent
    researcher_cfg = agents_config["researcher"]

    researcher = Agent(
        role=researcher_cfg["role"],
        goal=researcher_cfg["goal"],
        backstory=researcher_cfg["backstory"],
        llm=gemini_llm,  # ✅ CrewAI now fully recognizes it
        verbose=True,
    )

    # Define task
    task_cfg = tasks_config["summarize_task"]
    summarize_task = Task(
        description=task_cfg["description"],
        expected_output=task_cfg["expected_output"],
        agent=researcher,
    )

    # Build Crew
    crew = Crew(
        agents=[researcher],
        tasks=[summarize_task],
    )
    return crew
