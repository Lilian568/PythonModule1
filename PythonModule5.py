
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
    except valueerror:
        print("Invalid input.please enter a valid number.")
if len(numbers) >=5:
    numbers.sort(reverse=True)
    print ("Five greatest numbers in descending order:")
    for i in range(5):
        print(numbers[i])
else:
    print("you entered less than five numbers, so there are not enough to display.")

#Ex5.3
num = int(input("Enter a number: "))
prime = True
if num ==1:
    print ("This is not a prime number")
else:
    for i in range(2,num):
        if num % i ==0:
            print("This is not a prime number.")
            break
    if prime == True:
        print("This is a prime number.")

# Ex5.4
cities = []
for i in range(5):
    city_name = input(f"Enter the name of city #{i+1}: ")
    cities.append(city_name)
print("Cities you entered: ")
for city in cities:
    print(city)

