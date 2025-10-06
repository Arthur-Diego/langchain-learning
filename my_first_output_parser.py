from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()

chat = ChatOpenAI(
    model="gpt-5",
    temperature=0.7
)

class Review(BaseModel):
    produto: str = Field(
        description="Breve descrição do produto"
    )
    entrega: str = Field(
        description="Cliente ficou satisfeito com a entrega"
    )
    produto_satisfacao: str = Field(
        description="Cliente ficou satisfeito com o produto"
    )
    atendimento: str = Field(
        description="Cliente ficou satisfeito com o atendimento"
    )
    satisfacao: str = Field(
        description="Satisfação geral do cliente com a compra"
    )


review = """Este soprador de folhas é bastante incrível. 
Ele tem quatro configurações: sopro de vela, brisa suave, 
cidade ventosa e tornado. 
Chegou em dois dias, bem a tempo para o presente de aniversário da minha esposa. 
Acho que minha esposa gostou tanto que ficou sem palavras. 
Até agora, fui o único a usá-lo, e tenho usado em todas as manhãs alternadas para 
limpar as folhas do nosso gramado. 
É um pouco mais caro do que os outros sopradores de folhas disponíveis no mercado, 
mas acho que vale a pena pelas características extras.
"""


llm_estrurada = chat.with_structured_output(Review)
repostaa = llm_estrurada.invoke(review)
print(repostaa)

