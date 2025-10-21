import os
from crewai.llm import LLM
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class GeminiLLM(LLM):
    def __init__(self, model="gemini-pro-latest", temperature=0.7):
        super().__init__(model=model)  # Pass model to CrewAI LLM base
        self.temperature = temperature
        self.stop = []

    def call(self, messages, **kwargs):
        prompt = "\n".join([f"{m['role'].capitalize()}: {m['content']}" for m in messages])
        model_obj = genai.GenerativeModel(self.model)
        response = model_obj.generate_content(
            prompt,
            generation_config={"temperature": self.temperature}
        )
        return response.text if hasattr(response, "text") else "No response."
