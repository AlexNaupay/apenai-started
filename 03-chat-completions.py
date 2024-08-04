import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_KEY"))

response = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
        {"role": "system", "content": "Eres un asistente que da informacion sobre deportes."},
        {"role": "user", "content": "¿Quién ganó el mundial de fútbol?"},
        {"role": "assistant", "content": "El mundial de 2022 lo ganó Argentina"},
        {"role": "user", "content": "¿Dónde se jugó?"}
    ],
    #temperature=1
)

print(response.choices[0].message.content)
