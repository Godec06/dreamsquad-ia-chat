from strands import Agent
from strands.models.ollama import OllamaModel
from strands_tools import calculator

from .config import OLLAMA_HOST, OLLAMA_MODEL_ID, AGENT_SYSTEM_PROMPT

def create_agent() -> Agent:

    model = (
        OllamaModel(host=OLLAMA_HOST,model_id=OLLAMA_MODEL_ID))

    agent = Agent(model, tools=[calculator], system_prompt=AGENT_SYSTEM_PROMPT)

    return agent


#Utilizar Instancia na api
agent = create_agent()


#teste do agente - python -m app.agente
if __name__ == "__main__":
    print("Faça sua pergunta.\n")
    while True:
        user_input = input("Digite: ").strip()
        if not user_input:
            break

        try:
            response = agent(user_input)
            print(f"Agente: {response.message}\n")
        except Exception as e:
            print(f"[Deu ruim] {e}\n")
