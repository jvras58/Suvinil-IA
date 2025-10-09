"""DB Query Tool for CrewAI agents."""

import re

from crewai.tools import tool
from langchain_community.utilities import SQLDatabase
from sqlalchemy import create_engine, inspect

from apps.packpage.settings import get_settings


@tool('db_query')
def db_query_tool(query: str) -> str:
    """
    Use esta ferramenta para consultar o banco de dados SQL.
    Fornece resultados de queries SQL seguras com validação inteligente.

    IMPORTANTE: Use primeiro a ferramenta 'db_schema_inspector' ou
    'db_paint_query_helper' para descobrir a estrutura correta das tabelas.

    Args:
        query (str): A query SQL para executar no banco de dados.

    Returns:
        str: Resultados da query em formato texto com sugestões em caso de erro.
    """
    settings = get_settings()
    engine = create_engine(settings.DB_URL)
    db = SQLDatabase(engine=engine)
    inspector = inspect(engine)

    try:
        validation_result = _validate_query(query, inspector)
        if validation_result:
            return validation_result

        result = db.run_no_throw(query)
        if result:
            return str(result)
        else:
            return 'Nenhum resultado encontrado.'

    except Exception as e:
        error_msg = str(e)

        suggestions = _get_error_suggestions(error_msg, query, inspector)

        return f'Erro ao executar query: {error_msg}\n\n{suggestions}'
    finally:
        engine.dispose()


def _validate_query(query: str, inspector) -> str:
    """Valida a query antes da execução e fornece sugestões."""
    # Mapeamento de aliases comuns para nomes reais de tabelas
    table_aliases = {
        "tintas": "paint",
        "tinta": "paint",
        "tintas_suvinil": "paint",
        "suvinil": "paint",
        "paints": "paint",
        "usuarios": "user",
        "usuario": "user",
        "users": "user",
        "roles": "role",
        "funcoes": "role",
        "autorizacoes": "authorization",
        "autorizacao": "authorization",
        "transacoes": "transaction",
        "transacao": "transaction",
        "conversas": "ia_conversations",
        "conversa": "ia_conversations",
        "mensagens": "ia_messages",
        "mensagem": "ia_messages",
        "documentos": "ia_documents",
        "documento": "ia_documents",
        "atribuicoes": "assignment",
        "atribuicao": "assignment",
    }

    table_pattern = (
        r'\bFROM\s+(\w+)|\bJOIN\s+(\w+)|\bINTO\s+(\w+)|\bUPDATE\s+(\w+)'
    )
    matches = re.findall(table_pattern, query, re.IGNORECASE)

    referenced_tables = [
        table for match in matches for table in match if table
    ]

    if not referenced_tables:
        return None

    existing_tables = inspector.get_table_names()

    for table in referenced_tables:
        # Aplicar mapeamento de alias se existir
        corrected_table = table_aliases.get(table.lower(), table)
        if corrected_table != table:
            # Substituir na query e sugerir a correção
            query_corrected = re.sub(
                r"\b" + re.escape(table) + r"\b",
                corrected_table,
                query,
                flags=re.IGNORECASE,
            )
            return (
                f'Tabela "{table}" não encontrada. '
                f'Use "{corrected_table}" em vez de "{table}". '
                f"Query sugerida: {query_corrected}"
            )

        if table not in existing_tables:
            suggestions = _suggest_similar_tables(table, existing_tables)
            return f'Tabela "{table}" não encontrada. {suggestions}'

    return None


def _suggest_similar_tables(table_name: str, existing_tables: list) -> str:
    """Sugere tabelas similares baseadas no nome."""
    suggestions = []
    table_lower = table_name.lower()

    for existing in existing_tables:
        if (
            table_lower in existing.lower()
            or existing.lower() in table_lower
            or _similar_strings(table_lower, existing.lower())
        ):
            suggestions.append(existing)

    if suggestions:
        return f"Tabelas similares disponíveis: {', '.join(suggestions)}"
    else:
        return f"Tabelas disponíveis: {', '.join(existing_tables)}"


def _similar_strings(s1: str, s2: str, threshold: float = 0.6) -> bool:
    """Verifica se duas strings são similares usando distância de Levenshtein
    simples."""
    if len(s1) == 0 or len(s2) == 0:
        return False

    common_chars = sum(1 for a, b in zip(s1, s2, strict=False) if a == b)
    max_len = max(len(s1), len(s2))

    return (common_chars / max_len) >= threshold


def _get_error_suggestions(error_msg: str, query: str, inspector) -> str:
    """Fornece sugestões específicas baseadas no tipo de erro."""
    suggestions = []

    if 'no such table' in error_msg.lower():
        table_match = re.search(
            r'no such table: (\w+)', error_msg, re.IGNORECASE
        )
        if table_match:
            table_name = table_match.group(1)
            existing_tables = inspector.get_table_names()
            similar_suggestion = _suggest_similar_tables(
                table_name, existing_tables
            )
            suggestions.append(f'SUGESTÃO: {similar_suggestion}')

    elif 'no such column' in error_msg.lower():
        suggestions.append(
            'SUGESTÃO: Use a ferramenta "db_schema_inspector" '
            'para ver as colunas disponíveis na tabela.'
        )

    elif 'syntax error' in error_msg.lower():
        suggestions.append(
            'SUGESTÃO: Verifique a sintaxe SQL. '
            'Use a ferramenta "db_paint_query_helper" '
            'para ver exemplos de queries válidas.'
        )

    if 'paint' in query.lower() or 'tinta' in query.lower():
        suggestions.append(
            'DICA: Para consultar tintas, use a tabela "paint". '
            'Execute "db_paint_query_helper" para ver exemplos '
            'de queries e valores válidos para os campos enum.'
        )

    if suggestions:
        return '\n'.join(suggestions)
    else:
        return (
            'SUGESTÃO: Use "db_schema_inspector" para descobrir '
            'a estrutura das tabelas disponíveis.'
        )
