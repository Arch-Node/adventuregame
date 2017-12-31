import dice


class Enemy:
    def __init__(self,
                 name,
                 size,
                 alignment,
                 armorclass,
                 hp,
                 groundspeed,
                 flyingspeed,
                 swimingspeed,
                 damage_die1,
                 dam_die_num1,
                 damage_bonus1,
                 damage_die2,
                 dam_die_num2,
                 damage_bonus2,
                 bonus_to_hit,
                 number_of_attacks,
                 strength,
                 dexterity,
                 constitution,
                 intelligence,
                 wisdom,
                 charisma,
                 xp,
                 cr
                 ):
        self.name = name
        self.size = size
        self.alignment = alignment
        self.armorClass = armorclass
        self.hp = hp
        self.groundspeed = groundspeed
        self.flyingspeed = flyingspeed
        self.swimingspeed = swimingspeed
        self.damage_die1 = damage_die1
        self.dam_die_num1 = dam_die_num1
        self.damage_bonus1 = damage_bonus1
        self.damage_die2 = damage_die2
        self.dam_die_num2 = dam_die_num2
        self.damage_bonus2 = damage_bonus2
        self.bonus_to_hit = bonus_to_hit
        self.number_of_attacks = number_of_attacks
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.xp = xp
        self.cr = cr

    def is_alive(self):
        return self.hp > 0


class GiantSpider(Enemy):
    def __init__(self):
        super().__init__(
            name="Giant Spider",
            size="Large",
            alignment="unaligned",
            armorclass=14,
            hp=dice.roll(10, 4) + 4,
            groundspeed=30,
            flyingspeed=0,
            swimingspeed=15,
            damage_die1=8,
            dam_die_num1=1,
            damage_bonus1=3,
            damage_die2=0,
            dam_die_num2=0,
            damage_bonus2=0,
            bonus_to_hit=5,
            number_of_attacks=1,
            strength=14,
            dexterity=16,
            constitution=12,
            intelligence=2,
            wisdom=11,
            charisma=4,
            xp=450,
            cr=2
        )


class Ogre(Enemy):
    def __init__(self):
        super().__init__(
            name="Ogre",
            size="Large",
            alignment="chaotic evil",
            armorclass=11,
            hp=dice.roll(10, 7) + 21,
            groundspeed=40,
            flyingspeed=0,
            swimingspeed=20,
            damage_die1=8,
            dam_die_num1=2,
            damage_bonus1=4,
            damage_die2=0,
            dam_die_num2=0,
            damage_bonus2=0,
            bonus_to_hit=6,
            number_of_attacks=1,
            strength=19,
            dexterity=8,
            constitution=16,
            intelligence=5,
            wisdom=7,
            charisma=7,
            xp=450,
            cr=2
        )


class BlackBear(Enemy):
    def __init__(self):
        super().__init__(
            name="Black Bear",
            size="Medium",
            alignment="unaligned",
            armorclass=11,
            hp=dice.roll(8, 3) + 6,
            groundspeed=40,
            flyingspeed=0,
            swimingspeed=20,
            damage_die1=6,
            dam_die_num1=1,
            damage_bonus1=2,
            damage_die2=4,
            dam_die_num2=2,
            damage_bonus2=2,
            bonus_to_hit=3,
            number_of_attacks=1,
            strength=15,
            dexterity=10,
            constitution=14,
            intelligence=2,
            wisdom=12,
            charisma=7,
            xp=100,
            cr=.5
        )


class Stirge(Enemy):
    def __init__(self):
        super().__init__(
            name="Stirge",
            size="Tiny",
            alignment="unaligned",
            armorclass=14,
            hp=dice.roll(4),
            groundspeed=10,
            flyingspeed=40,
            swimingspeed=20,
            damage_die1=4,
            dam_die_num1=1,
            damage_bonus1=3,
            damage_die2=0,
            dam_die_num2=0,
            damage_bonus2=0,
            bonus_to_hit=5,
            number_of_attacks=1,
            strength=4,
            dexterity=16,
            constitution=11,
            intelligence=2,
            wisdom=8,
            charisma=6,
            xp=25,
            cr=.125
        )


