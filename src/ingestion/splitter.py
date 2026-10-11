from google import genai
from langchain_community.document_loaders import TextLoader , DirectoryLoader
from src.ingestion.ingest import docs

# Step - 2 : Text Splitting ( Split docs into Chunks )

from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000 ,
    chunk_overlap = 200 
)
chunks = text_splitter.split_documents(docs)