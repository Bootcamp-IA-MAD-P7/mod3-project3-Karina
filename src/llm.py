from langchain_ollama import OllamaLLM
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()


def get_ollama_llm(model: str = None, temperature: float = 0.7) -> OllamaLLM:
    model_name = model or os.getenv("OLLAMA_MODEL", "llama3")
    return OllamaLLM(model=model_name, temperature=temperature)


def get_groq_llm(model: str = None, temperature: float = 0.7) -> ChatGroq:
    model_name = model or os.getenv("GROQ_MODEL", "openai/gpt-oss-20b")
    api_key = os.getenv("GROQ_API_KEY")
    return ChatGroq(model=model_name, temperature=temperature, api_key=api_key)


def get_llm(provider: str = "ollama", model: str = None, temperature: float = 0.7):
    if provider == "groq":
        return get_groq_llm(model=model, temperature=temperature)
    return get_ollama_llm(model=model, temperature=temperature)
