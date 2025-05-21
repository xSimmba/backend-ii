# app/services/summarizer.py
from app.agents.summarizer_agent import SummarizerAgent

def summarize_text(text: str) -> str:
    agent = SummarizerAgent()
    return agent.run(text)