class Darkmantle(Enemy):
    def __init__(self):
        super().__init__(
            name="Darkmantle",
            size="Small",
            alignment="unaligned",
            armorclass=11,
            hp=dice.roll(6, 5) + 5,
            groundspeed=10,
            flyingspeed=30,
            swimingspeed=15,
            damage_die1=6,
            dam_die_num1=1,
            damage_bonus1=3,
            damage_die2=0,
            dam_die_num2=0,
            damage_bonus2=0,
            bonus_to_hit=5,
            number_of_attacks=1,
            strength=16,
            dexterity=12,
            constitution=13,
            intelligence=2,
            wisdom=10,
            charisma=5,
            xp=100,
            cr=.5
        )


class VioletFungus(Enemy):
    def __init__(self):
        super().__init__(
            name="Violet Fungus",
            size="Medium",
            alignment="unaligned",
            armorclass=5,
            hp=dice.roll(8, 4),
            groundspeed=5,
            flyingspeed=0,
            swimingspeed=2,
            damage_die1=8,
            dam_die_num1=1,
            damage_bonus1=0,
            damage_die2=0,
            dam_die_num2=0,
            damage_bonus2=0,
            bonus_to_hit=5,
            number_of_attacks=dice.roll(4),
            strength=3,
            dexterity=1,
            constitution=10,
            intelligence=1,
            wisdom=3,
            charisma=1,
            xp=50,
            cr=.25
        )


class Goblin(Enemy):
    def __init__(self):
        super().__init__(
            name="Goblin",
            size="Small",
            alignment="neutral evil",
            armorclass=15,
            hp=dice.roll(6, 2),
            groundspeed=30,
            flyingspeed=0,
            swimingspeed=15,
            damage_die1=6,
            dam_die_num1=1,
            damage_bonus1=2,
            damage_die2=0,
            dam_die_num2=0,
            damage_bonus2=0,
            bonus_to_hit=4,
            number_of_attacks=1,
            strength=8,
            dexterity=14,
            constitution=10,
            intelligence=10,
            wisdom=8,
            charisma=8,
            xp=50,
            cr=.25
        )


class Grimlock(Enemy):
    def __init__(self):
        super().__init__(
            name="Grimlock",
            size="Medium",
            alignment="neutral evil",
            armorclass=11,
            hp=dice.roll(8, 2),
            groundspeed=30,
            flyingspeed=0,
            swimingspeed=15,
            damage_die1=4,
            dam_die_num1=1,
            damage_bonus1=3,
            damage_die2=4,
            dam_die_num2=1,
            damage_bonus2=0,
            bonus_to_hit=5,
            number_of_attacks=1,
            strength=16,
            dexterity=12,
            constitution=12,
            intelligence=9,
            wisdom=8,
            charisma=6,
            xp=50,
            cr=.25
        )


class Hobgoblin(Enemy):
    def __init__(self):
        super().__init__(
            name="Hobgoblin",
            size="Medium",
            alignment="lawful evil",
            armorclass=18,
            hp=dice.roll(8, 2) + 2,
            groundspeed=30,
            flyingspeed=0,
            swimingspeed=15,
            damage_die1=8,
            dam_die_num1=1,
            damage_bonus1=1,
            damage_die2=0,
            dam_die_num2=0,
            damage_bonus2=0,
            bonus_to_hit=3,
            number_of_attacks=1,
            strength=13,
            dexterity=12,
            constitution=12,
            intelligence=10,
            wisdom=10,
            charisma=9,
            xp=100,
            cr=.5
        )


class Kobold(Enemy):
    def __init__(self):
        super().__init__(
            name="Kobold",
            size="Small",
            alignment="lawful evil",
            armorclass=12,
            hp=dice.roll(6, 2) - 2,
            groundspeed=30,
            flyingspeed=0,
            swimingspeed=15,
            damage_die1=4,
            dam_die_num1=1,
            damage_bonus1=2,
            damage_die2=0,
            dam_die_num2=0,
            damage_bonus2=0,
            bonus_to_hit=4,
            number_of_attacks=1,
            strength=7,
            dexterity=15,
            constitution=9,
            intelligence=8,
            wisdom=7,
            charisma=8,
            xp=25,
            cr=.125
        )


class Lizardfolk(Enemy):
    def __init__(self):
        super().__init__(
            name="Lizardfolk",
            size="Medium",
            alignment="neutral",
            armorclass=15,
            hp=dice.roll(8, 4) + 4,
            groundspeed=30,
            flyingspeed=0,
            swimingspeed=30,
            damage_die1=4,
            dam_die_num1=1,
            damage_bonus1=2,
            damage_die2=0,
            dam_die_num2=0,
            damage_bonus2=0,
            bonus_to_hit=4,
            number_of_attacks=1,
            strength=15,
            dexterity=10,
            constitution=13,
            intelligence=7,
            wisdom=12,
            charisma=7,
            xp=100,
            cr=.5
        )


