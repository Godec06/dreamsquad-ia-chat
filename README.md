# Chat IA + Cálculos (Teste DreamSquad)

Este projeto é a implementação de um **agente de IA com API em FastAPI**, usando:

- **Strands Agents** como orquestrador do agente
- **Ollama** para rodar o modelo de linguagem localmente
- **Tool de cálculo (`calculator`)** para operações matemáticas
- **FastAPI + Uvicorn** para expor tudo via HTTP

O agente:

- responde em **português**
- conversa sobre **assuntos gerais**
- identifica quando a pergunta é **cálculo numérico**
- usa a *tool* de cálculo para obter o resultado **exato** e depois explica em texto


## 1. Pré-requisitos

- **Python 3.11+**
- **Ollama** instalado e configurado  
  (https://ollama.com)

Depois de instalar o Ollama, baixe o modelo que será usado (por padrão `llama3.1`):

```bash
ollama pull llama3.1
Se a máquina for mais fraca, é possível usar um modelo menor (ex: llama3.2:1b) ajustando o .env.

2. Configuração do ambiente
2.1. Clonar o projeto (ou extrair o zip)
Entre na pasta do projeto, por exemplo:

bash
Copiar código
cd dreamsquad-ia-case
2.2. Criar e ativar o ambiente virtual
bash
Copiar código
python -m venv .venv

# Windows PowerShell
.\.venv\Scripts\activate

2.3. Instalar as dependências
bash
Copiar código
pip install -r requirements.txt
2.4. Arquivo .env
Na raiz do projeto, crie um arquivo chamado .env com algo assim:

env
Copiar código
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL_ID=llama3.1
O prompt padrão do agente está definido em app/config.py na constante DEFAULT_SYSTEM_PROMPT.
Se quiser sobrescrever o prompt via ambiente, é só adicionar no .env:

env
Copiar código
AGENT_SYSTEM_PROMPT=Prompt personalizado aqui...

3. Executando o projeto
3.1. Subir o servidor do Ollama
Se o Ollama não estiver rodando ainda:

bash
Copiar código
ollama serve
(ou abra o aplicativo do Ollama no Windows, que normalmente já sobe o servidor em localhost:11434).

3.2. Subir a API com Uvicorn
Na raiz do projeto:

bash
Copiar código
uvicorn app.main:app --reload
A API ficará disponível em:

http://127.0.0.1:8000

Documentação interativa (Swagger):

http://127.0.0.1:8000/docs

4. Testando o endpoint /chat
4.1. Via Swagger (/docs)
Acesse: http://127.0.0.1:8000/docs

Encontre o endpoint POST /chat

Clique em "Try it out"

Envie um JSON como:

json
Copiar código
{
  "message": "Quanto é 1234 * 5678?"
}
A resposta esperada é algo no formato:

json
Copiar código
{
  "response": "O resultado da multiplicação de 1234 por 5678 é ... (com explicação em texto)."
}
Exemplo de pergunta não matemática:

json
Copiar código
{
  "message": "Me explique em poucas frases o que é inteligência artificial."
}
O agente deve responder em português, sem precisar da tool de cálculo.

4.2. Via curl
bash
Copiar código
curl -X POST "http://127.0.0.1:8000/chat" ^
  -H "Content-Type: application/json" ^
  -d "{\"message\": \"Quanto é 1234 * 5678?\"}"
5. Arquitetura do agente
O comportamento do agente é definido em app/agent.py:

Usa OllamaModel, apontando para o host e o modelo definidos em app/config.py (OLLAMA_HOST e OLLAMA_MODEL_ID).

Usa Strands Agents para orquestrar as chamadas.

Registra a ferramenta de cálculo calculator (do strands-agents-tools).

O system prompt orienta o agente a:

responder perguntas gerais normalmente;

usar a tool de cálculo para contas numéricas (multiplicação, divisão, porcentagem, raiz quadrada etc.);

explicar o resultado em linguagem natural.

O endpoint /chat faz apenas o papel de adaptador HTTP:

Recebe um JSON com message.

Envia o texto para o agente Strands.

Extrai o conteúdo de texto da resposta do agente.

Devolve um JSON com response.

6. Estrutura do projeto
text
Copiar código
.
├── app
│   ├── __init__.py
│   ├── config.py   # Carrega variáveis de ambiente e prompt do agente
│   ├── agent.py    # Criação do agente Strands + Ollama + calculator
│   └── main.py     # API FastAPI com endpoint /chat
├── .env            # Configuração local (não versionar)
├── .env.example    # Exemplo de configuração
├── requirements.txt
├── README.md
└── .gitignore

7. Observações
O modelo padrão configurado é llama3.1.
Se necessário, basta ajustar OLLAMA_MODEL_ID no .env para outro modelo disponível no Ollama.

O projeto foi pensado para ser simples de rodar localmente:

um comando para instalar dependências,

um comando para subir o Ollama,

um comando para rodar a API.

makefile
Copiar código

::contentReference[oaicite:0]{index=0}

```
