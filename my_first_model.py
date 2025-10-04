from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(
    model="gpt-5",
    temperature=0.7
)

mensagens = [
    SystemMessage(content="Você é um contador de histórias criativo."),
    HumanMessage(content="Conte uma história breve sobre O Senhor dos Anéis.")
]

resposta = llm.invoke(mensagens)
print(resposta.content)