class DustMephit(Enemy):
    def __init__(self):
        super().__init__(
            name="Dust Mephit",
            size="Small",
            alignment="neutral evil",
            armorclass=12,
            hp=dice.roll(6, 5),
            groundspeed=30,
            flyingspeed=30,
            swimingspeed=0,
            damage_die1=4,
            dam_die_num1=1,
            damage_bonus1=2,
            damage_die2=0,
            dam_die_num2=0,
            damage_bonus2=0,
            bonus_to_hit=4,
            number_of_attacks=1,
            strength=5,
            dexterity=14,
            constitution=10,
            intelligence=9,
            wisdom=11,
            charisma=10,
            xp=100,
            cr=.5
        )


class Merfolk(Enemy):
    def __init__(self):
        super().__init__(
            name="Merfolk",
            size="Medium",
            alignment="neutral",
            armorclass=11,
            hp=dice.roll(8, 2),
            groundspeed=10,
            flyingspeed=0,
            swimingspeed=40,
            damage_die1=8,
            dam_die_num1=1,
            damage_bonus1=0,
            damage_die2=0,
            dam_die_num2=0,
            damage_bonus2=0,
            bonus_to_hit=2,
            number_of_attacks=1,
            strength=10,
            dexterity=13,
            constitution=12,
            intelligence=11,
            wisdom=11,
            charisma=12,
            xp=25,
            cr=.125
        )


class Orc(Enemy):
    def __init__(self):
        super().__init__(
            name="Orc",
            size="Medium",
            alignment="chaotic evil",
            armorclass=13,
            hp=dice.roll(8, 2) + 6,
            groundspeed=30,
            flyingspeed=0,
            swimingspeed=15,
            damage_die1=12,
            dam_die_num1=1,
            damage_bonus1=3,
            damage_die2=0,
            dam_die_num2=0,
            damage_bonus2=0,
            bonus_to_hit=5,
            number_of_attacks=1,
            strength=16,
            dexterity=12,
            constitution=16,
            intelligence=7,
            wisdom=11,
            charisma=10,
            xp=100,
            cr=.5
        )


class Sahuagin(Enemy):
    def __init__(self):
        super().__init__(
            name="Sahuagin",
            size="Medium",
            alignment="lawful evil",
            armorclass=12,
            hp=dice.roll(8, 4) + 4,
            groundspeed=30,
            flyingspeed=0,
            swimingspeed=40,
            damage_die1=6,
            dam_die_num1=1,
            damage_bonus1=1,
            damage_die2=4,
            dam_die_num2=1,
            damage_bonus2=1,
            bonus_to_hit=3,
            number_of_attacks=1,
            strength=13,
            dexterity=11,
            constitution=12,
            intelligence=12,
            wisdom=13,
            charisma=9,
            xp=100,
            cr=.5
        )


class Skeleton(Enemy):
    def __init__(self):
        super().__init__(
            name="Skeleton",
            size="Medium",
            alignment="lawful evil",
            armorclass=13,
            hp=dice.roll(8, 2) + 4,
            groundspeed=30,
            flyingspeed=0,
            swimingspeed=15,
            damage_die1=6,
            dam_die_num1=1,
            damage_bonus1=2,
            damage_die2=0,
            dam_die_num2=0,
            damage_bonus2=0,
            bonus_to_hit=4,
            number_of_attacks=1,
            strength=10,
            dexterity=14,
            constitution=15,
            intelligence=6,
            wisdom=8,
            charisma=5,
            xp=50,
            cr=.25
        )


class WarhorseSkeleton(Enemy):
    def __init__(self):
        super().__init__(
            name="Warhorse Skeleton",
            size="Large",
            alignment="lawful evil",
            armorclass=13,
            hp=dice.roll(10, 3) + 6,
            groundspeed=60,
            flyingspeed=0,
            swimingspeed=30,
            damage_die1=6,
            dam_die_num1=2,
            damage_bonus1=4,
            damage_die2=0,
            dam_die_num2=0,
            damage_bonus2=0,
            bonus_to_hit=6,
            number_of_attacks=1,
            strength=18,
            dexterity=12,
            constitution=15,
            intelligence=2,
            wisdom=8,
            charisma=5,
            xp=100,
            cr=.5
        )


