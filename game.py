import world
from player import Player


def play():
    world.load_tiles()
    player = Player()
    room = world.tile_exists(player.location_x, player.location_y)
    print("STR: %i, DEX: %i, CON: %i, INT: %i, WIS: %i, CHA: %i" % (player.strength,
                                                                    player.dexterity,
                                                                    player.constitution,
                                                                    player.intelligence,
                                                                    player.wisdom,
                                                                    player.charisma))
    print("HP: %i" % player.hp)
    print("AC: %i" % player.armor_class)
    print(room.intro_text())
    while player.is_alive() and not player.victory:
        room = world.tile_exists(player.location_x, player.location_y)
        # print('loc: ' + str(player.location_x) + ', ' + str(player.location_y))
        room.modify_player(player)
        if player.is_alive() and not player.victory:
            print("HP: {} | Choose an action:\n".format(player.hp))
            available_actions = room.available_actions()
            for action in available_actions:
                print(action)
            action_input = input('Action: ')
            for action in available_actions:
                if action_input == action.hotkey:
                    player.do_action(action, **action.kwargs)
                    break


if __name__ == "__main__":
    play()
