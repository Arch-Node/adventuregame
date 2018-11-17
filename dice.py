import random


def roll(die_type, dice_rolled=1, verbose=False, name='You'):
    if verbose:
        print('-----Rolling %i d%i.-----' % (dice_rolled, die_type))
    dice_sum = 0
    dice_start = dice_rolled
    while dice_rolled > 0:
        dice_rolled -= 1
        die = random.randrange(1, die_type+1)
        if verbose:
            print('%s rolled %i' % (name, die))
        dice_sum += die
    if verbose:
        if dice_start > 1:
            print('-----Sum: %i-----------\n' % dice_sum)
        else:
            print('-----------------------\n')
    return dice_sum


def highest_roll(roll_1, roll_2):
    if roll_1 >= roll_2:
        highest = roll_1
    else:
        highest = roll_2
    return highest


def lowest_roll(roll_1, roll_2):
    if roll_1 <= roll_2:
        lowest = roll_1
    else:
        lowest = roll_2
    return lowest


def dnd_advantage(verbose=False, name='You', die_type=20):
    r1 = roll(die_type, 1, verbose, name)
    r2 = roll(die_type, 1, verbose, name)
    advantage = highest_roll(r1, r2)
    if verbose:
        print('Highest advantage roll: %i' % advantage)
    return advantage


def dnd_disadvantage(verbose=False, name='You', die_type=20):
    r1 = roll(die_type, 1, verbose, name)
    r2 = roll(die_type, 1, verbose, name)
    disadvantage = lowest_roll(r1, r2)
    if verbose:
        print('Lowest disadvantage roll: %i' % disadvantage)
    return disadvantage


def die_modifier(die_roll, modifier, verbose=False, name='You'):
    modified_die = die_roll + modifier
    if verbose:
        print('%s rolled: %i, Modifier: %i. Total modified roll: %i' % (name, die_roll, modifier, modified_die))
    return modified_die


def fudge_dice(verbose=False, name='You'):
    dice_rolled = 4
    output = ''
    sum = 0
    while dice_rolled > 0:
        dice_rolled -= 1
        r = roll(6, 1)
        if r in (1, 2):
            output += '-'
            sum -= 1
        elif r in (3, 4):
            output += '0'
        else:
            output += '+'
            sum += 1
    if verbose:
        list_sum = sum + 2
        ladder_rank = {6: 'Great', 5: 'Good', 4: 'Fair', 3: 'Average', 2: 'Mediocre', 1: 'Poor', 0: 'Terrible'}
        print(name + ' rolled: ' + str(output) + '. Bonus(' + str(sum) + ') ' + ladder_rank[list_sum])
    return sum
