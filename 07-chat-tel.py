import requests
import time
import os
from dotenv import load_dotenv
from openai import OpenAI

SLEEP_SECONDS = 3

load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_KEY'))
telegram_token = os.getenv('TELEGRAM_TOKEN')


# Get updates from telegram
def get_updates(token, offset=None):
    url = f"https://api.telegram.org/bot{token}/getUpdates"
    params = {"offset": offset} if offset else {}  # offset
    response = requests.get(url, params=params)
    return response.json()


def print_new_messages(token):
    offset = None
    while True:
        updates = get_updates(token, offset)
        if updates['ok'] is True and 'result' in updates:
            for update in updates["result"]:  # Each update
                message = update["message"]  # Message
                _id = message["from"]["id"]
                username = message['from']["first_name"]

                text = message.get("text")
                chat_id = message["chat"]["id"]

                print(f"User: {username}({_id})")
                print(f"Message: {text}")
                print(f"Chat Id: {chat_id}")
                print("-" * 20)

                offset = update["update_id"] + 1  # Set next update
        time.sleep(SLEEP_SECONDS)


# Main
print_new_messages(telegram_token)
