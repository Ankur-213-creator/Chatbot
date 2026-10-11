# from langchain_community.document_loaders import TextLoader , PyPDFLoader , Docx2txtLoader

#  TextLoader("data/test.md")  // This is to read the text and md files using TextLoader 
# 
# loader.load()

# loader = TextLoader("data/test.md")
# docs = loader.load()

# -----------------------------------------------------------------

# loader = PyPDFLoader("data/invoice.pdf") // This is to read the pdf files using PyPDFLoader
# docs = loader.load()

# ----------------------------------------------------------------

#loader = Docx2txtLoader("data/document.docx")  // This is to read the docx files using Docx2txtLoader
# docs = loader.load()

# ----------------------------------------------------------------
# print(docs)


# ------------------------------------------------------------------------------------------------------------------------

# This project we have a info about car company and we will create a RAG which can answer based on the avaialbale text docs present for that company 

import os 
from dotenv import load_dotenv

# importing ingestion piepline modules 

from src.ingestion.splitter import chunks  
# Importing the chunks from the splitter module


from src.ingestion.embedding import embeddings  
# Importing the embeddings from the embedding module



from src.ingestion.vector_store import vector_store  
# Importing the vector_store from the vector_store module



# Import retriever pipeline modules  

# Step - 1 : 
from src.retriever.user_question import question  # Importing the question from the retriever module


# Step - 2 , 3 : Cretae Embedding for question and retrieve the relevant chunks from the vector store

from src.retriever.question_embedding import retrieved_docs  
# Importing the retrieved_docs from the question_embedding module


for i, doc in enumerate(retrieved_docs):

    print(f"\n--- Retrieved Document {i+1} ---")

    print(doc.page_content)


# Step - 4 Build Prompt Template ( Create a prompt template to be used for the question answering )

from src.prompts.prompt import formatted_prompt  
# Importing the formatted_prompt from the prompt module


# Step - 5 : Create a LLM ( Sending question to LLM for answer generation )

from src.llms.llm import result  # Importing the result from the llm module



# ====================================

### High level flow for full pipeline 

# indexing / ingestion phase


 #         .txt files
 #         
 #            ↓
 #         
 #         Load documents
 #         
 #            ↓
 #         
 #         Split into chunks
 #         
 #            ↓
 #         
 #         Create embeddings
 #         
 #            ↓
 #         
 #         Store embeddings + text
 #         
 #            ↓
 #         
 #         Chroma DB

# =============================================

# query / retrieval phase




 #          User Question
 #          
 #                ↓
 #          
 #          Question Embedding
 #          
 #                ↓
 #          
 #          Retriever
 #          
 #                ↓
 #          
 #          Chroma searches vectors
 #          
 #                ↓
 #          
 #          Top 4 relevant chunks
 #          
 #                ↓
 #          
 #          Context
 #          
 #                ↓
 #          
 #          Prompt
 #          
 #                ↓
 #          
 #          Groq LLM
 #          
 #                ↓
 #          
 #          Answer


 # Here in this file , we have imported all the things via modules ( We are just importing the modules )