from langchain_groq import ChatGroq

from src.core.config import config


llm = ChatGroq(
    model="openai/gpt-oss-20b",
    groq_api_key=config.GROQ_API_KEY,
)
