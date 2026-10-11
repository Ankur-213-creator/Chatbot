import os 
from dotenv import load_dotenv

load_dotenv() # It will load the enviornment

class Config:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # Retrieving the GROQ API key from environment variables
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")  # Retrieving the Google API key from environment variables



# Creating instance of this class 


config = Config()


# Here idea is like : Remove as many hardcoded value as we can , define all the constants hardcoded values as 
# Member in this confog class and then import via class name 

# e.g : config.GROQ_API_KEY , config.GOOGLE_API_KEY  etc