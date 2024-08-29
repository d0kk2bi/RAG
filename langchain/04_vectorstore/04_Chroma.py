from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

texts = ["My name = John Doe"]
query = "Who are you?"

embed = OpenAIEmbeddings(model="text-embedding-3-large")

# https://api.python.langchain.com/en/latest/chroma/vectorstores/langchain_chroma.vectorstores.Chroma.html#langchain_chroma.vectorstores.Chroma.from_texts
db = Chroma.from_texts(
    texts,
    embed,
    collection_name="history",
    persist_directory="./db/",
    collection_metadata={"hnsw:space": "cosine"},  # l2 is the default
)

# https://api.python.langchain.com/en/latest/chroma/vectorstores/langchain_chroma.vectorstores.Chroma.html#langchain_chroma.vectorstores.Chroma.similarity_search
docs = db.similarity_search(query)

print(docs[0].page_content)
