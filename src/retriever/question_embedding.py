from src.ingestion.vector_store import vector_store 


retriever = vector_store.as_retriever(
    search_type = "similarity", 
    search_kwargs = {"k" : 4} # Retrieve most 2 recent similar chunks 
    )  
# This will create a retriever object which will be used to retrieve the relevant chunks from the vector store based on the question asked by the user 

  # This will retrieve the relevant chunks from the vector store based on the question asked by the user