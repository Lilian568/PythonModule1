import random
import math

#Ex6.1
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

#Ex6.2
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

#Ex6.3
def volume_liters(x):
    liters = gallon * 3.7854
    return liters
while True:
    gallon = int(input("Enter volume in gallon: "))
    result = volume_liters(gallon)
    if result > 0:
        print(f"the volume converts from {gallon} gallon to liters is {result} liters")
    else:
        result < 0
        print(f"Invalid value")
        break

#Ex6.4
def sum_of_number(list):
    total = 0
    for x in list:
        total = total + x
    return total
if __name__ == "__main__":
    list_of_integer = (1,2,3,4,5,6,7,8,9,10)
    result = sum_of_number(list_of_integer)
    print(f"The sum of list of integer is:{result}")
    
    
#Ex6.5
def remove_odd_numbers(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers
if __name__ == "__main__":
    integer_list = [1,2,3,4,5,6,7,8,9,10]
    even_list = remove_odd_numbers(integer_list)
    print("Original list:", integer_list)
    print("Cut down list(even numbers only):", even_list)

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
price2 = float(input("Enter the diameter of the second pizza: "))