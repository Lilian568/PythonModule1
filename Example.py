"""
name = []
name = input("Enter your name")
index = []
while name != "" and index < len(name):
    print (name[index])
    index +=1
    # index = index +1

name = input ("Enter your name: ")
for i in name:
    print (i)

number = list(range(1, 5))
print(number)

for number in range(1, 6, 2):
    print(number)

for great in range(3):
    print("good morning! you are cool!")

num = int(input("Enter a number: "))
factorial = []
if num < 0:
    print("the number is invalid. enter another number")
else:
    for i in range (1, num+1):
        factorial = i + factorial
    print(f"the factorial of {num} is {factorial}")

sen = (input("enter a sentence:"))
words = sen.split()
for word in words:
    if word.isalpha():
        print (word[0])

def great(name):#definite the function, name is a parameter
    print ("Hi, soon I am going to br free", name)#body
    return


great("linh")#chau is an argument

def greet (times):
    for i in range (times):
        print("you are beautiful" + str(i+1) + "times")
greet(3)
greet(4)

def grocery (items):
    for item in items:
        print(" " + item)
shopping_list = ("cheese", "cake", "pasta")
grocery(shopping_list)
shopping_list.append ("icecream")
grocery(shopping_list)

def calculation (a, b):
    addition = a+b
    return addition
num1 = int(input("give me the 1st number: "))
num2 = int(input("give me the 2nd number: "))
addition = calculation(num1, num2)
print ("the sum of these two numbers is: ", addition)
"""
def print_spruce(size):
    print("A spruce is coming!")
    for i in range(1, size + 1):
        space = " " * (size - i)
        stars = "*" * (2*i - 1)
        print(space + stars)
print_spruce(6)

