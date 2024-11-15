import os
from engine_create import interact_with_llm
from llama_index.llms.ollama import Ollama
from ingestion import data_ingestion
from llama_index.core import Settings

# Initialize the LLM settings
Settings.llm = Ollama(model="llama3.2:1b", request_timeout=1000)

def main():
    # Load and process the data in chunks
    for chunk in data_ingestion():  # Assuming data_ingestion yields document chunks
        # Automatically interact with the LLM based on system prompt
        output = interact_with_llm(chunk)
        print("LLM Response:")
        print(output)  # Print the response from LLM for each chunk

if __name__ == "__main__":
    main()
