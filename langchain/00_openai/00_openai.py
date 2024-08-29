import os

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

# If you set OPENAI_API_KEY in your environment variables, you can skip the api_key argument
# https://python.langchain.com/v0.2/docs/tutorials/llm_chain/#using-language-models
# https://api.python.langchain.com/en/latest/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html#langchain-openai-chat-models-base-chatopenai
model = ChatOpenAI(model="gpt-3.5-turbo-0125")

messages = [
    SystemMessage(content="Translate the following from English into Italian"),
    HumanMessage(content="hi!"),
]

stream = model.invoke(messages)
print(stream)
