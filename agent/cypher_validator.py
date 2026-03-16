FORBIDDEN_KEYWORDS = [
    "DELETE",
    "DETACH",
    "DROP",
    "CREATE",
    "MERGE",
    "SET"
]


def extract_cypher(query: str):
    """
    Extract only the Cypher query from LLM output.
    """

    lines = query.split("\n")

    cypher_lines = []

    for line in lines:

        line = line.strip()

        if line.startswith("MATCH") or cypher_lines:
            cypher_lines.append(line)

        if line.startswith("RETURN"):
            break

    return "\n".join(cypher_lines)


def validate_cypher(query: str):

    upper_query = query.upper()

    for keyword in FORBIDDEN_KEYWORDS:
        if keyword in upper_query:
            raise ValueError(f"Forbidden Cypher keyword detected: {keyword}")

    if not upper_query.startswith("MATCH"):
        raise ValueError("Query must start with MATCH")

    if "RETURN" not in upper_query:
        raise ValueError("Query must contain RETURN")

    return True