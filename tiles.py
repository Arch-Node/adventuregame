import items
import enemies
import actions
import world
import dice


class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()

    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles"""
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves

    def available_actions(self):
        """Returns all of the available actions in this room."""
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
        moves.append(actions.Wait())
        return moves


class StartingRoom(MapTile):
    def intro_text(self):
        return """
        You find yourself in a cave with a flickering torch on the wall.
        You can make out four paths, each equally as dark and foreboding. 
        """

    def modify_player(self, player):
        # Room has on action on player
        pass


class LootRoom(MapTile):
    def __init__(self, x, y, item, is_loot=False):
        self.item = item
        self.is_loot = is_loot
        super().__init__(x, y)

    def add_loot(self, player):
        player.inventory.append(self.item)

    def modify_player(self, player):
        if self.is_loot is False:
            self.is_loot = True
            self.add_loot(player)


class LeaveCaveRoom(MapTile):
    def intro_text(self):
        return """
        You see a bright light in the distance...
        ... it grows as you get closer! It's sunlight!
        
        
        Victory is yours! You were not eaten by a grue.
        """

    def modify_player(self, player):
        player.victory = True


class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, player):
        if self.enemy.is_alive():
            hit_roll = dice.roll(20)
            print("{} rolled a {} to attack".format(self.enemy.name, hit_roll))
            hit_plus_bonus = hit_roll + self.enemy.bonus_to_hit
            print("{} has {} to hit your AC of {}.".format(self.enemy.name, hit_plus_bonus, player.armor_class))
            if hit_plus_bonus >= player.armor_class:
                damage1 = dice.roll(self.enemy.damage_die1, self.enemy.dam_die_num1) + self.enemy.damage_bonus1
                if self.enemy.dam_die_num2 == 0:
                    damage2 = 0
                else:
                    damage2 = dice.roll(self.enemy.damage_die2, self.enemy.dam_die_num2) + self.enemy.damage_bonus2
                damage_total = damage1 + damage2
                player.hp = player.hp - damage_total 
                print("\033[33m{} does {} damage.\033[0m You have {} HP remaining.".format(self.enemy.name,
                                                                                           damage_total,
                                                                                           player.hp))
            else:
                print("{}'s attack misses.".format(self.enemy.name))

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
            actions1 = self.adjacent_moves()
            actions1.append(actions.ViewInventory())
            actions1.append(actions.Wait())
            return actions1


class EmptyCavePath(MapTile):
    def intro_text(self):
        return """
        Another unremarkable part of the cave. You must find the exit.
        """

    def modify_player(self, player):
        # Room has no action on player
        pass


class SpringRoom(MapTile):
    def intro_text(self):
        return """
        You hear a bubbling spring. You feel thirsty and take a drink.
        The water feels cool and refreshing.
        """

    def modify_player(self, player):
        player.hp += 5
        print("The water heals 5 damage. You have {} HP.".format(player.hp))


class GiantSnakeRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.GiantPoisonousSnake())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A giant slithers down from the rocks above!
            """
        else:
            return """
            The corpse of a dead snake rots on the ground.
            """


class KoboldRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Kobold())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A kobold creeps out from the rocks!
            """
        else:
            return """
            The corpse of a Kobold rots on the ground.
            """


class GiantSpiderRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.GiantSpider())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A giant spider jumps down from its web in front of you!
            """
        else:
            return """
            The corpse of a dead spider rots on the ground.
            """


class OgreRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Ogre())\


    def intro_text(self):
        if self.enemy.is_alive():
            return """
            An ogre hurls a rock and hits you quite hard!
            """
        else:
            return """
            The body of a dead ogre takes up most of the room.
            """


class BearRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.BlackBear())\


    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A bear comes at you from out of the darkness. 
            """
        else:
            return """
            The body of a dead bear lies in the corner. If you are lost too long you might need to make a coat.
            """


class FindGoldRoom(LootRoom):
    def __init__(self, x, y, is_loot):
        super().__init__(x, y, is_loot)

    def modify_player(self, player):
        if self.is_loot:
            pass
        else:
            player.gold += 5

    def intro_text(self):
        if self.is_loot:
            return """
            Another unremarkable part of the cave. You must forge onwards.
            """
        else:
            return """
            You see some gold in the corner of the room.
            You found 5 gold.
            """


class FindDaggerRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dagger())

    def intro_text(self):
        if self.is_loot:
            return """
            The shadows dance on the cave walls.
            This reminds you why you don't like caves.
            """
        else:
            return """
            You notice something shiny in the corner.
            It's a dagger! You pick it up.
            """
