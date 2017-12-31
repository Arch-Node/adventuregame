import random


def roll(die_type, dice_rolled=1, verbose=False):
    if verbose:
        print('-----Rolling %i d%i.-----' % (dice_rolled, die_type))
    dice_sum = 0
    dice_start = dice_rolled
    while dice_rolled > 0:
        dice_rolled -= 1
        die = random.randrange(1, die_type+1)
        if verbose:
            print('You rolled \033[96m%i\033[0m' % die)
        dice_sum += die
    if verbose:
        if dice_start > 1:
            print('-----Sum: %i-----------' % dice_sum)
        else:
            print('-----------------------')
    return dice_sum
