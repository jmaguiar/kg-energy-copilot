# kg-energy-copilot

A minimal **Knowledge Graph + AI Agent architecture** built with **Neo4j, Python, and a local LLM**.

This project demonstrates how an AI-style agent can query a **Knowledge Graph representing an energy distribution network** by translating natural language questions into Cypher queries.

The repository is designed as a **technical portfolio project** showcasing:

- Knowledge Graph modeling
- Cypher query design
- Python + Neo4j integration
- Agent-style architectures
- LLM-driven query generation

---

## Quick Overview


Architecture

The system implements a **Graph AI Copilot architecture**.

```
User
↓
AI Agent
↓
Local LLM (Ollama)
↓
Cypher Generation
↓
Cypher Extraction + Validation
↓
GraphClient
↓
Neo4j Knowledge Graph
↓
Results
```

The agent converts **natural language questions into Cypher queries** executed on the graph.

Stack

```
Neo4j
Cypher
Python
Ollama (local LLM)
```

Purpose

```
Demonstrate a Graph + AI architecture for knowledge exploration.
```

---

# Graph Model

The graph represents a simplified **energy grid**.

## Nodes

```

PowerStation
Substation
Consumer

```

## Relationships

```

PowerStation → SUPPLIES → Substation
Substation → DISTRIBUTES → Consumer

```

Example topology:

```

SolarPlant1 → SubstationA → Factory1
WindFarm1 → SubstationB → Home1

```

---

# Project Structure

```

kg-energy-copilot
│
├── agent
│   ├── agent.py
│   ├── graph_client.py
│   ├── cypher_generator.py
│   ├── validator.py
│   └── prompts.py
│
├── queries
│   └── energy_queries.py
│
├── data
│   └── seed.cypher
│
├── docs
│   ├── architecture.md
│   └── problem.md
│
├── README.md
└── requirements.txt

```

---

# Project Phases

## Phase 1 — Knowledge Graph Prototype ✔

Implemented:

- Neo4j graph model
- Seed dataset
- Cypher queries
- Python Neo4j integration
- GraphClient abstraction
- Agent architecture

Architecture:

```

User
↓
Agent
↓
Tools / Query Layer
↓
GraphClient
↓
Neo4j

```

---

## Phase 2 — LLM Graph Agent ✔

The system now supports **natural language questions**.

Workflow:

```

User question
↓
Local LLM (Ollama)
↓
Generate Cypher query
↓
Cypher extraction
↓
Query validation
↓
Neo4j execution
↓
Results

```

Key features:

- Local LLM integration via **Ollama**
- Cypher generation module
- Graph schema prompt
- Cypher extraction layer
- Query validation guardrails
- Error handling (agent does not crash)

The current model used is **tinyllama**, which occasionally produces incorrect queries.

The goal of Phase 2 was to **validate the architecture**, not optimize model accuracy.

---

# Installation

Clone the repository:

```

git clone [https://github.com/YOUR_USERNAME/kg-energy-copilot.git](https://github.com/YOUR_USERNAME/kg-energy-copilot.git)
cd kg-energy-copilot

```

Create environment:

```

conda create -n kg-agent python=3.11
conda activate kg-agent

```

Install dependencies:

```

pip install -r requirements.txt

```

---

# Run the Agent

Start Neo4j and load the dataset:

```

data/seed.cypher

```

Then run:

```

python -m agent.agent

```

Example interaction:

```

Ask a question:
Which consumers are powered?

```

Example output:

```

SolarPlant1 → Factory1
HydroPlant1 → Factory2

```

---

# Tech Stack

Graph Database

```

Neo4j

```

Graph Query Language

```

Cypher

```

Language

```

Python

```

LLM

```

Local LLM via Ollama

```

Development

```

VSCode
WSL
Conda

```

---

# Roadmap

```

Phase 1 — Knowledge Graph prototype ✔
Phase 2 — LLM Graph Agent ✔
Phase 3 — Graph dataset scaling
Phase 4 — Graph analytics queries
Phase 5 — Graph visualization
Phase 6 — Production architecture

```

---

# Purpose

This project demonstrates how to build a **Graph + AI system architecture** combining:

- Knowledge Graphs
- Agent architectures
- LLM query generation
- Graph data exploration

It is designed as a **technical portfolio project for Tech Lead and Graph AI architecture roles**.

