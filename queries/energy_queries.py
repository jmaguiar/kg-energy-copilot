FACTORIES_POWERED = """
MATCH (p:PowerStation)-[:SUPPLIES]->(:Substation)-[:DISTRIBUTES]->(c:Consumer)
WHERE c.type = "industrial"
RETURN p.name, c.name
"""

ALL_CONSUMERS = """
MATCH (c:Consumer)
RETURN c.name
"""