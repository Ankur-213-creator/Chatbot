from fastapi import APIRouter, HTTPException

from src.api.chat_schema import ChatRequest, ChatResponse
from src.retriever.question_embedding import retriever
from src.llms.llm import llm
from src.prompts.prompt import PROMPT_TEMPLATE

router = APIRouter()


@router.post("/ask", response_model=ChatResponse)
def ask_question(request: ChatRequest):

    # Step 1: Get the user's question
    question = request.question.strip()

    # Step 2: Validate the question
    if not question:
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty."
        )

    # Step 3: Retrieve relevant documents
    retrieved_docs = retriever.invoke(question)

    # Step 4: Create context from retrieved documents
    context = "\n\n".join(
        doc.page_content
        for doc in retrieved_docs
        if doc.page_content and doc.page_content.strip()
    )

    # Step 5: Handle cases where no useful context is retrieved
    if not context.strip():
        return ChatResponse(
            answer="I don't know. No relevant information was found in the documents."
        )

    # Step 6: Insert the context and question into the prompt
    formatted_prompt = PROMPT_TEMPLATE.format(
        context=context,
        question=question
    )

    # Step 7: Send the prompt to the LLM
    response = llm.invoke(formatted_prompt)

    # Step 8: Return the answer
    return ChatResponse(answer=response.content)
