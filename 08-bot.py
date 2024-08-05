import requests
import time
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

SLEEP_SECONDS = 3
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
# MODEL_NAME = 'INGRESA EL NOMBRE DE TU MODELO CON FINE-TUNING'
MODEL_NAME=''

client = OpenAI(api_key=os.getenv('OPENAI_KEY'))


def get_updates(offset):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates"
    params = {"timeout": 250, "offset": offset}
    response = requests.get(url, params=params)
    return response.json()["result"]


def send_messages(chat_id, text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    params = {"chat_id": chat_id, "text": text}
    response = requests.post(url, params=params)
    return response


def get_openai_response(prompt):
    system = '''
        Eres un asistente de atención a clientes 
        y estudiantes de la plataforma de educación online en tecnología,  
        inglés y liderazgo llamada Platzi
        '''
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": f'{system}'},
            {"role": "user", "content": f'{prompt}'}],
        max_tokens=150,
        n=1,
        temperature=0.2)
    return response.choices[0].message.content.strip()


def main():
    print("Starting bot...")
    offset = 0
    while True:
        updates = get_updates(offset)
        if updates:
            for update in updates:
                offset = update["update_id"] + 1
                chat_id = update["message"]["chat"]['id']
                user_message = update["message"]["text"]
                print(f"Received message: {user_message}")
                gpt_response = get_openai_response(user_message)
                send_messages(chat_id, gpt_response)
        else:
            time.sleep(SLEEP_SECONDS)


if __name__ == '__main__':
    main()
