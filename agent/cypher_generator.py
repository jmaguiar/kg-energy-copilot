import requests
import re
from agent.prompts import SYSTEM_PROMPT

OLLAMA_URL = "http://172.21.16.1:11434/api/generate"
MODEL = "tinyllama"


def extract_cypher(text):
    match = re.search(r"(MATCH .*?RETURN .*?)(;|$)", text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return text.strip()


def generate_cypher(question):

    prompt = SYSTEM_PROMPT + "\n\nQuestion:\n" + question

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    raw_output = response.json()["response"]

    cypher_query = extract_cypher(raw_output)

    return cypher_query

# With OpenAI API (commented out for now, as we are using Ollama instead)
# import os
# from openai import OpenAI
# from dotenv import load_dotenv
# from agent.prompts import SYSTEM_PROMPT

# load_dotenv()

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# def generate_cypher(question):

#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[
#             {"role": "system", "content": SYSTEM_PROMPT},
#             {"role": "user", "content": question},
#         ],
#         temperature=0,
#     )

#     cypher_query = response.choices[0].message.content.strip()

#     return cypher_query
