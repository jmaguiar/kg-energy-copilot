# 1️⃣ Knowledge Graph Tech Lead Cheat Sheet (1 page)

This is the **mental model a tech lead uses** when discussing KG with clients or architects.

---

# Knowledge Graph Tech Lead Cheat Sheet

## 1. What is a Knowledge Graph?

A **Knowledge Graph (KG)** represents entities and their relationships in a graph structure.

Basic idea:

```
Entity — Relationship — Entity
```

Example:

```
SolarPlant1 — SUPPLIES — SubstationA
SubstationA — DISTRIBUTES — Factory1
```

Key idea:

> **Graph = entities + relationships + properties**

---

# 2. Two main graph models

## Labeled Property Graph (LPG)

Used by:

```
Neo4j
ArangoDB
JanusGraph
```

Structure:

```
Nodes
Relationships
Properties
Labels
```

Example:

```
(:PowerStation {type:"solar"})
```

Relationship:

```
(:PowerStation)-[:SUPPLIES]->(:Substation)
```

Query language:

```
Cypher
```

---

## Semantic Knowledge Graph (RDF)

Used by:

```
GraphDB
Stardog
Jena
```

Structure:

```
Subject — Predicate — Object
```

Example:

```
SolarPlant1 generates SolarEnergy
```

Query language:

```
SPARQL
```

---

# 3. When to use a Knowledge Graph

Knowledge graphs are useful when:

```
relationships are complex
data comes from many systems
exploration queries are needed
```

Typical use cases:

```
data integration
recommendation systems
knowledge management
AI copilots
network analysis
```

---

# 4. Core components of a KG system

A production KG architecture contains:

```
Data sources
ETL / ingestion
Graph database
Query layer
Applications / AI
```

Architecture example:

```
Data sources
     ↓
Data pipelines
     ↓
Graph database
     ↓
API / queries
     ↓
Applications / AI agent
```

---

# 5. Graph modeling approach

Tech leads follow this process:

```
1 Identify entities
2 Identify relationships
3 Define properties
4 Define queries
```

Example:

Entities:

```
PowerStation
Substation
Consumer
```

Relationships:

```
SUPPLIES
DISTRIBUTES
```

Properties:

```
capacity
type
location
```

---

# 6. Query examples

Cypher example:

```
MATCH (p:PowerStation)-[:SUPPLIES]->(:Substation)-[:DISTRIBUTES]->(c:Consumer)
RETURN p.name, c.name
```

Question answered:

```
Which power stations supply consumers?
```

---

# 7. Enterprise KG architecture

Production architecture often includes:

```
Graph DB
Search index
Vector DB
AI agents
Data pipelines
```

Example:

```
User
 ↓
AI Agent
 ↓
Graph Query
 ↓
Knowledge Graph
 ↓
Answer
```

---

# 8. Common KG tools

Graph databases:

```
Neo4j
ArangoDB
GraphDB
TigerGraph
```

Frameworks:

```
LangChain
LlamaIndex
```

Visualization:

```
Neo4j Bloom
Linkurious
Graphistry
```

---

# 9. Tech lead mindset

Always structure a KG project as:

```
Problem
→ Data model
→ Architecture
→ Prototype
→ Roadmap
```
