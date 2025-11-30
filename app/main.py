from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .agent import agent

class ChatSolicitacao(BaseModel):
    message: str

class ChatResposta(BaseModel):
    response: str

app = FastAPI(
    title="Chat IA + calculos",
    description="API de chat usando Strands Agents + Ollama 3.1",
    version="1.0.0",
)

@app.get("/")
def root():
    return {
        "message": "API de Chat IA + Cálculos está online. Use POST /chat ou acesse /docs para testar."
    }


@app.post("/chat", response_model=ChatResposta)
def chat_endpoint(payload: ChatSolicitacao) -> ChatResposta:
    """Recebe uma mensagem do usuario e retorna a resposta do agente de IA."""
    try:
        result = agent(payload.message)
        msg = result.message

        if isinstance(msg, dict) and "content" in msg:
            textos = []
            for bloco in msg["content"]:
                if isinstance(bloco, dict) and "text" in bloco:
                    textos.append(bloco["text"])
            answer_text = "\n".join(textos).strip()
        else:
            answer_text = str(msg)

        return ChatResposta(response=answer_text)

    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))
