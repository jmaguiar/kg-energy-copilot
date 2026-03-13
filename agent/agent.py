import os
from neo4j import GraphDatabase
from dotenv import load_dotenv

load_dotenv()

URI = os.getenv("NEO4J_URI")
USER = os.getenv("NEO4J_USER")
PASSWORD = os.getenv("NEO4J_PASSWORD")

driver = GraphDatabase.driver(URI, auth=(USER, PASSWORD))


def run_query(query):

    with driver.session() as session:
        result = session.run(query)
        return [record.data() for record in result]


query = """
MATCH (p:PowerStation)-[:SUPPLIES]->(:Substation)-[:DISTRIBUTES]->(c:Consumer)
RETURN p.name, c.name
"""

results = run_query(query)

print(results)