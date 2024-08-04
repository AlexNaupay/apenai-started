import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_KEY"))

response = client.completions.create(
    model="gpt-3.5-turbo-instruct",
    prompt="¿Quién descubrió américa?",
    # temperature=0,
    max_tokens=100,
    top_p=1,
)

print(response.choices[0].text)
