import os
from dotenv import load_dotenv
from openai import OpenAI
import random

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_KEY"))


def get_clue():
    words = ['elefante', 'león', 'jirafa', 'hipopótamo', 'mono']
    random_word = random.choice(words)
    prompt = 'Adivina la palabra que estoy pensando. Es un animal que vive en la selva.'
    return prompt, random_word


def check_answer(user_input, answer):
    if user_input == answer:
        return True
    return False


def give_property(animal):
    response = client.chat.completions.create(
        model='gpt-4',
        messages=[
            {"role": "user",
             "content": 'Dame una caracteristica del tipo animal ' + animal + ', pero jamás digas el nombre del animal'},
        ],
        max_tokens=100)
    return response.choices[0].message.content


def play_game():
    prompt, answer = get_clue()
    print(prompt)
    while True:
        user_input = input('Ingresa tu respuesta:')
        if check_answer(user_input, answer):
            print('Correcto! La respuesta era:', answer)
            break
        else:
            print('Respuesta incorrecta. Intentalo de nuevo')
            print(give_property(answer))


# Play game
play_game()
