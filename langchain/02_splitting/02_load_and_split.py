import os

from langchain_community.document_loaders import TextLoader

# langchain_text_splitters package separated with langchain package
# langchain.text_splitter -> langchain_text_splitters (< langchain v0.1.11)
from langchain_text_splitters import CharacterTextSplitter

path = "test.txt"

loader = TextLoader(file_path=path)

text_splitter = CharacterTextSplitter(
    separator="\n",  # A user defined separator
    chunk_size=50,  # Maximum size of chunks to return
    chunk_overlap=0,  # Overlap in characters between chunks
    length_function=len,  # Function that measures the length of given chunks
)

# https://api.python.langchain.com/en/latest/community/document_loaders/langchain_community.document_loaders.text.TextLoader.html#langchain_community.document_loaders.text.TextLoader.load_and_split
data = loader.load_and_split(text_splitter=text_splitter)

print("split content:", data)
