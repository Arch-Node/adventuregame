import items
import world
import random
import dice


class Player:
    def __init__(
            self,
            strength=dice.roll(6, 3),
            dexterity=dice.roll(6, 3),
            constitution=dice.roll(6, 3),
            intelligence=dice.roll(6, 3),
            wisdom=dice.roll(6, 3),
            charisma=dice.roll(6, 3)):
        self.level = 1
        self.xp = 0
        self.copper = 10
        self.silver = 0
        self.gold = 0
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        if self.strength < 8:
            self.strength = 8
        if self.dexterity < 8:
            self.dexterity = 8
        if self.constitution < 10:
            self.constitution = 10
        if self.intelligence < 8:
            self.intelligence = 8
        if self.wisdom < 8:
            self.wisdom = 8
        if self.charisma < 8:
            self.charisma = 8
        self.hp = 100
        self.armor_class = 10 + int((self.dexterity-10)/2)
        self.inventory = [items.Copper(self.copper), items.Mace()]
        self.location_x, self.location_y = world.starting_position
        self.victory = False

    def is_alive(self):
        return self.hp > 0

    def print_inventory(self):
        for item in self.inventory:
            print(item, '\n')

    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        print(world.tile_exists(self.location_x, self.location_y).intro_text())

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)

    def attack(self, enemy):
        best_weapon = None
        weapon_list = {}
        for i in self.inventory:
            if isinstance(i, items.Weapon):
                weapon_list[i.name] = i.damage
                best_weapon_check = max(weapon_list, key=lambda k: weapon_list[k])
                if i.name == best_weapon_check:
                    best_weapon = i
        print("You use {} against {}!".format(best_weapon.name, enemy.name))
        hit_roll = dice.roll(20, 1, True)
        hit_plus_bonus = hit_roll + int((self.strength-10)/2)
        print("You have {} to hit {}.".format(hit_plus_bonus, enemy.name))
        if hit_plus_bonus >= enemy.armorClass:
            enemy.hp -= dice.roll(best_weapon.damage, 1, True) + int((self.strength-10)/2)
            if int((self.strength-10)/2) == 0:
                pass
            else:
                print("Adding STR mod({}) to the attack".format(int((self.strength-10)/2)))
            if not enemy.is_alive():
                print("You killed the {}!".format(enemy.name))
                self.xp += enemy.xp
                print("You gained {} xp and have a total of {} xp.".format(enemy.xp, self.xp))
            else:
                print("{} HP is {}".format(enemy.name, enemy.hp))
        else:
            print("You missed the {}.".format(enemy.name))

    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)

    def flee(self, tile):
        """Moves the player randomly to an adjacent tile"""
        available_moves = tile.adjacent_moves()
        r = random.randint(0, len(available_moves) - 1)
        self.do_action(available_moves[r])
