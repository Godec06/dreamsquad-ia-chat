import os
from dotenv import load_dotenv
load_dotenv()

OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")

OLLAMA_MODEL_ID = os.getenv("OLLAMA_MODEL_ID", "llama3.1")

DEFAULT_SYSTEM_PROMPT = """ 
Você é um assiste em português.

Voce consegue conversas sobre assunto gerais e responder perguntas de conhecimento comum apenas usando a modelo de linguagem.

Quando a pergunta do usuario envolver operações numericas, como somar, subtrair, multiplicar, dividir, calcular porcetagem ou raiz quadrada,
voce deve usar a ferramenta de calcular 'calculator' para obter o resultado exato e, em seguida, explicar o resultado em linguagem natural para o usuário.
"""

AGENT_SYSTEM_PROMPT = os.getenv("AGENT_SYSTEM_PROMPT", DEFAULT_SYSTEM_PROMPT)

