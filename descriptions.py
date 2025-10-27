import json

def get_locations():
    locations = {
        "0": {
            "title": "West of House",
            "description": {
                "brief": "You are standing in an open field west of a white house, with a boarded front door.",
                "verbose": "You are standing in an open field west of a white house, with a boarded front door."
            },
            "items": {
                "leaflet": "There is a small mailbox here. Inside is a leaflet."
            }
        },
        "1": {
            "title": "North of House",
            "description": {
                "brief": "You are facing the north side of a white house.\nThere is no door here, and all the windows are boarded up.\nTo the north a narrow path winds through the trees.",
                "verbose": "You are facing the north side of a white house.\nThere is no door here, and all the windows are boarded up.\nTo the north a narrow path winds through the trees."
            },
            "items": {}
        },
        "2": {
            "title": "South of House",
            "description": {
                "brief": "You are facing the south side of a white house.\nThere is no door here, and all the windows are boarded.",
                "verbose": "You are facing the south side of a white house.\nThere is no door here, and all the windows are boarded."
            },
            "items": {}
        },
        "3": {
            "title": "Forest",
            "description": {
                "brief": "This is a forest, with trees in all directions.\nTo the east, there appears to be sunlight.",
                "verbose": "This is a forest, with trees in all directions.\nTo the east, there appears to be sunlight."
            },
            "items": {}
        },
        "4": {
            "title": "Forest Path",
            "description": {
                "brief": "This is a path winding through a dimly lit forest.\nThe path heads north-south here.\nOne particularly large tree with some low hanging branches stands at the edge of the path.\nYou hear in the distance the chirping of a small bird.",
                "verbose": "This is a path winding through a dimly lit forest.\nThe path heads north-south here.\nOne particularly large tree with some low hanging branches stands at the edge of the path.\nYou hear in the distance the chirping of a small bird.",
            },
            "items": {}
        },
        "5": {
            "title": "Clearing",
            "description": {
                "brief": "You are in a clearing, with a forest surrounding you on all sides.\nA path leads south.",
                "verbose": "You are in a clearing, with a forest surrounding you on all sides.\nA path leads south."
            },
            "items": {
                "leaves": "On the ground is a pile of leaves."
            }
        },
        "6": {
            "title": "Behind House",
            "description": {
                "brief": "You are behind the white house.\nA path leads into the forest to the east.",
                "verbose": "You are behind the white house.\nA path leads into the forest to the east."
            },
            "items": {
                "kitchen window": "In one corner of the house there is a small window which is slightly ajar."
            }
        },
        "7": {
            "title": "Up a Tree",
            "description": {
                "brief": "You are about 10 feet above the ground nestled among some large branches.\nThe nearest branch above you is above your reach.\nBeside you on the branch is a small bird's nest.",
                "verbose": "You are about 10 feet above the ground nestled among some large branches.\nThe nearest branch above you is above your reach.\nBeside you on the branch is a small bird's nest."
            },
            "items": {
                "egg": "In the bird's nest is a large egg encrusted with precious jewels, apparently scavenged by a childless songbird.\nThe egg is covered with fine gold inlay, and ornamented in lapis lazuli and mother-of-pearl.\nUnlike most eggs, this one is hinged and closed with a delicate looking clasp.\nThe egg appears extremely fragile."
            }
        },
        "8": {
            "title": "Kitchen",
            "description": {
                "brief": "You are in the kitchen of the white house.\nA table seems to have been used recently for the preparation of food.\nTo the east is a small window which is open.",
                "verbose": "You are in the kitchen of the white house.\nA table seems to have been used recently for the preparation of food.\nTo the east is a small window which is open."
            },
            "items": {
                "bottle": "A bottle is sitting on the table containing a quantity of water",
            }
        },
        "9": {
            "title": "Living Room",
            "description": {
                "brief": "You are in in the living room.\nThere is a doorway to the east, a wooden door with strange gothic lettering to the west, which appears to be nailed shut, a trophy case, and a large oriental rug in the center of the room.",
                "verbose": "You are in in the living room.\nThere is a doorway to the east, a wooden door with strange gothic lettering to the west, which appears to be nailed shut, a trophy case, and a large oriental rug in the center of the room."
            },
            "items": {
                "sword": "Above the trophy case hangs a short sword with the word 'Stung' written on the facing side",
            }
        }
    }
    return locations

def get_location_detail(room, detail):
    verbosity = 0

    # fetch verbosity
    with open('game_states.json', 'r') as file:
        game_states = json.load(file)
        verbosity = game_states['verbosity']

    if detail not in ['title', 'description', 'items', 'item_keys']:
        return ''

    locations = get_locations()

    if room in locations.keys():
        if detail == 'title':
            return locations[room][detail]
        elif detail == 'description':
            if verbosity in ["0","1"]:
                verbosity_key = "brief"
                if verbosity == 0:
                    verbosity_key = "verbose"
                return locations[room]["description"][verbosity_key]
        elif detail == 'items':
            list_of_items = '\n'.join(f'{v}' for v in locations[room][detail].values())
            return list_of_items
        elif detail == 'item_keys':
            list_of_item_keys = ', '.join(f'{v}' for v in locations[room]['items'].keys())
            return list_of_item_keys

    return ""