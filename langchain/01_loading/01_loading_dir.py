import os

from langchain_community.document_loaders import DirectoryLoader

path = "./"
glob = "*.txt"

# https://api.python.langchain.com/en/latest/community/document_loaders/langchain_community.document_loaders.directory.DirectoryLoader.html#directoryloader
# Required 'unstructured'
# If not work in Windows, check:
# https://github.com/Yelp/elastalert/issues/1927#issuecomment-1477301855
loader = DirectoryLoader(path=path, glob=glob)
data = loader.load()

print("content:", data[0].page_content)
print("metadata:", data[0].metadata)
