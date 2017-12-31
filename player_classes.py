import dice


class StatGenerationPlayer:
    def __init__(self,
                 strength=dice.roll(6, 3),
                 dexterity=dice.roll(6, 3),
                 constitution=dice.roll(6, 3),
                 intelligence=dice.roll(6, 3),
                 wisdom=dice.roll(6, 3),
                 charisma=dice.roll(6, 3)
                 ):
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
        self.hp = 8 + (self.constitution-10)/2

    def __str__(self):
        return "STR: %i\nDEX: %i\nCON: %i\nINT: %i\nWIS: %i\nCHA: %i\n-----------------------\nHP: %i" % (
            self.strength,
            self.dexterity,
            self.constitution,
            self.intelligence,
            self.wisdom,
            self.charisma,
            self.hp
        )


roll = dice.roll(6, 3, True)

stat_set = StatGenerationPlayer()
print(stat_set)
