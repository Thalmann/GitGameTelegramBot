import requests
import os
import json

token = open(os.path.join(".", "token.txt"), "r").read().rstrip()
url = "".join(["https://api.telegram.org/", "bot", token, "/"])
update_url = "".join([url, "getUpdates"])
send_message_url = "".join({url, "sendMessage"})


def get_message(offset=0):
    message = requests.post(update_url, {"offset": offset}).json()
    return Message(message)

def get_chat_id(message):
    return message[u"result"][0][u"message"][u"from"][u"id"]

def get_update_id(message, old_update_id):
    if message != None:
        return message[u"result"][0][u"update_id"]
    else:
        return old_update_id

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


class Chat:
    chat_id = None
    update_id = None
    

# https://core.telegram.org/bots/api#message

class Message:
    empty = False
    message_id = None
    from_ = None
    date = None
    chat = None
    update_id = None

    #Optional:
    text = None

    def __init__(self, json_message):
        if json_message[u"result"] != []:
            self.message_id = json_message[u"result"][0][u"message"][u"message_id"]
            self.from_ = User(json_message[u"result"][0][u"message"][u"from"])
            self.date = json_message[u"result"][0][u"message"][u"date"]
            self.chat = json_message[u"result"][0][u"message"][u"chat"]
            self.update_id = int(json_message[u"result"][0][u"update_id"])
            if "text" in json_message[u"result"][0][u"message"]:
                self.text = json_message[u"result"][0][u"message"][u"text"]
        else:
            self.empty = True

# https://core.telegram.org/bots/api#user

class User:
    id_ = None
    first_name = None
    last_name = None
    username = None

    def __init__(self, json_user):
        if json_user != []:
            self.id_ = json_user[u"id"]
            self.first_name = json_user[u"first_name"]
            if "last_name" in json_user:
                self.last_name = json_user[u"last_name"]
            if "username" in json_user:
                self.username = json_user[u"username"]

# https://core.telegram.org/bots/api#groupchat

class GroupChat:
    id_ = None
    name = None

    def __init__(self, json_group):
        self.id_ = json_group[u"id"]
        self.name = json_group[u"group_name"]
