import os

from bs4 import SoupStrainer
from langchain_community.document_loaders import WebBaseLoader

url1 = "http://example.com/"
url2 = "https://www.example.com/"

# https://api.python.langchain.com/en/latest/community/document_loaders/langchain_community.document_loaders.web_base.WebBaseLoader.html#webbaseloader
# If load one web path
loader = WebBaseLoader(web_path=url1)

# Can load multiple web paths
loader = WebBaseLoader(web_paths=[url1, url2])

# Can use bs4 with bs_kwargs
loader = WebBaseLoader(
    web_paths=[url1, url2],
    bs_kwargs=dict(parse_only=SoupStrainer("h1")),
)

# Return a list of documents
docs = loader.load()

print("content:", docs[0].page_content)
print("metadata:", docs[0].metadata)
