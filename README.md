# 🔍 Sourcelens 2.0

## Agentic Codebase Intelligence Platform

> An AI engineering assistant that understands repositories, answers architectural questions, analyzes code relationships, detects issues, and assists developers using RAG, LangGraph, and autonomous agents.

Sourcelens converts a software repository into an intelligent knowledge system by combining:

- Code understanding
- Retrieval Augmented Generation (RAG)
- Agentic workflows
- Code graphs
- Developer automation

Inspired by:

- Claude Code
- Sourcegraph
- Cursor Codebase Chat

---

# ✨ Features

## 🧠 Repository Understanding

Sourcelens analyzes repositories structurally instead of treating code as plain text.

Supported languages:

- TypeScript
- JavaScript
- Python
- Java
- Go

Capabilities:

- Function extraction
- Class extraction
- Component discovery
- API route detection
- Dependency analysis
- Code relationship mapping

---

# 🏗️ Architecture

```
User
 |
 v
Next.js Interface
 |
 v
FastAPI Backend
 |
 v
LangGraph Agent Runtime
 |
 +-----------------------------+
 |             |               |
 v             v               v

Retrieval     Code          Execution
Agent         Agent         Agent


 |
 v

Knowledge Layer

PostgreSQL + pgvector
Redis

 |
 v

Repository Intelligence Engine

Tree-sitter
Chunking
Embeddings
Code Graph
```

---

# 🤖 Agent System

Sourcelens uses LangGraph to orchestrate specialized agents.

```
                 User Question

                       |
                       v

                Planner Agent

                       |

        +--------------+--------------+

        v              v              v

 Knowledge       Code Analyst    Executor
 Agent            Agent          Agent


        +--------------+--------------+

                       |

                       v

              Response Generator
```

---

# Agent Responsibilities

## Planner Agent

Breaks complex questions into tasks.

Example:

```
Question:

Why is authentication failing?


Plan:

1. Find authentication routes
2. Inspect middleware
3. Analyze database models
4. Check token handling
```

---

## Knowledge Agent

Responsible for retrieving relevant repository context.

Tools:

- Semantic search
- Keyword search
- Symbol lookup
- Dependency lookup

---

## Code Analyst Agent

Understands relationships:

```
API Route
   |
   v
Service Layer
   |
   v
Database Model
   |
   v
External APIs
```

---

## Execution Agent

Provides controlled developer automation.

Initial permissions:

✅ Read files  
✅ Run tests  
✅ Generate git diff  

Future:

- Modify files
- Generate patches
- Create commits

with human approval.

---

# 🧬 Repository Intelligence Pipeline

```
Repository URL

      |
      v

Clone Repository

      |
      v

Tree-sitter Parsing

      |
      v

Extract Symbols

      |
      v

Generate Embeddings

      |
      v

Store in PostgreSQL + pgvector

      |
      v

Build Code Graph
```

---

# 🌳 Code Graph

Sourcelens stores relationships between code entities.

Example:

```
login.ts

   |
 calls
   |

auth.service.ts

   |
 uses
   |

user.model.ts
```

Relationships:

- imports
- calls
- extends
- implements
- uses

---

# 🔎 Retrieval System

Sourcelens uses hybrid code retrieval.

## Semantic Search

Understands concepts:

```
authentication
login
session
JWT
```

## Keyword Search

Finds exact symbols:

```
authMiddleware
generateToken
verifyJWT
```

## Graph Search

Understands architecture:

```
Controller
 |
Service
 |
Database
```

---

# 🚀 Example Usage

## Repository Analysis

Input:

```
Analyze this repository
```

Output:

```
Frontend:
Next.js

Backend:
Node.js API

Database:
PostgreSQL


Main modules:

- Authentication
- Payments
- Users
- Notifications
```

---

## Code Explanation

Question:

```
Explain authentication flow
```

Response:

```
Authentication starts at:

src/routes/login.ts

then moves through:

src/services/auth.service.ts

and generates JWT tokens using:

src/utils/jwt.ts
```

---

## Bug Investigation

Question:

```
Why is login failing?
```

Agent workflow:

```
Plan

↓

Search authentication code

↓

Analyze middleware

↓

Inspect token generation

↓

Identify issue

↓

Suggest fix
```

---

# 🛠️ Tech Stack

## Frontend

- Next.js
- TypeScript
- Tailwind CSS
- shadcn/ui

## Backend

- FastAPI
- Python
- LangChain
- LangGraph
- Deep Agents

## AI Infrastructure

- Ollama
- Local LLMs
- Embeddings
- Structured Outputs

## Database

- PostgreSQL
- pgvector
- Redis

## Code Intelligence

- Tree-sitter

## Infrastructure

- Docker
- Docker Compose

---

# 📂 Project Structure

```
sourcelens/

├── apps/
│
│   ├── web/
│   │   └── Next.js frontend
│   │
│   └── api/
│       └── FastAPI backend
│
├── services/
│
│   ├── indexer/
│   │   └── Repository parsing
│   │
│   ├── agent/
│   │   └── LangGraph workflows
│   │
│   └── worker/
│       └── Background jobs
│
├── packages/
│
│   ├── database/
│   ├── embeddings/
│   └── shared/
│
└── docker-compose.yml
```

---

# 🗺️ Roadmap

## Phase 1 — Code RAG

- Repository ingestion
- Tree-sitter parsing
- Symbol extraction
- Embeddings
- Semantic search


## Phase 2 — Code Intelligence

- Code graph
- Dependency analysis
- Architecture visualization


## Phase 3 — Agent System

- Planner agent
- Retrieval agent
- Code analyst agent
- LangGraph workflows


## Phase 4 — Autonomous Development

- Deep Agents
- Code modification
- Test execution
- Patch generation


## Phase 5 — Production

- Authentication
- Background workers
- Streaming responses
- Deployment

---

# 🎯 Vision

Sourcelens aims to become an autonomous engineering assistant capable of:

- Understanding unfamiliar repositories
- Explaining system architecture
- Finding bugs
- Generating documentation
- Creating tests
- Assisting developers throughout the software lifecycle

---

# License

MIT License

DO NOT FUCKING BUILD THE APP, JUST CREATE THE REPO WITH ABOVE README CONTENT