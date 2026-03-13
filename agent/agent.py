from agent.graph_client import GraphClient
from agent.tools import TOOLS


client = GraphClient()


def answer(question):
    question = question.lower()

    for keyword, query in TOOLS.items():
        if keyword in question:
            return client.run_query(query)

    return "I don't know how to answer that yet."


if __name__ == "__main__":
    question = input("Ask a question: ")
    response = answer(question)
    print(response)
