# Main agent logic: takes a question, generates a Cypher query, runs it against the graph database, and returns the result.
from agent.graph_client import GraphClient
from agent.cypher_generator import generate_cypher
from agent.cypher_validator import validate_cypher, extract_cypher

client = GraphClient()

def answer(question):
    try:
        raw_query = generate_cypher(question)
        cypher_query = extract_cypher(raw_query)

        print("\nGenerated Cypher:\n")
        print(cypher_query)

        validate_cypher(cypher_query)
        result = client.run_query(cypher_query)
        return result

    except Exception as e:
        print("\nAgent Error:", str(e))
        return "The agent could not answer the question."

if __name__ == "__main__":
    question = input("Ask a question: ")
    response = answer(question)
    print("\nResult:\n")
    print(response)
    
    
# Previous code using hardcoded queries and tools (commented out for now, as we are now generating queries dynamically with the LLM)
# from agent.graph_client import GraphClient
# from agent.tools import TOOLS


# client = GraphClient()


# def answer(question):
#     question = question.lower()

#     for keyword, query in TOOLS.items():
#         if keyword in question:
#             return client.run_query(query)

#     return "I don't know how to answer that yet."


# if __name__ == "__main__":
#     question = input("Ask a question: ")
#     response = answer(question)
#     print(response)

