#Ex4.1
number = 1
while number <= 1000:
    if number % 3 == 0:
        print(number)
    number += 1

#Ex4.2
inches_to_cm = 2.54
inches = 0
while inches >= 0:
    inches = float(input("Enter a length in inches"))
    if inches > 0:
        centimeters = inches * inches_to_cm
        print(f"{inches} inches is equal to {centimeters} centimeters")
    else:
        print("exit the program")

#Ex4.2
smallest = None
largest = None
while True:
    user_input = input("Enter a number: ")
    if user_input == "":
        break

    try:
        number = float(user_input)
        if smallest is None or number < smallest:
            smallest = number
        if largest is None or number > largest:
            largest = number
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if smallest is not None and largest is not None:
    print(f"Smallest number: {smallest}")
    print(f"Largest number: {largest}")
else:
    print("No numbers were entered.")

#Ex4.4
import random
hid_number = random.randint(1,10)
player_guess = 0
while not player_guess ==hid_number:
    player_guess = int(input("guess the number between 1 and 10:"))
    if player_guess < hid_number:
        print("your number is too low, let's try again.")
    if player_guess > hid_number:
        print("your number is too high, let's try again.")
else:
        print("Correct")

#Ex4.5
correct_username = "python"
correct_password = "rules"
attempts = 0
while attempts < 5:
    username = input("Enter your username: ")
    password = input("enter your password: ")
    if username == correct_username and password == correct_password:
        print("welcome!")
        break
    else:
        print ("Incorrect username or password. Please try again. ")
        attempts +=1
if attempts >= 5:
    print ("Access denied. you have reached the maximum numbers of login attempts.")

#Ex4.6
point_N = int(input("How many random points to generate? "))
point_n = 0
point_generated = 1
while point_generated <= point_N:
    random_x = random.uniform(-1,1)
    random_y = random.uniform(-1, 1)
    point_generated +=1
    equation_check = random_x * random_x + random_y * random_y
    if equation_check <1:
        point_n +=1
    pi = 4 * point_n / point_N
    print (f"Approximate value of Pi:{pi}")



