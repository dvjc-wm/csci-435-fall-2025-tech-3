import descriptions as desc
import model_manager as mm

def get_full_map():
    # keys: rooms
    # values: available directions
    return {
        "0": { # "West of House"
            "moves": {
                "e": "The door is boarded and you can't move the boards.",
                "ne": "1",
                "n": "1",
                "nw": "You can't go that way.",
                "w": "3",
                "sw": "You can't go that way.",
                "s": "2",
                "se": "2",
                "u": "You can't go that way.",
                "d": "You can't go that way.",
            }
        },
        "1": { # "North of House"
            "moves": {
                "e": "6",
                "ne": "You can't go that way.",
                "n": "4",
                "nw": "You can't go that way.",
                "w": "0",
                "sw": "0",
                "s": "The windows are all boarded.",
                "se": "2",
                "u": "You can't go that way.",
                "d": "You can't go that way.",
            },
        },
        "2": { # "South of House"
            "moves": {
                "e": "6",
                "ne": "6",
                "n": "The windows are all boarded.",
                "nw": "0",
                "w": "0",
                "sw": "You can't go that way.",
                "s": "3",
                "se": "You can't go that way."
            },
        },
        "3": { # "Forest"
            "moves": {
                "e": "4",
                "ne": "The rank undergrowth prevents eastward movement",
                "n": "2",
                "nw": "2",
                "w": "3",
                "sw": "You can't go that way.",
                "s": "Storm-tossed trees block your way",
                "se": "You can't go that way.",
                "u": "You can't go that way.",
                "d": "You can't go that way.",
            },
        },
        "4": { # "Forest Path"
            "moves": {
                "e": "The rank undergrowth prevents eastward movement",
                "ne": "You can't go that way.",
                "n": "5",
                "nw": "2",
                "w": "3",
                "sw": "You can't go that way.",
                "s": "Storm-tossed trees block your way",
                "se": "You can't go that way.",
                "u": "7",
                "d": "You can't go that way.",
            },
        },
        "5": { # "Clearing"
            "moves": {
                "e": "3",
                "ne": "You can't go that way.",
                "n": "The forest becomes impenetrable to the north.",
                "nw": "You can't go that way.",
                "w": "3",
                "sw": "You can't go that way.",
                "s": "4",
                "se": "You can't go that way.",
                "u": "You can't go that way.",
                "d": "You can't go that way.",
            },
        },
        "6": { # "Behind House"
            "moves": {
                "e": "5",
                "ne": "You can't go that way.",
                "n": "1",
                "nw": "1",
                "w": "The kitchen window is closed",
                "sw": "2",
                "s": "3",
                "se": "You can't go that way.",
                "u": "You can't go that way.",
                "d": "You can't go that way.",
            },
        },
        "7": { # "Up a Tree"
            "moves": {
                "e": "You can't go that way.",
                "ne": "You can't go that way.",
                "n": "You can't go that way.",
                "nw": "You can't go that way.",
                "w": "You can't go that way.",
                "sw": "You can't go that way.",
                "s": "You can't go that way.",
                "se": "You can't go that way.",
                "u": "You cannot climb any higher.",
                "d": "4",
            },
        },
        "8": { # "Kitchen"
            "moves": {
                "e": "6",
                "ne": "You can't go that way.",
                "n": "You can't go that way.",
                "nw": "You can't go that way.",
                "w": "9",
                "sw": "You can't go that way.",
                "s": "You can't go that way.",
                "se": "You can't go that way.",
                "u": "You can't go that way.",
                "d": "You can't go that way.",
            },
        },
        "9": { # "Living Room"
            "moves": {
                "e": "8",
                "ne": "You can't go that way.",
                "n": "You can't go that way.",
                "nw": "You can't go that way.",
                "w": "The door is nailed shut",
                "sw": "You can't go that way.",
                "s": "You can't go that way.",
                "se": "You can't go that way.",
                "u": "You can't go that way.",
                "d": "You can't go that way.",
            },
        }
    }

def is_valid_movement(movement):
    valid_movements = ['n', 'north'
                     , 's', 'south'
                     , 'e', 'east'
                     , 'w', 'west'
                     , 'ne', 'northeast'
                     , 'nw', 'northwest'
                     , 'sw', 'southwest'
                     , 'se', 'southeast'
                     , 'u',  'up'
                     , 'd',  'down']
    return movement in valid_movements

def normalize_movement(movement):
    m = ""
    if movement[0:1] == 'u':
        m = 'u'
    elif movement[0:1] == 'd':
        m = 'd'
    elif movement[-1] == 'h':
        m = movement[0]
    else:
        if "north" in movement:
            m += "n"
        elif "south" in movement:
            m += "s"
        if "west" in movement:
            m += "w"
        elif "east" in movement:
            m += 'e'
        else:
            m = movement
    return m

def handle_movement(room, movement):

    default_moves = {
                "e": "You can't go that way.",
                "ne": "You can't go that way.",
                "n": "You can't go that way.",
                "nw": "You can't go that way.",
                "w": "You can't go that way.",
                "sw": "You can't go that way.",
                "s": "You can't go that way.",
                "se": "You can't go that way.",
                "u": "You can't go that way.",
                "d": "You can't go that way.",
            }

    if not is_valid_movement(movement):
        moves = default_moves
    elif room not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        moves = default_moves
    else:
        full_map = get_full_map()
        moves = full_map[room]["moves"]

    normalized_movement = normalize_movement(movement)
    next_room = moves[normalized_movement]
    description = next_room

    # look for single exception
    current_window = mm.get_flag_value('window')

    if room == "6" and current_window == "open":
        next_room = "8"

    if next_room.isnumeric():
        # update model location
        mm.update_model('location', next_room)
        description = ""

    return description
