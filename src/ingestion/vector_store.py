from src.ingestion.embedding import embeddings 
from src.ingestion.splitter import chunks 
from langchain_chroma import Chroma

# Step - 4 : Store the embeddings into vector database ( Chroma DB ) 

# Storing chunks along with thie embeddings into vector database for retrieval

vector_store = Chroma.from_documents(
    documents = chunks,
    embedding = embeddings,
    persist_directory = "data/chroma_db"        # To save all the data inside this path 
)

# print(vector_store)  # It will print the vector store object