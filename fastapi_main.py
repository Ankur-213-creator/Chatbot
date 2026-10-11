from fastapi import FastAPI
from pydantic import BaseModel
from src.api.chat_router import router  # Importing the router from the chat_router module

app = FastAPI()
app.include_router(router)

# Creating a endpoint which will return some msg 


