# https://core.telegram.org/bots/api#message

class message:
    message_id = None
    from_ = None
    date = None
    chat = None

    #Optional:
    text = None

    def __init__(self, json_message):
        if json_message != None:
            self.message_id = json_message[u"result"][0][u"update_id"]
            self.from_ = json_message[u"result"][0][u"from"]
            self.date = json_message[u"result"][0][u"date"]
            self.chat = json_message[u"result"][0][u"chat"]
            self.text = json_message[u"result"][0][u"message"][u"text"]
