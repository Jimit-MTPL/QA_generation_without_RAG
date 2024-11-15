import os
from llama_index.readers.file import MarkdownReader
from llama_index.core import SimpleDirectoryReader

def data_ingestion(chunk_size=200):
    processed_files_file = 'processed_files.txt'
    input_file = "BS_2_table/BS_2_table.md"

    if not os.path.exists(processed_files_file):
        open(processed_files_file, 'w').close()

    with open(processed_files_file, 'r') as f:
        processed_files = f.read().splitlines()

    if input_file in processed_files:
        print(f"{input_file} has already been processed. Skipping ingestion.")
        return

    parser = MarkdownReader()
    file_extractor = {".md": parser}
    reader = SimpleDirectoryReader(input_files=[input_file], file_extractor=file_extractor)
    documents = reader.load_data()

    # Chunking documents
    for document in documents:
        content = document.get_content()
        for i in range(0, len(content), chunk_size):
            yield content[i:i + chunk_size]

    with open(processed_files_file, 'a') as f:
        f.write(input_file + '\n')
