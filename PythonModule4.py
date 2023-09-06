#Ex4.1
#Initialize a variable to start from 1
number = 1
# Use the while loop to iterate through numbers from 1 to 1000
while number <= 1000:
    #check if the number is divisible by 3
    if number % 3 == 0:
        #Print the number if divisible by 3
        print(number)
    #Increment the number
    number += 1

#Ex4.2
#Convert factor from inches to centimeters
inches_to_cm = 2.54
#show the input value to a positive number
inches = 0
#repeat a while loop until the user inputs a negative number
while inches >= 0:
    try:
        #prompt the user for input
        inches = float(input("enter a length in inches"))
        if inches >0:
            #convert inches to centimeters and show the results
            centimeters = inches * inches_to_cm
            print(f"{inches}inches is equal to {centimeters} centimeters")
        else:
            print ('exiting the program.')
    except ValueError:
        print("Invalid input. please enter a valid number.")
print("program ended.")

#Ex4.3
smallest = None
largest = None

# Use a while loop to continuously ask for input
while True:
    user_input = input("Enter a number (or press Enter to quit): ")

    # Check if the user input is empty
    if user_input == "":
        break

    try:
        # Convert the user input to a float
        number = float(user_input)
        # Update the smallest and largest numbers
        if smallest is None or number < smallest:
            smallest = number
        if largest is None or number > largest:
            largest = number
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Check if any numbers were entered
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
#while player_guess != hid_number:
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
#Use the while loop to start the login
while attempts < 5:
    #Request the user for username and password
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


