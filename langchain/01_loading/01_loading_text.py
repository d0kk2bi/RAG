import os

from langchain_community.document_loaders import TextLoader

path = "test.txt"

# https://api.python.langchain.com/en/latest/community/document_loaders/langchain_community.document_loaders.text.TextLoader.html#textloader
loader = TextLoader(file_path=path)
data = loader.load()

print("content:", data[0].page_content)
print("metadata:", data[0].metadata)
