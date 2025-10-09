"""Conversation Agent using CrewAI with optimizations."""

import os

from crewai import Agent, Crew, Process, Task
from langchain.memory import ConversationBufferMemory

from apps.ia.services.rag_service import RAGService
from apps.ia.utils.load_yaml import load_agent_prompt
from apps.packpage.llm import get_llm

memory = ConversationBufferMemory(
    memory_key='chat_history', return_messages=True
)



class ConversationAgent:
    """Agente de conversa otimizado, agora com prompt carregado via YAML."""

    def __init__(self, rag_service: RAGService = None, prompt_path: str = None):
        self.rag_service = rag_service or RAGService()
        self.llm = get_llm()
        if prompt_path is None:
            prompt_path = os.path.join(
                os.path.dirname(__file__),
                "..",
                "utils",
                "prompts",
                "conversation_agent_prompt.yaml",
            )
        self.prompt_path = prompt_path
        self.prompt = load_agent_prompt(self.prompt_path)

    def create_conversation_agent(self) -> Agent:
        """Cria o agente de conversa usando o prompt do YAML."""
        backstory_base = self.prompt.get(
            "backstory", "Especialista em tintas Suvinil com contexto mantido."
        )
        examples = self.prompt.get("examples", [])
        if examples:
            backstory_base += "\n\nExemplos de respostas:\n"
            for ex in examples:
                backstory_base += (
                    f"- Pergunta: {ex['question']}\n  Resposta: {ex['answer']}\n"
                )

        return Agent(
            role=self.prompt.get(
                "role", "Agente de Conversa especialista em tintas Suvinil"
            ),
            goal=self.prompt.get(
                "objective", "Interpretar intenções e responder naturalmente em PT-BR"
            ),
            backstory=backstory_base,
            # tools=[rag_search_tool, db_query_tool],
            tools=[],
            llm=self.llm,
            verbose=False,
            max_iter=3,
            memory=memory,
        )

    def process_query(self, query: str) -> str:
        """Process a user query with single task to minimize API calls."""
        if not query or not query.strip():
            return 'Por favor, faça uma pergunta para que eu possa ajudá-lo.'

        agent = self.create_conversation_agent()

        task = Task(
            description=(
                f"Analise '{query}'. Use tools apenas se necessário "
                '(DB para dados estruturados, RAG para documentos). '
                'Responda diretamente se possível, sem chamadas extras.'
            ),
            agent=agent,
            expected_output='Resposta final concisa à query.',
        )

        crew = Crew(
            agents=[agent],
            tasks=[task],
            process=Process.sequential,
            verbose=1,
            cache=True,
        )

        try:
            result = crew.kickoff()

            if hasattr(result, 'raw'):
                response = str(result.raw).strip()
            else:
                response = str(result).strip()
            if not response:
                return (
                    'Desculpe, não consegui processar sua pergunta. '
                    'Pode tentar reformulá-la?'
                )

            return response

        except Exception as e:
            if 'quota exceeded' in str(e).lower():
                local_llm = get_llm(use_local_fallback=True)
                result = local_llm(query)[0]['generated_text']
                return str(result).strip()
            else:
                raise

        return result
