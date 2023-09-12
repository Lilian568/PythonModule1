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

def print_spruce(size):
    print("A spruce is coming!")
    for i in range(1, size + 1):
        space = " " * (size - i)
        stars = "*" * (2*i - 1)
        print(space + stars)
print_spruce(6)

 # Session 6
 myTuples = (1,35,5)
 for i in myTuples:
     print(i)
point = (2,4)
x,y = point
print(point)
print(f"here is the x {x} value")
student = ("Linh", 20, "Computer science")
print(f"Name: {student[0]}, Age:{student[1], Major{student[2]}")


grades = (6,8,9,10)
total = 0
for grade in grades:
    total +=grade
print(f"Here is the total{total}: ")

students = []
students.append(("Linh", (60,70,80,100,40)))
students.append(("Son", (50,70,60,90,100)))
students.append(("Khanh", (80,90,70,80,100)))
found = False
print(students)
for student in students:
    if student[0] == "Linh":
        print(f"the name, {students[0][0]}")
        print(f"the grades, {students[0][1]}")
        avg = sum(student[1])/ len(student[1])
        print(f"The average of the {student[0]},  is {avg}")

        found = True
        break
    if not found:
        print("Invalid name")
student.append("Divid")

student = {
    "name": "Amir",
    "grade": "A",
    "courses":["Math","Physics", "Programming"]
}
print("Name: ", student["name"])
print("grade", student["grade"])
print("courses", student["courses"])

student["age"] = 21
print("Age ", student["age"])

student["city"] = "ESPOO"
student["age"] = 21
print(student)
for key, value in student.items():
    print(key + " :", value)

if "age" in student:
    print("age: ", student["age"])
else:
    print("not in the dictionary")

"""
shopping_list = {
    "milk": 4,
    "juice": 3,
    "apple": 3,
    "oat": 2
}
def add_item_to_shopping_list (shopping_list, item, quantity):
    if item in shopping_list:
        shopping_list[item] += quantity
    else:
        shopping_list[item] = quantity
add_item_to_shopping_list (shopping_list,"egg", 5 )
def display_shopping_list(shopping_list):
    total = 0
    print("Shopping List:")
    for item, quantity in shopping_list.items():
        print(f"{item}:{quantity}")
        total += quantity
    print(f"total items: {total}")
display_shopping_list (shopping_list)