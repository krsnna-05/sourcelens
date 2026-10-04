# 🔍 Sourcelens 2.0

## Agentic Codebase Intelligence Platform

> An AI-powered system that understands GitHub repositories, analyzes software architecture, maps code relationships, and provides contextual explanations using RAG, LangGraph, and code intelligence.

Sourcelens transforms large software repositories into an intelligent knowledge layer.

Instead of searching through thousands of files manually, developers can ask questions like:

```
How does authentication work?

Where is payment processing implemented?

Explain the database architecture.

What is the request flow for this API?

Where is Redis used in this project?
```

Sourcelens analyzes the repository and provides answers with relevant files, symbols, and code context.

---

# ✨ Features

## 🧠 Repository Understanding

Sourcelens builds a semantic understanding of a repository.

Capabilities:

- Repository structure analysis
- Function and class extraction
- Component discovery
- API route detection
- Dependency mapping
- Architecture analysis
- Code relationship discovery

Supported languages:

- TypeScript
- JavaScript
- Python
- Java
- Go

---

# 🔎 Intelligent Code Search

Traditional search finds text.

Sourcelens understands code concepts.

Example:

User:

```
Where is authentication handled?
```

Instead of searching only:

```
auth
login
jwt
```

Sourcelens understands:

```
Login Route

        ↓

Authentication Controller

        ↓

Auth Service

        ↓

User Repository

        ↓

JWT Generation
```

and returns the complete flow.

---

# 🏗️ System Architecture

```
                         User

                          |

                          v

                    Next.js UI

                          |

                          v

                    FastAPI API

                          |

                          v

                  LangGraph Runtime

                          |

        +-----------------+-----------------+

        |                 |                 |

        v                 v                 v

 Architecture       Retrieval        Explanation
   Agent              Agent             Agent


        |

        v


             Repository Knowledge Layer


        PostgreSQL + pgvector

                 +

              Redis


        |

        v


          Repository Intelligence Engine


        |

        v


        Tree-sitter Parser
        Embeddings
        Code Graph
```

---

# 🤖 Agent Architecture

Sourcelens uses specialized agents for repository analysis.

```
                  User Question

                        |

                        v

                Query Understanding Agent

                        |

        +---------------+---------------+

        |               |               |

        v               v               v


 Architecture      Dependency      Documentation
 Agent              Agent            Agent


        |               |               |

        +---------------+---------------+

                        |

                        v

              Context Synthesis Agent

                        |

                        v

                    Final Answer
```

---

# Agent Responsibilities

## 🧭 Query Understanding Agent

Determines what the user is asking.

Example:

Question:

```
Explain payment flow
```

Creates tasks:

```
1. Find payment routes

2. Find payment services

3. Find external integrations

4. Find database models

5. Generate flow explanation
```

---

# 🏛️ Architecture Agent

Understands the overall system design.

Analyzes:

- Folder structure
- Entry points
- Services
- Modules
- Communication patterns

Example output:

```
Repository architecture:

Frontend:
Next.js application

Backend:
Node.js REST API

Database:
PostgreSQL

External services:
Stripe
Redis
AWS S3
```

---

# 🔗 Dependency Agent

Understands relationships between code entities.

Example:

Question:

```
Where is Redis used?
```

Output:

```
Redis usage found:

1. Session management

src/auth/session.ts


2. Background jobs

src/jobs/queue.ts


3. Cache layer

src/cache/redis.ts
```

---

# 📚 Documentation Agent

Converts complex code into human-readable explanations.

Example:

Question:

```
Explain this module
```

Output:

```
This module handles user authentication.

Responsibilities:

- Validate credentials
- Generate access tokens
- Manage sessions
- Communicate with user repository
```

---

# 🌳 Code Intelligence Pipeline

```
GitHub Repository

        |

        v

Clone Repository

        |

        v

Tree-sitter Parsing

        |

        v

Extract Code Symbols

        |

        v

Generate Embeddings

        |

        v

Store Vector Knowledge

        |

        v

Build Code Graph

        |

        v

Enable Agentic Search
```

---

# 🌳 Code Graph

Sourcelens builds relationships between code entities.

Example:

```
login.ts

    |
    | calls
    v

auth.service.ts

    |
    | uses
    v

user.repository.ts
```

Stored relationships:

```
source_symbol

      |

relationship

      |

target_symbol
```

Supported relationships:

- imports
- calls
- extends
- implements
- uses

---

# 🔍 Retrieval System

Sourcelens uses hybrid retrieval.

## Semantic Search

Understands meaning.

Example:

```
authentication
login
sessions
authorization
```

---

## Keyword Search

Finds exact symbols.

Example:

```
authMiddleware
generateToken
verifyJWT
```

---

## Graph Search

Understands software relationships.

Example:

```
API Endpoint

      ↓

Controller

      ↓

Service

      ↓

Database
```

---

# 🚀 Example Queries

## Repository Overview

Question:

```
What does this repository do?
```

Response:

```
This is an e-commerce platform.

Main modules:

- Authentication
- Product management
- Order processing
- Payment handling

Architecture:

Next.js frontend
Node.js backend
PostgreSQL database
```

---

## Architecture Explanation

Question:

```
Explain backend architecture
```

Response:

```
Request flow:

API Route

 ↓

Controller

 ↓

Business Service

 ↓

Database Layer

 ↓

External Provider
```

---

## Feature Discovery

Question:

```
How does user registration work?
```

Response:

```
Registration flow:

1. POST /register

File:
routes/user.ts


2. User validation

File:
services/user.service.ts


3. Database insertion

File:
repositories/user.repository.ts
```

---

# 🛠️ Tech Stack

## Frontend

- Next.js
- TypeScript
- Tailwind CSS
- shadcn/ui

---

## Backend

- FastAPI
- Python
- LangChain
- LangGraph
- Deep Agents

---

## AI Layer

- LLM APIs / Local LLMs
- Embedding models
- Structured outputs

---

## Database

- PostgreSQL
- pgvector
- Redis

---

## Code Analysis

- Tree-sitter

---

## Infrastructure

- Docker
- Docker Compose

---

# 📂 Project Structure

```
sourcelens/

├── apps/

│   ├── web/
│   │   └── Next.js frontend
│   │
│   └── api/
│       └── FastAPI backend


├── services/

│   ├── indexer/
│   │   └── Repository analysis engine
│   │
│   ├── agent/
│   │   └── LangGraph workflows
│   │
│   └── worker/
│       └── Background processing


├── packages/

│   ├── database/
│   ├── embeddings/
│   └── shared/


└── docker-compose.yml
```

---

# 🗺️ Roadmap

## Phase 1 — Repository Intelligence

- [ ] GitHub repository ingestion
- [ ] Tree-sitter parsing
- [ ] Symbol extraction
- [ ] Embedding generation
- [ ] Vector search

## Phase 2 — Code Understanding

- [ ] Code graph generation
- [ ] Dependency analysis
- [ ] Architecture extraction
- [ ] API flow detection

## Phase 3 — Agentic Intelligence

- [ ] Query planning agent
- [ ] Architecture agent
- [ ] Dependency agent
- [ ] Documentation agent
- [ ] Context synthesis

## Phase 4 — Advanced Features

- [ ] Repository comparison
- [ ] Architecture diagrams
- [ ] Developer onboarding mode
- [ ] Repository health analysis

---

# 🎯 Vision

Sourcelens aims to become an intelligent codebase understanding layer that helps developers:

- Understand unfamiliar repositories
- Navigate large codebases
- Learn system architecture
- Discover dependencies
- Generate technical documentation
- Accelerate developer onboarding

---

# 📜 License

MIT License
