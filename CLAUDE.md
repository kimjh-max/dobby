# CLAUDE.md

This file provides guidance to Claude Code when working in this repository.

## Project Overview

Dobby is an AI-powered Docs Agent that provides document search, Q&A (RAG), and document generation capabilities. Built with Python and FastAPI.

## Tech Stack

- **Language:** Python 3.10+
- **API Framework:** FastAPI + Uvicorn
- **LLM:** Anthropic Claude (via `anthropic` SDK)
- **Vector Store:** ChromaDB
- **Document Processing:** LangChain text splitters
- **Config:** Pydantic Settings + `.env`
- **Linter/Formatter:** Ruff
- **Type Checker:** mypy (strict mode)
- **Testing:** pytest + pytest-asyncio

## Build & Run

```bash
# Setup
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env  # then fill in API keys

# Run API server
uvicorn src.api.app:app --reload

# Ingest documents
python scripts/ingest.py
```

## Testing

```bash
pytest                    # run all tests
pytest tests/unit         # unit tests only
pytest --cov=src          # with coverage
```

## Code Style & Conventions

- Ruff for linting and formatting (line-length=88)
- mypy strict mode for type checking
- Async-first: use `async def` for I/O-bound operations
- Pydantic models for all data structures
- All modules must have `__init__.py`
- Docstrings on all public classes and functions

## Architecture

```
Dobby/
├── src/
│   ├── agent/              # Agent logic (orchestration)
│   │   ├── base.py         #   Abstract base agent
│   │   └── docs_agent.py   #   Main docs agent implementation
│   ├── core/               # Core config and shared logic
│   │   └── config.py       #   Pydantic Settings (reads .env)
│   ├── api/                # FastAPI endpoints
│   │   ├── app.py          #   App factory
│   │   └── router.py       #   Route definitions
│   ├── models/             # Pydantic data models
│   │   └── document.py     #   Document schema
│   ├── services/           # External service integrations
│   │   ├── llm/            #   LLM provider wrappers
│   │   ├── embedding/      #   Embedding model wrappers
│   │   ├── vectorstore/    #   Vector DB operations
│   │   └── document_loader/ #  File/URL loading & parsing
│   ├── prompts/            # Prompt templates
│   │   └── templates.py    #   System/QA prompts
│   └── utils/              # Utilities
│       └── logger.py       #   Logging setup
├── config/                 # YAML configuration files
├── data/
│   ├── raw/                # Original source documents
│   ├── processed/          # Chunked/cleaned documents
│   └── vectordb/           # ChromaDB persistence (gitignored)
├── tests/
│   ├── unit/               # Unit tests
│   ├── integration/        # Integration tests
│   └── fixtures/           # Test data
├── scripts/                # CLI scripts (ingestion, etc.)
├── docs/                   # Project documentation
├── pyproject.toml          # Dependencies & tool config
├── .env.example            # Environment variable template
└── .gitignore
```

### Data Flow

1. **Ingest:** `scripts/ingest.py` -> `document_loader` -> `embedding` -> `vectorstore`
2. **Query:** API request -> `docs_agent` -> `vectorstore` (retrieval) -> `llm` (generation) -> response

## Important Notes

- `.env` 파일은 절대 커밋하지 않음 (gitignored)
- `data/vectordb/`는 로컬 전용, git에 포함하지 않음
- 새로운 service를 추가할 때는 `src/services/` 하위에 별도 패키지로 생성
- 모든 외부 API 호출은 `services/` 레이어를 통해서만 수행
