# KG Energy Copilot

Minimal **Knowledge Graph + Python Agent** demo using **Neo4j**.

This project demonstrates how an AI-style agent can query a knowledge graph representing a simplified **energy distribution network**.

The goal of the project is to explore:

* Knowledge Graph modeling
* Cypher queries
* Python integration with Neo4j
* Agent-style architectures for data exploration

---

# Architecture

User question
↓
Python Agent
↓
Cypher query
↓
Neo4j Knowledge Graph
↓
Results

---

# Graph Model

The graph represents a simplified **energy grid**.

## Nodes

* PowerStation
* Substation
* Consumer

## Relationships

PowerStation → SUPPLIES → Substation
Substation → DISTRIBUTES → Consumer

Example:

SolarPlant1 → SubstationA → Factory1
WindFarm1 → SubstationB → Home1

---

# Project Structure

```
kg-energy-copilot
│
├── agent
│   ├── agent.py
│   ├── graph_client.py
│   └── tools.py
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

# Installation

Clone the repository:

```
git clone https://github.com/YOUR_USERNAME/kg-energy-copilot.git
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

Start Neo4j and load the dataset (`data/seed.cypher`).

Then run:

```
python -m agent.agent
```

Example interaction:

```
Ask a question:
Which factories are powered?
```

Example output:

```
SolarPlant1 → Factory1
HydroPlant1 → Factory2
```

---

# Tech Stack

* Neo4j
* Cypher
* Python
* Knowledge Graphs
* Agent-based architecture

---

# Future Improvements

Possible extensions of this project:

* LLM → Cypher query generation
* Larger graph datasets
* Graph visualization
* Web interface for querying the graph

---

# Purpose

This project is a **minimal Knowledge Graph prototype** designed to explore how graph databases and AI-style agents can be combined to query structured relational data.
