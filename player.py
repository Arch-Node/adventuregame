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
        self.level = 3
        self.xp = 900
        self.copper = dice.roll(10, 2)
        self.silver = dice.roll(6, 1)
        self.gold = 0
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        if self.strength < 12:
            self.strength = 12
        if self.dexterity < 12:
            self.dexterity = 12
        if self.constitution < 12:
            self.constitution = 12
        if self.intelligence < 7:
            self.intelligence = 7
        if self.wisdom < 7:
            self.wisdom = 7
        if self.charisma < 7:
            self.charisma = 7
        self.max_hp = 10 + ((self.level - 1)*6) + int((self.constitution-10)/2)
        self.hp = self.max_hp
        self.armor_class = 11 + int((self.dexterity-10)/2)
        self.inventory = [items.Copper(self.copper), items.Mace(), items.Silver(self.silver)]
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

    def wait(self):
        if dice.roll(6, 1) > 1:
            heal = dice.roll(6, 1)
            # print("HP: {}/{}, Heal: {}".format(self.hp, self.max_hp, heal))
            if self.max_hp >= self.hp:
                hp_to_heal = self.max_hp - self.hp
                if hp_to_heal == 0:
                    print("Time passes")
                else:
                    if hp_to_heal >= heal:
                        self.hp += heal
                        print("You heal {} hit points.".format(heal))
                    else:
                        reduced_heal = hp_to_heal
                        self.hp += reduced_heal
                        print("You heal {} hit points.".format(reduced_heal))
            else:
                print("Time Passes")
        else:
            print("Time passes.")

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
                self.copper += enemy.copper
                self.silver += enemy.silver
                print("You gained {} xp and have a total of {} xp.".format(enemy.xp, self.xp))
                if enemy.copper or enemy.silver != 0:
                    print("You gained: {}cp, {}sp, {}gp".format(enemy.copper, enemy.silver, enemy.gold))
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
