import os

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter

path = "test.txt"

loader = TextLoader(file_path=path)
data = loader.load()

print("base content:", data[0].page_content)

# https://api.python.langchain.com/en/latest/text_splitters/character/langchain_text_splitters.character.CharacterTextSplitter.html#charactertextsplitter
text_splitter = CharacterTextSplitter(
    separator=" ",
    chunk_size=500,
    chunk_overlap=100,
    length_function=len,
)

texts = text_splitter.split_text(data[0].page_content)

print("split content:", texts[0])
