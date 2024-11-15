from llama_index.core.memory import ChatMemoryBuffer
from llama_index.core.chat_engine import SimpleChatEngine

def create_chat_engine():
    # Initialize memory if required in the future
    #memory = ChatMemoryBuffer.from_defaults(token_limit=1500)
    chat_engine = SimpleChatEngine.from_defaults(system_prompt = """
    You are tasked with generating high-quality, meaningful question-answer pairs from the provided user's query. 
    The questions should cover all key points in the text, be diverse, and not repetitive. 
    The answers should be detailed, conversational, accurate, and provide explanations where necessary. 
    Avoid using wording that directly refers back to the text (like "according to the text"). 
    Ensure each question is unique and comprehensive.

    Format your response like this:
    Question: [Insert question here]
    Answer: [Insert detailed, conversational answer here]

    Make sure:
    1. Each question addresses a different key aspect or detail from the text.
    2. The answers are well-explained, providing context or additional information when necessary.
    3. Both questions and answers should be clear and specific without direct references to phrases from the text.
    4. The questions should be open-ended (who, what, when, where, why, how) and encourage detailed responses.
                                                 
    generate maximum 3 question-answer pairs from the provided user's query.
    """
    )
    
    # Defining the system prompt (this replaces the need to pass query each time)
    
    return chat_engine

def interact_with_llm(chunk):
    print(chunk)  # Printing part of the chunk for clarity
    chat_engine = create_chat_engine()
    AgentChatResponse = chat_engine.chat(chunk)
    answer = AgentChatResponse.response
    return answer
