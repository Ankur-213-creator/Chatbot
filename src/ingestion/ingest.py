# Step -1 : Document Loading ( Muliple docs via DirectoryLoader ) 

from google import genai
from langchain_community.document_loaders import TextLoader , DirectoryLoader

loader = DirectoryLoader ( 
"data/" , 
glob = "**/*.txt", 
loader_cls = TextLoader
)  

docs = loader.load()


# Here we are reading all the files present in the data folder using TextLoader 
# For reading multiple files we use DirectoryLoader and specify the glob pattern to read all the files with .txt extension