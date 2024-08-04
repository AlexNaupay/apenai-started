import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_KEY"))

response = client.completions.create(
    model="gpt-3.5-turbo-instruct",
    prompt="Decide si el sentimiento de un Tweet es positivo, neutral, o negativo. \
  \n\nTweet: \"I have discussed with Donald Trump the idea of a government efficiency commission and I would be willing to be part of that commission.\
  \"\nSentiment:",
    temperature=0,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

print(response.choices[0].text)
