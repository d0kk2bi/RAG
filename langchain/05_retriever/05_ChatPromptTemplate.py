from langchain.prompts import ChatPromptTemplate
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI, OpenAIEmbeddings


def format_docs(docs):
    return "\n\n".join([d.page_content for d in docs])


texts = ["My name = John Doe"]
query = "Who are you?"

embed = OpenAIEmbeddings(model="text-embedding-3-large")

db = Chroma.from_texts(
    texts,
    embed,
    collection_name="history",
    persist_directory="./db/",
    collection_metadata={"hnsw:space": "cosine"},
)

retriever = db.as_retriever(search_kwargs={"k": 1})
docs = retriever.invoke(query)


template = """Answer the question based only on the following context:
{context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

llm = ChatOpenAI(
    model="gpt-3.5-turbo-0125",
    temperature=0,
    max_tokens=500,
)

chain = prompt | llm | StrOutputParser()

response = chain.invoke({"context": (format_docs(docs)), "question": query})

print(response)
