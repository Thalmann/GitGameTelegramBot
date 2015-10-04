# https://core.telegram.org/bots/api#user

class user:
    id_ = None
    first_name = None
    last_name = None
    username = None

    def __init__(self, json_user):
        if json_user != []:
            self.id_ = json_user[u"id"]
            self.first_name = json_user[u"first_name"]
            self.last_name = json_user[u"last_name"]
            self.username = json_user[u"username"]
