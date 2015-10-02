import requests
import os
import json

token = open(os.path.join(".", "token.txt"), "r").read()
url = "https://api.telegram.org/" + "bot" + token + "/"
update_url = url.join( "getUpdates")
send_message_url = url + "sendMessage"
url2 = "https://api.telegram.org/bot131685579:AAHSPec4s1xZ5vdUu03eV4hpq2LaLPF4KG8/getUpdates"

def get_message():
    message = []
    try:
        message = requests.get(update_url.encode(encoding='UTF-8',errors='strict')).json()
    except ValueError:
        return None
    return message if message[u"result"] != [] else None

def get_text_message(message):
    if message != None:
        return message[u"result"][0][u"message"][u"text"]
    raise ValueError("Invalid message")

def get_chat_id(message):
    return message[u"result"][0][u"message"][u"from"][u"id"]

def get_update_id(message, old_update_id):
    if message != None:
        return message[u"result"][0][u"update_id"]
    else:
        return old_update_id

def get_updates_message(payload = {"offset": 0}):
    message = []
    try:
        message = requests.get(update_url.encode(encoding='UTF-8',errors='strict'), payload).json()
    except ValueError:
        return None

def load_update_id():
    return int(open(os.path.join(".", "update_id.txt"), "r").read())

def save_update_id(update_id):
    open(os.path.join(".", "update_id.txt"), "w").write(str(update_id))

def send_text_message(chat_id, text):
    payload = {"chat_id": chat_id, "text": text}
    return requests.post(send_message_url, payload)

def send_text_message_with_keyboard(chat_id, text, buttons):
    keyboard = '{"keyboard":' + json.dumps(buttons) + ',"one_time_keyboard": true}'
    payload = {"chat_id": chat_id, "text": text, "reply_markup": keyboard}
    return requests.post(send_message_url, payload)
