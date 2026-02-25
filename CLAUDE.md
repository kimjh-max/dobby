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

---

## 🤖 Claude 업무 지침

### 새 채팅 시작 시
항상 아래 질문으로 시작할 것:
> "안녕하세요! 👋 오늘 진행할 **프로젝트명**이 무엇인가요?"

프로젝트명을 받으면:
1. `~/Desktop/dobby/projects/프로젝트명/` 폴더 생성 (없으면)
2. `~/Desktop/dobby/projects/프로젝트명/YYYY-MM-DD.md` 파일 생성
3. 아래 형식으로 업무 기록 시작

### 매일 저장되는 .md 파일 형식
```markdown
# 프로젝트명 - YYYY-MM-DD

## 📌 오늘 대화 요약

## ✅ 과업 목록
- [ ] [과업명]
  - 발신인:
  - 내용:
  - 마감일:

## 🔄 진행 상황
- 완료:
- 진행 중:
- 다음 스텝:
```

### 매일 아침
"오늘 메일 요약해줘" 요청 시 Gmail 확인 후 신규 과업을 체크리스트로 정리해서 해당 날짜 .md 파일에 저장

### GitHub 자동 커밋
- 매일 24:00에 `scripts/daily_commit.sh` 자동 실행
- 커밋 메시지 형식: `YYYY-MM-DD 업무 기록 자동 커밋`
