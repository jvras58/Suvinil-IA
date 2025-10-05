<h1 align="center">

## 🎨 Suvinil IA - Sistema Inteligente de Recomendação de Tintas

Solução inovadora para o desafio Suvinil: sistema de recomendação inteligente de tintas baseado em análise de ambiente usando IA. Backend FastAPI com agentes CrewAI que analisam descrições de ambiente (cheiro, lavabilidade, superfície, clima, preferências de cor) e recomendam produtos Suvinil ideais via RAG. Arquitetura robusta com RBAC, JWT, auditoria e observabilidade.
</h1>

<p align="center">
   🏆 Desenvolvido para o Desafio Loomi 20205 - Transformando a experiência de escolha de tintas através de Inteligência Artificial
</p>

<p align="center">
  <a href="#📝-sobre-o-projeto">Sobre o Projeto</a> •
  <a href="#🚀-tecnologias">Tecnologias</a> •
  <a href="#📋-requisitos">Requisitos</a> •
  <a href="#🔧-arquitetura">Arquitetura</a> •
  <a href="#⚙️-como-usar">Como Usar</a> •
  <a href="#🤝-como-contribuir">Como Contribuir</a> •
  <a href="#📄-licença">Licença</a>
</p>

---

## 🏆 Desafio Suvinil

**Problema**: Como ajudar consumidores a escolher a tinta ideal para suas necessidades específicas?

**Solução**: Sistema IA que analisa descrições detalhadas do ambiente e necessidades do usuário:
- 📝 **Input**: Usuário descreve ambiente (cheiro, lavabilidade, superfície, clima, preferências de cor)
- 🤖 **Processamento**: Agentes CrewAI especializados processam a descrição usando RAG com base de conhecimento Suvinil
- 🎯 **Output**: Recomendações justificadas de produtos Suvinil com explicação técnica

**Arquitetura**: Sistema robusto com autenticação, autorização, auditoria completa e containerização.

### 🎯 Funcionalidades Principais

#### 🤖 Sistema de Recomendação Inteligente
- **Análise de Ambiente**: Processamento de descrições detalhadas de ambientes usando NLP
- **Recomendação de Produtos**: Sugestões personalizadas de tintas Suvinil baseadas em RAG
- **Justificativas Técnicas**: Explicações detalhadas sobre por que cada produto foi recomendado
- **Agentes Especializados**: CrewAI com agentes específicos para diferentes aspectos (cor, durabilidade, aplicação)

#### 🔐 Sistema de Segurança Robusto  
- **Autenticação JWT**: Login seguro de usuários com tokens de acesso
- **Autorização RBAC**: Controle granular de acesso baseado em papéis e permissões
- **Auditoria Completa**: Rastreamento de todas as interações (usuário, IP, timestamps)

#### 👥 Gestão de Usuários e Permissões
- **Gerenciamento de Usuários**: CRUD completo para usuários do sistema
- **Gestão de Papéis**: Atribuição flexível de papéis e permissões
- **Controle de Acesso**: Validação de permissões em tempo real

#### 🧪 Qualidade e Observabilidade
- **Testes Automatizados**: Cobertura completa com pytest
- **Containerização**: Deploy fácil com Docker e Docker Compose
- **Monitoramento**: Logs estruturados e métricas de desempenho

O projeto é estruturado para ser modular, escalável e seguir boas práticas de desenvolvimento, como separação de responsabilidades e uso de ferramentas modernas de desenvolvimento Python.

---

## 🚀 Tecnologias

