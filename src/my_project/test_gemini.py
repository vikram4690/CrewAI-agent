from src.my_project.llm.gemini_llm import GeminiLLM

if __name__ == "__main__":
    llm = GeminiLLM()
    response = llm.call([{"role": "user", "content": "Explain AI Agents in 3 simple points"}])
    print(response)
