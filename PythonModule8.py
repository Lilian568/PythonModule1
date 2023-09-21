import random


def dice_roll():
    return random.randint(1, 6)


roll_number = 0
while roll_number != 6:
    roll_number = dice_roll()
    print(f"Rolled: {roll_number}")

def roll_dice(sides):
    max_sides = sides
    return random.randint(1, max_sides)
roll_number = 0
max = int(input("enter the maximum number on the dice: "))
while roll_number != max:
    roll_number = roll_dice(max)
    print(f"rolled: {roll_number}")



