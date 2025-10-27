import os
import descriptions as desc
import model_manager as mm
import location_manager as lm


def reset_model():
    mm.update_model('verbosity', "0")
    mm.update_model('location', "0")
    mm.update_model('items', [])
    mm.update_model('window', "close")

def show_intro():
    wipe_terminal()
    print('SPORK I: The Trivial Above-ground Empire')
    describe_current_location()
    print('')

def wipe_terminal():
    os.system('cls')


def describe_current_location():
    current_location_details = mm.get_flag_value("location")

    print("")
    print( desc.get_location_detail(current_location_details, "title") )

    print("")
    print( desc.get_location_detail(current_location_details, "description") )

    current_held_inventory = mm.get_flag_value("items")
    all_location_items = desc.get_location_detail(current_location_details, "item_keys")

    if all_location_items not in current_held_inventory:
        print( desc.get_location_detail(current_location_details, "items") )


def fetch_valid_command():
    available_commands = ['n', 's', 'e', 'w', 'ne', 'se', 'nw', 'sw', 'u', 'd'
                        , 'north', 'south', 'east', 'west', 'northeast', 'southeast', 'northwest', 'southwest'
                        , 'verbose', 'brief'
                        , 'i', 'inventory'
                        , 'x', 'exit', 'take'
                        , 'l', 'look', 'open', 'close'
                        , 'read'
                        , 'place'
                        , 'restart', 'cls']
    cmd = input('>')
    if cmd[0:4] == "take":
        return cmd
    if cmd[0:5] == "place":
        return cmd
    if cmd[0:4] == "read":
        return cmd
    while cmd not in available_commands:
        print(F"I don't know the word {cmd}\n")
        cmd = input('>')
    return cmd

reset_model()
show_intro()

valid_command = fetch_valid_command()

continue_loop = valid_command != "exit" and valid_command != "x"

while continue_loop:

    if valid_command == "cls":
        wipe_terminal()
        describe_current_location()

    elif valid_command == "brief":
        mm.update_model('verbosity', "0")
        print('Brief descriptions.')

    elif valid_command == "verbose":
        mm.update_model('verbosity', "1")
        print('Maximum verbosity descriptions.')

    elif valid_command == "read":
        current_inventory = mm.get_flag_value("items")
        if "leaflet" in current_inventory:
            print("\nDirections:")
            print("1. Get to the Forest Path; from mailbox: S -> S -> E")
            print("2. Get the egg (climb the tree, take the egg)")
            print("3. Go behind the house")
            print("4. Open the window")
            print("5. Go west, into the kitchen")
            print("6. Go west, into the living room")
            print("7. Place the egg in the trophy case")

    elif lm.is_valid_movement(valid_command):
        room = mm.get_flag_value("location")
        description = lm.handle_movement(room, valid_command)

        if len(description)>0:
            print(f"\n{description}\n")
        else:
            describe_current_location()

    elif valid_command == "restart":
        reset_model()
        describe_current_location()

    elif valid_command == "look" or valid_command == "l":
        describe_current_location()
        print("")

    elif valid_command == "i" or valid_command == "inventory":
        current_inventory = mm.get_flag_value("items")
        print("You are currently carrying:\n", current_inventory)

    elif valid_command == "open" or valid_command == "close":
        room = mm.get_flag_value("location")
        window_state = mm.get_flag_value("window")
        if room != "6":
            print(f"Nothing here to {valid_command}")
        else:
            if window_state != valid_command:
                mm.update_model("window", valid_command)
                if valid_command == "open":
                    print('With great effort, you open the window far enough to allow entry.')
                else:
                    print('The window closes (more easily than it opened).\n')

    elif valid_command[0:4] == "take":
        current_inventory = mm.get_flag_value("items")
        current_location = mm.get_flag_value("location")
        target_item = valid_command[5:]
        location_items = desc.get_location_detail(current_location, "item_keys")
        location_items_as_array = location_items.split(',')

        if len(location_items_as_array) == 0:
            print("There is nothing to take\n")

        else:
            # auo-assign the first item in the location
            if len(target_item)==0 and len(location_items_as_array)>0:
                item_count = len(location_items_as_array)
                while item_count > 0 and len(target_item)==0 :
                    next_location_item = location_items_as_array[item_count-1]
                    if next_location_item not in current_inventory:
                        target_item = next_location_item.strip()
                    item_count -= 1

            # first validation
            no_inventory = len(current_inventory) == 0
            not_in_inventory = location_items not in current_inventory

            if no_inventory or not_in_inventory:
                location_item_keys = desc.get_location_detail(current_location, "item_keys")

                # second validation
                if target_item in location_item_keys:
                    if no_inventory:
                        current_inventory = [target_item]
                        mm.update_model("items", current_inventory)
                    else:
                        current_inventory.append(target_item)
                        mm.update_model("items", current_inventory)
                    print(f"{target_item} added to inventory.\n")
            else:
                print("All items have been taken\n")

    elif valid_command[0:5] == "place":
        current_location = mm.get_flag_value("location")
        current_inventory = mm.get_flag_value("items")

        if current_location != '9':
            print('You need to be in the living room')
        else:
            if 'egg' not in current_inventory:
                print("You need the egg")
            else:
                print("\nYou gently place the egg in the trophy case.")
                print("You have won the game!")
                continue_loop = False


    if continue_loop:
        valid_command = fetch_valid_command()
        continue_loop = valid_command != "exit" and valid_command != "x"

print("")
