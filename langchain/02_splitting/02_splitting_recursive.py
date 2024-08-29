import os

from langchain_community.document_loaders import TextLoader

# langchain_text_splitters package separated with langchain package
# langchain.text_splitter -> langchain_text_splitters (< langchain v0.1.11)
from langchain_text_splitters import CharacterTextSplitter

path = "test.txt"

loader = TextLoader(file_path=path)
data = loader.load()

print("base content:", data[0].page_content)

# https://api.python.langchain.com/en/latest/text_splitters/base/langchain_text_splitters.base.TextSplitter.html#textsplitter
# https://api.python.langchain.com/en/latest/text_splitters/character/langchain_text_splitters.character.RecursiveCharacterTextSplitter.html#recursivecharactertextsplitter
# https://python.langchain.com/v0.1/docs/modules/data_connection/document_transformers/recursive_text_splitter/
# Splitting text by recursively look at characters
text_splitter = CharacterTextSplitter(
    chunk_size=50,  # Maximum size of chunks to return
    chunk_overlap=10,  # Overlap in characters between chunks
    length_function=len,  # Function that measures the length of given chunks
    is_separator_regex=False,
)

texts = text_splitter.split_text(data[0].page_content)

print("split content:", texts)
