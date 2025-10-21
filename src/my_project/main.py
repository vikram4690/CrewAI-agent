from src.my_project.crew import create_crew
from src.my_project.tools.custom_tool import hello_tool

if __name__ == "__main__":
    print(hello_tool("Vikram"))  # test custom tool

    crew = create_crew()
    result = crew.kickoff()
    print("\n=== Agent Result ===")
    print(result)
