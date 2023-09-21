import random
import math


#Ex6.1
def dice_roll():
    return random.randint(1, 6)


roll_number = 0
while roll_number != 6:
    roll_number = dice_roll()
    print(f"Rolled: {roll_number}")
# Ex6.2
def roll_dice(sides):
    max_sides = sides
    return random.randint(1, max_sides)
roll_number = 0
max = int(input("enter the maximum number on the dice: "))
while roll_number != max:
    roll_number = roll_dice(max)
    print(f"rolled: {roll_number}")

#Ex6.3
def volume_liters(x):
    liters = gallon * 3.7854
    return liters
while True:
    gallon = int(input("Enter volume in gallon: "))
    result = volume_liters(gallon)
    if result >= 0:
        print(f"the volume converts from {gallon} gallon to liters is {result} liters")
    else:
        print(f"Invalid value")
        break

#Ex6.4
def sum_of_list(list_of_integer):
    return sum(list_of_integer)


number = (input("enter a number: "))
list_number = []
while True:
    try:
        int_input = int(number)
        list_number.append(int_input)
        number = input("enter a number: ")

    except ValueError:
        print("Invalid input.")
        print(f"This is the sum of the list {list_number}: {sum_of_list(list_number)}")
        break
#Ex6.5
def remove_odd_numbers():
    even_numbers = []
    for num in integer_list:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers
integer_list = []
even_list = remove_odd_numbers()
while True:
    number = int(input("Enter your number:"))
    if number < 0:
        break
    else:
        integer_list.append(number)
print(f"all number have been put into the list: {integer_list}")
print(f"cut down list:{remove_odd_numbers()}")


#Ex6.6
def calculate_unit_price(diameter_cm, price_euros):
    diameter_m = diameter_cm / 100
    area_sqm = math.pi * (diameter_m / 2) ** 2
    unit_price_per_sqm = price_euros / area_sqm
    return unit_price_per_sqm
print("Welcome to the Pizza Calculator!")
diameter1 = float(input("Enter the diameter of the first pizza: "))
price1 = float(input("Enter the price of the first pizza"))
diameter2 = float(input("Enter the diameter of the second pizza: "))
price2 = float(input("Enter the price of the second pizza: "))



def roll_dice():
    return random.randint(1, 6)
def main():
    rolls = 0
    while True:
        result = roll_dice()
        rolls += 1
        print(f"roll {rolls}: {result}")
        if result == 6:
            break
if __name__ == "__main__":
    main()


def roll_dice(sides):
    return random.randint(1, sides)
def main():
    max_sides = int(input("Enter the maximum number of sides on the dice:"))
    rolls = 0
    while True:
        result = roll_dice(max_sides)
        rolls += 1
        print(f"Roll {rolls}:{result}")
        if result ==max_sides:
            break
if __name__ == "__main__":
    main()