class Zombie(Enemy):
    def __init__(self):
        super().__init__(
            name="Zombie",
            size="Medium",
            alignment="neutral evil",
            armorclass=8,
            hp=dice.roll(8, 3) + 9,
            groundspeed=20,
            flyingspeed=0,
            swimingspeed=10,
            damage_die1=6,
            dam_die_num1=1,
            damage_bonus1=1,
            damage_die2=0,
            dam_die_num2=0,
            damage_bonus2=0,
            bonus_to_hit=3,
            number_of_attacks=1,
            strength=13,
            dexterity=6,
            constitution=16,
            intelligence=3,
            wisdom=6,
            charisma=5,
            xp=50,
            cr=.25
        )


class GiantPoisonousSnake(Enemy):
    def __init__(self):
        super().__init__(
            name="Giant Poisonous Snake",
            size="Medium",
            alignment="unaligned",
            armorclass=14,
            hp=dice.roll(8, 2) + 2,
            groundspeed=30,
            flyingspeed=0,
            swimingspeed=30,
            damage_die1=4,
            dam_die_num1=1,
            damage_bonus1=4,
            damage_die2=0,
            dam_die_num2=0,
            damage_bonus2=0,
            bonus_to_hit=6,
            number_of_attacks=1,
            strength=10,
            dexterity=18,
            constitution=13,
            intelligence=2,
            wisdom=10,
            charisma=3,
            xp=50,
            cr=.25
        )


class Bandit(Enemy):
    def __init__(self):
        super().__init__(
            name="Bandit",
            size="Medium",
            alignment="neutral",
            armorclass=12,
            hp=dice.roll(8, 2) + 2,
            groundspeed=30,
            flyingspeed=0,
            swimingspeed=15,
            damage_die1=8,
            dam_die_num1=1,
            damage_bonus1=1,
            damage_die2=0,
            dam_die_num2=0,
            damage_bonus2=0,
            bonus_to_hit=3,
            number_of_attacks=1,
            strength=11,
            dexterity=12,
            constitution=12,
            intelligence=10,
            wisdom=10,
            charisma=10,
            xp=25,
            cr=.125
        )


class Acolyte(Enemy):
    def __init__(self):
        super().__init__(
            name="Acolyte",
            size="Medium",
            alignment="neutral",
            armorclass=12,
            hp=dice.roll(8, 2),
            groundspeed=30,
            flyingspeed=0,
            swimingspeed=15,
            damage_die1=4,
            dam_die_num1=1,
            damage_bonus1=0,
            damage_die2=0,
            dam_die_num2=0,
            damage_bonus2=0,
            bonus_to_hit=2,
            number_of_attacks=1,
            strength=10,
            dexterity=10,
            constitution=10,
            intelligence=10,
            wisdom=14,
            charisma=11,
            xp=50,
            cr=.25
        )


class Thug(Enemy):
    def __init__(self):
        super().__init__(
            name="Thug",
            size="Medium",
            alignment="neutral evil",
            armorclass=11,
            hp=dice.roll(8, 5) + 10,
            groundspeed=30,
            flyingspeed=0,
            swimingspeed=15,
            damage_die1=6,
            dam_die_num1=1,
            damage_bonus1=2,
            damage_die2=0,
            dam_die_num2=0,
            damage_bonus2=0,
            bonus_to_hit=4,
            number_of_attacks=2,
            strength=15,
            dexterity=11,
            constitution=14,
            intelligence=10,
            wisdom=10,
            charisma=11,
            xp=100,
            cr=.5
        )


class TribalWarrior(Enemy):
    def __init__(self):
        super().__init__(
            name="Tribal Warrior",
            size="Medium",
            alignment="neutral",
            armorclass=12,
            hp=dice.roll(8, 2) + 2,
            groundspeed=30,
            flyingspeed=0,
            swimingspeed=15,
            damage_die1=8,
            dam_die_num1=1,
            damage_bonus1=3,
            damage_die2=0,
            dam_die_num2=0,
            damage_bonus2=0,
            bonus_to_hit=3,
            number_of_attacks=1,
            strength=13,
            dexterity=11,
            constitution=12,
            intelligence=8,
            wisdom=11,
            charisma=8,
            xp=25,
            cr=.125
        )
