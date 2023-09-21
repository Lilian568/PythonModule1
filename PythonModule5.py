"""
#Ex5.1
import random
num_dice = int(input("How many dice would you want to roll? "))
sum_of_roll = 0
#Roll the dice and calculate the sum
for _ in range(num_dice):
    roll = random.randint(1, 6)
    print(f"Rolled:{roll}")
    sum_of_roll += roll
print (f"Sum of the rolls: {sum_of_roll}")

#Ex5.2
numbers = []
#Continue prompting the user for input untill they enter an empty string to quit
while True:
    user_input = input("Enter a number: ")
    if user_input == "":
        break
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input.please enter a valid number.")
if len(numbers) >=5:
    numbers.sort(reverse=True)
    print ("Five greatest numbers in descending order:")
    for i in range(5):
        print(numbers[i])
else:
    print("you entered less than five numbers, so there are not enough to display.")

#Ex5.3
list_number = [2,3,5,7,9]

def print_list(list_example):
    print("here is the list")
    for element in list_example:
        print(f"{element}")
    return
print("here is the list")
"""


list_num = [2,3,4,5]
check_num =8

def is_prime_number(number_to_check, list_of_number):
    for number in list_of_number:
        remaining_value = number_to_check % number
        if remaining_value == 0:
            print(f"{number_to_check} is not a prime number")
            break
        else:
            print(f"{number_to_check}/{number} remaning {remaining_value} ")
    else:
        print(f"{number_to_check} is a prime number")
    return
is_prime_number(check_num, list_num)




        


"""
# Ex5.4
cities = []
for i in range(5):
    city_name = input(f"Enter the name of city #{i+1}: ")
    cities.append(city_name)
print("Cities you entered: ")
for city in cities:
    print(city)
"""