# Suvinil-IA Copilot Instructions

## Project Architecture

This is a **FastAPI + SQLAlchemy + CrewAI** intelligent paint recommendation system. The architecture is modular with clear separation between core business logic (`apps/core/`) and AI functionality (`apps/ia/`).

### Key Components
- **Core API**: RBAC-enabled REST API with JWT authentication and comprehensive audit trails
- **AI Module**: CrewAI agents for paint recommendation using RAG with Suvinil product knowledge
- **Database**: SQLAlchemy ORM with Alembic migrations, supports SQLite (dev) and PostgreSQL (prod)

## Critical Patterns & Conventions

### Model Structure
All models inherit from `AbstractBaseModel` (in `apps/packpage/base_model.py`) which provides automatic audit fields:
```python
# Every model gets these audit fields automatically
audit_user_ip: Mapped[str]
audit_created_at: Mapped[datetime] 
audit_updated_on: Mapped[datetime]
audit_user_login: Mapped[str]
```

Models must be imported in `apps/core/models/__init__.py` to resolve SQLAlchemy relationships.

### API Pattern
**Router → Controller → Model** structure:
- **Routers** (`apps/core/api/*/router.py`): FastAPI route definitions with dependency injection
- **Controllers** (`apps/core/api/*/controller.py`): Business logic layer
- **Schemas** (`apps/core/api/*/schemas.py`): Pydantic models for request/response validation

Standard dependencies:
```python
DbSession = Annotated[Session, Depends(get_session)]
CurrentUser = Annotated[User, Depends(get_current_user)]
```

### Authorization System
- **RBAC**: User → Assignment → Role → Authorization → Transaction
- **Middleware**: `AuthorizationMiddleware` adds request timing headers
- **Validation**: Use `validate_transaction_access()` for operation permissions
- **Operation Codes**: Defined in `EnumOperationCode` for granular permissions

### Database Naming Convention
- Table names: lowercase (e.g., `user`, `paint`)
- Column names: prefixed by type (`str_username`, `int_id`, `audit_*`)
- Indexes: `idx_{table}_{column}` format

## Development Workflows

### Environment Setup
```bash
# Use UV package manager (not pip)
uv sync                    # Install dependencies
uv run taskipy run        # Start development server

# Database operations
uv run taskipy migrate     # Run Alembic migrations
uv run taskipy setup_db    # Full DB setup with seeds
```

### Testing
```bash
uv run taskipy test       # Run pytest with coverage
uv run taskipy lint       # Ruff + Blue linting
uv run taskipy format     # Format code
```

Test structure uses factories (`tests/factory/`) and follows the pattern:
- Unit tests: `test_{module}.py`
- Fixtures: Comprehensive setup in `conftest.py` with in-memory SQLite

### Docker Development
```bash
# Local development with PostgreSQL
docker-compose up postgres    # Just database
docker-compose up            # Full stack
```

## AI Integration Points

### CrewAI Configuration
- AI agents are in development (`apps/ia/` - currently minimal)
- Groq API integration for LLM inference (Llama 3.1 8B)
- RAG system for paint product knowledge
- Environment variable: `GROQ_API_KEY` required

### Paint Domain Model
Critical paint attributes in `apps/core/api/paint/paint_enums.py`:
- `PaintLine`: Product categories (STANDARD, PREMIUM, SUPER_PREMIUM)
- `Environment`: Application contexts (INTERNAL, EXTERNAL, BATHROOM, KITCHEN)
- `SurfaceType`: Application surfaces
- `FinishType`: Paint finish options

## Common Pitfalls

1. **Missing Model Import**: Always add new models to `apps/core/models/__init__.py`
2. **Audit Fields**: Never manually set audit fields - they're handled automatically
3. **Path Structure**: Use `apps.core.api` (not `app.core.api`) in imports
4. **Dependencies**: Use UV, not pip - pyproject.toml defines all dependencies
5. **Authorization**: Every protected endpoint needs `validate_transaction_access()`

## File Structure Navigation

- `apps/core/startup.py`: FastAPI app configuration and router registration
- `apps/packpage/`: Shared utilities (base models, exceptions, settings)
- `migrations/versions/`: Alembic migration files
- `seeds/`: Database initialization scripts
- `DOCS/`: Architecture documentation and deployment guides

## Environment Variables

Required for full functionality:
- `GROQ_API_KEY`: For AI agent functionality
- `DB_URL`: Database connection (defaults to SQLite)
- `SECURITY_*`: JWT configuration for authentication
