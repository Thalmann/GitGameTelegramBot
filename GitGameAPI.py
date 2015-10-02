import requests

# API definition: https://github.com/SickTeam/GitGameServer/wiki/GitGame-definition
url = ""
url_game = "".join([url, "games"])
url_players = "".join([url, "games/"])

def get_game_id_url(game_id):
    return "".join([url, "games/", game_id])

def get_players_url(game_id):
    return "".join([get_game_id_url(game_id), "/players"])

def get_settings_url(game_id):
    return "".join([get_game_id_url(game_id), "/setup"])

def get_state_url(game_id):
    return "".join([get_game_id_url(game_id), "/state"])

def create_game(repo_owner, repo_name, username, token):
    return requests.post(url, {"owner": repo_owner, "repo": repo_name, "username": username, "token": token})

def join_game(username, game_id):
    return requests.post(get_players_url(game_id), {"username": username})
    
def change_settings(contributors=None, excludeMerges=True, lowerCase=False):
    if contributors == None:
        return requests.post(get_settings_url(game_id), {"excludeMerges": excludeMerges, "lowerCase": lowerCase})
    return requests.post(get_seetings_url(game_id), {"contributors": contributors, "excludeMerges": excludeMerges, "lowerCase": lowerCase})

def get_game_state(game_id):
    return requests.get(get_state_url(game_id))

def set_game_state(game_id, state):
    states = ["setup", "started", "finished"]
    if state in states:
        return requests.put(get_state_url(game_id), {"state": state}
    raise ValueError("Wrong state, has to be setup, started or finished")
