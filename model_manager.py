import json

def update_model(flag,value=0):
    if flag=="verbosity":
        game_states = {}
        with open('game_states.json', 'r') as file:
            game_states = json.load(file)

        game_states['verbosity'] = value
        with open('game_states.json', 'w') as file:
            file.write(json.dumps(game_states))

    elif flag=="location":
        game_states = {}
        with open('game_states.json', 'r') as file:
            game_states = json.load(file)

        game_states['location'] = value
        with open('game_states.json', 'w') as file:
            file.write(json.dumps(game_states))

    elif flag=="items":
        game_states = {}
        with open('game_states.json', 'r') as file:
            game_states = json.load(file)

        game_states['items'] = value
        with open('game_states.json', 'w') as file:
            file.write(json.dumps(game_states))

    elif flag == "window":
        game_states = {}
        with open('game_states.json', 'r') as file:
            game_states = json.load(file)

        if value in ['open', 'close']:
            game_states['window'] = value
            with open('game_states.json', 'w') as file:
                file.write(json.dumps(game_states))


def get_flag_value(flag):
    game_states = {}
    with open('game_states.json', 'r') as file:
        game_states = json.load(file)

    if flag in game_states.keys():
        return game_states[flag]

    return ""
