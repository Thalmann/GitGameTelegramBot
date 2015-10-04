# https://core.telegram.org/bots/api#groupchat

class group_chat:
    id_ = None
    name = None

    def __init__(self, json_group):
        self.id_ = json_group[u"id"]
        self.name = json_group[u"group_name"]
