from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

model_name = "ft:gpt-3.5-turbo-0613:lac::7qr3DY9v"
chat = ChatOpenAI(model=model_name)

messages = [
    HumanMessage(content=input("question: "))
]

response = chat(messages)

print(response.content)