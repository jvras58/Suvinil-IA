# Copilot Instructions - Suvinil IA

## Project Overview
This is a FastAPI-based AI paint recommendation system for Suvinil, using CrewAI agents to analyze environment descriptions and recommend appropriate paints. The system features a complete RBAC (Role-Based Access Control) architecture with JWT authentication, audit trails, and CrewAI integration with Groq's Llama 3.1 model.

## Architecture & Key Patterns

### Core Structure
- **FastAPI App**: `app/startup.py` - Main application with middleware and router configuration
- **Generic Controller Pattern**: `app/utils/generic_controller.py` - Base CRUD operations for all entities
- **Base Model**: `app/utils/base_model.py` - All models inherit from `AbstractBaseModel` with audit fields
- **RBAC System**: Users → Assignments → Roles → Authorizations → Transactions (permissions)

### AI Integration
- **LLM Configuration**: `app/utils/llm.py` - Groq/Llama 3.1 setup with CrewAI
- **Text Processing**: `app/api/text_processing/controller.py` - CrewAI agents for environment analysis
- **Paint Recommendation**: Uses specialized agents to match user environment descriptions to paint products

### Data Models
All models extend `AbstractBaseModel` and include audit fields:
```python
audit_user_ip, audit_created_at, audit_updated_on, audit_user_login
```

Key models: `User`, `Role`, `Assignment`, `Authorization`, `Transaction`, `Paint`, `ProcessedText`

## Development Workflow

### Setup Commands
```bash
# Install dependencies
uv sync && uv install

# Database setup (applies migrations + seeds RBAC data)
task setup_db

# Run development server
task run

# Run tests with coverage
task test
```

### Environment Configuration
- **Settings**: `app/utils/settings.py` uses Pydantic settings with `.env` and `.secrets/` directory
- **Required**: `GROQ_API_KEY`, `SECURITY_API_SECRET_KEY` (in .secrets/), `DB_URL`
- **Dev Container**: Project configured for VS Code dev containers

### Testing Patterns
- **Factory Pattern**: `tests/factory/` - Use factories for test data creation
- **Fixtures**: `tests/conftest.py` - Comprehensive test setup with in-memory SQLite
- **Coverage**: Aim for comprehensive test coverage with `pytest-cov`

## Paint Domain Logic

### Paint Enums (`app/api/paint/paint_enums.py`)
- `SurfaceType`: wood, metal, masonry, concrete, etc.
- `Environment`: internal, external, both
- `FinishType`: matte, satin, semi_gloss, gloss, etc.
- `PaintLine`: premium, standard, economic, professional

### AI Processing Flow
1. User describes environment (surface, climate, preferences)
2. CrewAI agent analyzes description using specialized prompt
3. RAG system matches to Suvinil product database
4. Returns justified recommendations with technical explanations

## Code Conventions

### Router Structure
```python
# Standard pattern in all routers
@router.post('/', response_model=schemas.ResponseModel)
def create_item(payload: schemas.CreateModel, db_session: Session = Depends(get_session)):
    controller = Controller()
    return controller.create(db_session, payload)
```

### Controller Pattern
All controllers inherit from `GenericController[T]` providing:
- `get()`, `get_all()`, `save()`, `delete()` methods
- Built-in filtering and pagination
- Consistent error handling with custom exceptions

### Security & Middleware
- **JWT Authentication**: `app/utils/security.py`
- **Authorization Middleware**: `app/api/authorization/middleware.py` - Process time tracking
- **RBAC Validation**: Controllers validate permissions against `Transaction` entities

## Database & Migrations

### Alembic Usage
```bash
# Generate migration
alembic revision --autogenerate -m "description"

# Apply migrations
alembic upgrade head
```

### Model Relationships
- Import all models in `app/models/__init__.py` to resolve SQLAlchemy relationships
- Use `lazy='subquery'` for related data loading
- Foreign keys follow pattern: `{entity}_id` references `{table}.id`

## CrewAI Integration

### Agent Configuration
```python
agent = Agent(
    role='Especialista em Processamento de Texto',
    goal='Analisar e melhorar texto usando técnicas de IA',
    backstory='...',
    llm=get_llm(),  # Uses Groq/Llama 3.1
    verbose=False   # Set True for debugging
)
```

### Task Execution
Tasks are defined with `description`, `expected_output`, and assigned to crews for orchestrated execution.

## Docker & Deployment

### Development
- Dev container configuration in `.devcontainer/`
- SQLite for local development
- Hot reload with `--reload` flag

### Production
- PostgreSQL database (compose.yml)
- Multi-stage Docker build
- Health checks and restart policies
- Port 8000 exposed, PostgreSQL on 5433

## Common Patterns

### Error Handling
Custom exceptions in `app/utils/exceptions.py`:
- `ObjectNotFoundException`
- `IntegrityValidationException` 

### API Response Format
Consistent response schemas in `app/utils/base_schemas.py`

### IP Address Tracking
Use `app/utils/client_ip.py` for audit trail IP capture

Remember: Always run `task setup_db` after schema changes, and use the generic controller pattern for new entities to maintain consistency.
