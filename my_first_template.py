from langchain.chains.summarize.map_reduce_prompt import prompt_template
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(
    model="gpt-5",
    temperature=0.7
)

# prompt_template =PromptTemplate.from_template('''
#     Response a seguinte pergunta do usuario:
# {pergunta}
# ''')

# print(prompt_template.format(pergunta='''O que é um buraco negro'''))


temlate_word_count =PromptTemplate.from_template('''
    Response a pergunta em até {n_words} palavras:
''')

template_language =PromptTemplate.from_template('''
    Retorna a resposta em {language}
''')

template_final = (
    temlate_word_count +
    template_language +
    'Reponda a pergunta seguinte seguindo as instruções: {question}'
)

prompt = template_final.format(n_words=10, language='English', question='O que é uma estrela?')
answer = llm.invoke(prompt)
print(answer.content)