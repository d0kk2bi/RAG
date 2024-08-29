from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

texts = ["My name = John Doe"]
query = "Who are you?"

embed = OpenAIEmbeddings(model="text-embedding-3-large")

# https://api.python.langchain.com/en/latest/community/vectorstores/langchain_community.vectorstores.faiss.FAISS.html#langchain_community.vectorstores.faiss.FAISS.from_texts
db = FAISS.from_texts(texts, embedding=embed)

# https://api.python.langchain.com/en/latest/community/vectorstores/langchain_community.vectorstores.faiss.FAISS.html#langchain_community.vectorstores.faiss.FAISS.similarity_search
docs = db.similarity_search(query)

print(docs[0].page_content)
