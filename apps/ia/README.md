# Módulo IA - Chat Conversacional com RAG

Este módulo implementa um sistema de chat conversacional usando CrewAI, LangChain e RAG (Retrieval Augmented Generation) integrado ao sistema RBAC do FastAPI.

## 🚀 Funcionalidades


- **RAG Service**: Sistema de busca semântica com LangChain e FAISS
- **Conversation Agent**: Agente conversacional usando CrewAI
- **API REST**: Endpoints para chat, conversas e documentos
- **Modelos de Dados**: Conversation, Message e Document
- **Integração RBAC**: Conectado ao sistema de autenticação do core
- **Upload de Documentos**: Para alimentar a base de conhecimento

### 🎯 Endpoints Disponíveis

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `POST` | `/chat/chat` | Enviar mensagem e receber resposta da IA |
| `GET` | `/chat/conversations` | Listar conversas do usuário |
| `POST` | `/chat/conversations` | Criar nova conversa |
| `GET` | `/chat/conversations/{id}` | Obter conversa com mensagens |
| `PUT` | `/chat/conversations/{id}` | Atualizar conversa |
| `POST` | `/chat/documents` | Upload de documento |
| `GET` | `/chat/documents` | Listar documentos |
| `GET` | `/chat/search` | Buscar na base de conhecimento |

## 🛠️ Configuração

### 1. Variáveis de Ambiente

```bash
# Obrigatória para usar a IA
GROQ_API_KEY="your_groq_api_key_here"

```

### 1. Chat Simples

```python
from apps.ia.agents.conversation_agent import ConversationAgent
from apps.ia.services.rag_service import RAGService

rag_service = RAGService()
agent = ConversationAgent(rag_service)
response = agent.process_query("Olá, como você está?")
print(response)
```

## 🏗️ Arquitetura

```
apps/ia/
├── agents/             # Agentes CrewAI
│   ├── conversation_agent.py
│   └── __init__.py
├── api/               # Endpoints REST
│   └── chat/
│       ├── controller.py
│       ├── router.py
│       ├── schemas.py
│       └── __init__.py
├── models/            # Modelos SQLAlchemy
│   ├── conversation.py
│   ├── message.py
│   ├── document.py
│   └── __init__.py
├── services/          # Serviços de negócio
│   ├── rag_service.py
│   └── __init__.py
├── tools/             # Ferramentas para agentes
│   ├── rag_search_tool.py
│   └── __init__.py
└── main.py           # Ponto de entrada
```

## 📊 Modelos de Dados

### Conversation
- Armazena conversas entre usuários e IA
- Relacionado ao User via `user_id`
- Contém título, descrição, timestamps

### Message
- Mensagens individuais (user/assistant/system)
- Relacionada à Conversation
- Conteúdo, role e metadados

### Document  
- Documentos da base de conhecimento
- Conteúdo processado pelo RAG
- Hash para evitar duplicatas

## 🧪 Testes

Execute os testes do módulo IA:

```bash
# Testes específicos do IA
pytest tests/test_ia_chat.py -v

# Todos os testes
task test
```


## 🔧 Troubleshooting

### Problema: "GROQ_API_KEY not found"
- Configure a chave da API no arquivo `.env`
- Obtenha uma chave gratuita em https://console.groq.com
