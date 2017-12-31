import dice


class Item:
    """The base class for all items"""
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)


class Copper(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Copper",
                         description="Coins worth {} copper.".format(str(self.amt)),
                         value=self.amt)


class Silver(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Silver",
                         description="Coins worth {} silver.".format(str(self.amt)),
                         value=self.amt)


class Weapon(Item):
    def __init__(self, name, description, value, damage, damage_type):
        self.damage = damage
        self.damage_type = damage_type
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)


class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
                         description="A fist-sized rock, suitable for bludgeoning.",
                         value=0,
                         damage=4,
                         damage_type="bludgeoning"
                         )


class Dagger(Weapon):
    def __init__(self):
        super().__init__(name="Dagger",
                         description="A fist-sized dagger, suitable for bludgeoning.",
                         value=2,
                         damage=4,
                         damage_type="piercing"
                         )


class Mace(Weapon):
    def __init__(self):
        super().__init__(name="Mace",
                         description="A metal ball on a stick, suitable for bludgeoning.",
                         value=5,
                         damage=6,
                         damage_type="bludgeoning"
                         )