### 🤖 Stack de Inteligência Artificial
- **[CrewAI](https://crewai.com/)**: Framework para orquestração de agentes IA especializados
- **[LangChain](https://langchain.com/)**: Framework para desenvolvimento de aplicações com LLMs
- **[Groq](https://groq.com/)**: Plataforma de inferência de IA com Llama 3.1 8B Instant
- **RAG (Retrieval-Augmented Generation)**: Sistema de recuperação e geração aumentada
- **NLP (Natural Language Processing)**: Processamento de linguagem natural para análise de texto

### 🛠️ Stack Backend e Infraestrutura
- **Linguagem**: [Python 3.12](https://www.python.org/) - Linguagem principal do projeto
- **Framework Web**: [FastAPI](https://fastapi.tiangolo.com/) - API moderna e de alta performance
- **ORM**: [SQLAlchemy](https://www.sqlalchemy.org/) - Mapeamento objeto-relacional avançado
- **Banco de Dados**: [SQLite](https://sqlite.org/) / [PostgreSQL](https://postgresql.org/) - Flexibilidade entre desenvolvimento e produção

### 🔧 Ferramentas de Desenvolvimento
- **Gerenciador de Dependências**: [UV](https://docs.astral.sh/uv/) - Gerenciamento moderno de dependências Python
- **Migrações**: [Alembic](https://alembic.sqlalchemy.org/) - Controle de versão de banco de dados
- **Testes**: [pytest](https://pytest.org/) + [pytest-cov](https://pytest-cov.readthedocs.io/) - Testes automatizados com cobertura
- **Code Quality**: [Ruff](https://github.com/charliermarsh/ruff) + [isort](https://pycqa.github.io/isort/) - Linting e formatação
- **Containerização**: [Docker](https://docker.com/) + [Docker Compose](https://docs.docker.com/compose/) - Deploy e orquestração

### 🔐 Segurança e Autenticação  
- **JWT**: [python-jose](https://github.com/mpdavis/python-jose) - Tokens de autenticação seguros
- **Hashing**: [bcrypt](https://pypi.org/project/bcrypt/) - Hash seguro de senhas
- **RBAC**: Sistema próprio de controle de acesso baseado em papéis

---

## 📋 Requisitos

Para rodar ou contribuir com o projeto, você precisará das seguintes ferramentas instaladas:

| Ferramenta                                         | Versão       | Instalação (Linux/macOS)                     |
|----------------------------------------------------|--------------|----------------------------------------------|
| [Python](https://www.python.org/)                  | 3.12       | `asdf install python 3.12` ou similar      |
| [UV](https://docs.astral.sh/uv/)                   | Latest       | `curl -LsSf https://astral.sh/uv/install.sh | sh |
| [Git](https://git-scm.com/)                        | Latest       | `sudo apt install git` (Linux) ou `brew install git` (macOS) |
| [SQLite](https://sqlite.org/)                      | Latest       | Geralmente pré-instalado, ou `sudo apt install sqlite3` |

**Nota**: Recomendamos o uso do `asdf` para gerenciar versões do Python. Consulte o arquivo `.python-version` para a versão exata do Python utilizada.

---

## 🔧 Arquitetura

A estrutura do projeto é organizada para promover modularidade e facilitar a manutenção. Abaixo está a organização dos arquivos e diretórios:

```bash
FastAPI/
├── apps/                        # Aplicações do monólito
│   ├── core/                    # 🔐 API REST com RBAC
│   │   ├── api/                 # Endpoints da API
│   │   │   ├── assignment/      # 👥 Designações (usuário-papel)
│   │   │   ├── authentication/  # 🔑 Autenticação (login, JWT)
│   │   │   ├── authorization/   # ✅ Autorizações (papel-transação)
│   │   │   ├── role/            # 🏷️ Gerenciamento de papéis
│   │   │   ├── transaction/     # 📋 Gerenciamento de transações
│   │   │   ├── user/            # 👤 Gerenciamento de usuários
│   │   │   └── text_processing/ # 🔄 Processamento de texto (bridge para IA)
│   │   ├── database/            # 🗄️ Configuração SQLAlchemy
│   │   ├── models/              # 📊 Modelos ORM (User, Role, etc.)
│   │   ├── utils/               # 🛠️ Utilitários (segurança, configs)
│   │   └── startup.py           # 🚀 Inicialização FastAPI
│   │
│   ├── ia/                      # 🤖 Serviço de Agentes IA
│   │   ├── agents/              # 🧠 Definição dos agentes CrewAI
│   │   ├── api/                 # 🌐 Endpoints específicos da IA
│   │   │   └── chat/            # 💭 Chat com agentes
│   │   ├── models/              # 📈 Modelos específicos da IA
│   │   ├── services/            # ⚙️ Serviços da IA
│   │   │   └── rag_service.py   # 🔍 RAG com LangChain
│   │   └── tools/               # 🔧 Ferramentas para agentes
│   │       └── rag_search_tool.py # 🔎 Ferramenta de busca RAG
│   │
│   └── packpage/                # 📦 Utilitários compartilhados
│       ├── base_model.py        # 🏗️ Modelo base com auditoria
│       ├── llm.py               # 🧮 Configuração LLM (Groq)
│       └── generic_controller.py # 🎮 Controller genérico CRUD
│
├── migrations/                  # 🔄 Migrações Alembic
├── scripts/                     # 📜 Scripts de automação
├── seeds/                       # 🌱 Dados iniciais
├── tests/                       # 🧪 Testes automatizados
│   ├── factory/                 # 🏭 Factories para testes
│   └── conftest.py              # ⚙️ Configuração pytest
├── DOCS/                        # 📚 Documentação
│   ├── PERMISSIONS.MD           # 🔐 Guia RBAC
│   ├── FLUXOGRAMA.MD           # 🔄 Fluxos da aplicação
│   └── DEPLOYMENT.md            # 🚀 Deploy em produção
├── .devcontainer/               # 🐳 Configuração dev container
├── .secrets/                    # 🔒 Arquivos sensíveis
├── .env-semple                  # 📋 Template de configuração
├── alembic.ini                  # ⚙️ Configuração Alembic
├── uv.lock                      # 🔒 Lockfile dependências
└── pyproject.toml               # 📦 Configuração projeto
```

### Modelo de Dados
O projeto utiliza um modelo de dados baseado em RBAC, com as seguintes entidades principais:
- **User**: Representa os usuários do sistema.
- **Role**: Papéis que definem permissões.
- **Assignment**: Associa usuários a papéis.
- **Transaction**: Operações do sistema (ex.: criar, listar, excluir).
- **Authorization**: Associa papéis a transações, definindo permissões.

---

## 📚 Documentação Técnica

Para informações técnicas detalhadas sobre o projeto, consulte os documentos específicos:

### 📊 **Modelo de Entidades e Relacionamentos**
- **Diagrama ER**: [DOCS/MODELS.png](DOCS/MODELS.png) - Visualização completa das entidades e seus relacionamentos no banco de dados.

### 🔐 **Sistema de Permissões (RBAC)**
- **Guia Completo**: [DOCS/PERMISSIONS.MD](DOCS/PERMISSIONS.MD) - Documentação detalhada sobre:
  - Como um usuário novo ganha permissões
  - Como criar novas permissões no sistema
  - Estrutura hierárquica de roles
  - Cenários práticos de uso
  - Sistema de segurança e validações

### 🔄 **Fluxograma da Aplicação**
- **Fluxo Técnico**: [DOCS/FLUXOGRAMA.MD](DOCS/FLUXOGRAMA.MD) - Mapeamento completo dos fluxos da aplicação:
  - Pontos de entrada (endpoints)
  - Pontos de decisão (middlewares e validações)
  - Pontos de saída (respostas e persistência)
  - Agrupamentos naturais do sistema

### 🚀 **Deploy**
- **Guia Completo**: [DOCS/DEPLOYMENT.md](DOCS/DEPLOYMENT.md) - Documentação detalhada sobre:
  - Configuração do ambiente de produção com Docker
  - Setup com PostgreSQL e Docker Compose
  - Comandos para gerenciamento de containers
  - Backup e restauração do banco de dados
  - Considerações de segurança e performance
  - Troubleshooting de problemas comuns

---

## ⚙️ Como Usar

Siga os passos abaixo para configurar e executar o projeto localmente.

### 1. Clonar o Repositório
```bash
git clone https://github.com/jvras58/fastapi-crewai
cd fastapi-crewai
```

## 2.1 Montando o ambiente

Este repositório esta organizando em um devcontainer.
E para instacia-lo no VSCODE é recomendado as seguintes configurações:

#### Extenções recomendadas

- Name: Remote Development
- Id: ms-vscode-remote.vscode-remote-extensionpack
- Description: An extension pack that lets you open any folder in a container, on a remote machine, or in WSL and take advantage of VS Code's full feature set.
- Version: 0.25.0
- Publisher: Microsoft
- VSCode Marketplace Link: https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack

#### Docker Engine

É obrigatório ter o Docker Engine já instalado e cunfigurado. Para mais informações de como instalar o Docker Engine em seu SO, ver em:

- Instruções para instalação do Docker Engine: [Ver o link](https://docs.docker.com/engine/install/)

#### Procedimento para instanciar o projeto no VSCODE
1. Com o pack de extenções instalado,
1. Realize o clone/fork deste repositório,
1. Abra o diretorio deste repositorio no VSCODE como um projeto,
1. Use o Comando _Dev Containers: Reopen in Container_ da paleta de comandos do VSCODE. _(F1, Ctrl+Shift+P)_.

Depois da compilação do container o VSCode abrirá o repositório em um ambiente encapsulado e executando diretamente de dentro do container como configurado nas definições do **/.devconainer**.

---

### 2.2 Configurar o Ambiente
Crie o arquivo `.env` baseado no modelo fornecido:
```bash
cp .env-semple .env
```

Edite o arquivo `.env` com as configurações adequadas. Exemplo:
```plaintext
DB_URL="sqlite:///database.db"
SECURITY_ALGORITHM="HS256"
SECURITY_ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Crie o diretório `.secrets` e adicione o arquivo `SECURITY_API_SECRET_KEY` com um valor seguro:
```bash
mkdir .secrets
echo "SUA_CHAVE_SECRETA_AQUI" > .secrets/SECURITY_API_SECRET_KEY
```

### 3. Instalar Dependências
Ative o ambiente virtual e instale as dependências com o UV:
```bash
uv sync
uv install
```
> Entre no ambiente virtual: source activate_env.sh

### 4. Aplicar Migrações
Execute as migrações para criar as tabelas no banco de dados:
A) aplique as migrations existentes:
```bash
alembic upgrade head
```
b) Suba os seedings de RBAC e de usuario admin
```bash
task setup_db
```

### 5. Executar a API
Inicie o servidor FastAPI com o comando:
```bash
task run
```

A API estará disponível em:
- **URL Local**: [http://localhost:8000](http://localhost:8000)
- **Documentação Interativa**: [http://localhost:8000/api/v1/docs](http://localhost:8000/api/v1/docs) (Swagger UI)
- **Documentação Alternativa**: [http://localhost:8000/api/v1/redoc](http://localhost:8000/api/v1/redoc) (ReDoc)

### 6. Executar Testes
Para rodar os testes automatizados e verificar a cobertura:
```bash
task test
```

O relatório de cobertura será gerado em `htmlcov/index.html`.

---

## 🤝 Como Contribuir

Contribuições são sempre bem-vindas! Para contribuir com o projeto:

1. **Fork** o repositório
2. Crie uma **branch** para sua feature (`git checkout -b feature/nova-feature`)
3. **Commit** suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. **Push** para a branch (`git push origin feature/nova-feature`)
5. Abra um **Pull Request**

### Padrões de Contribuição
- Siga as convenções de código estabelecidas
- Escreva testes para novas funcionalidades
- Mantenha a documentação atualizada
- Use mensagens de commit descritivas

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE). Veja o arquivo `LICENSE` para mais detalhes.

---

## 💬 Contato

Se tiver dúvidas ou sugestões, entre em contato:
- **Autores**: jvras <jvras58@gmail.com>
