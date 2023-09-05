import math
import random

#Ex1
name= input("What is your name?")
print ("Hello, ", name)

#Ex2
import math
rad= input("what is radius of the circle?")
r = int(rad)
result = math.pi*r**2
print(f"The area of the circle: {result:2.2f}")

#Ex3
length = float(input("Enter length of rectangle:"))
width = float(input("enter width of rectangles: "))
perimeter = (length+width)*2
rec_area = length*width
print (f"perimeter of this rectangle:{ perimeter: .2f}")
print (f"Area of this rectangle: {rec_area: .2f}")

#Ex4
number1 = int(input("Enter the first integer number: "))
number2 = int(input("Enter the second integer number: "))
number3 = int(input("Enter the third integer number: "))
sum = number1 + number2 + number3
product= number1+number2+number3
average= sum/3
print(f"Sum: {sum}")
print(f"Product: {product}")
print(f"Average:{average}")

#Ex5
talent = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))
tal_pou = talent*20
pou_lt = (tal_pou + pounds)*32
lt_gr = (lots + pou_lt)*13.3
kilograms = int(lt_gr/1000)
grams = (lt_gr/1000 - kilograms)*1000
print(f"The weight in mordern units: kilograms and {grams:2f} grams")

#Ex6
lock3_digit1 = random.randint(0,9)
lock3_digit2 = random.randint(0,9)
lock3_digit3 = random.randint(0,9)
print(f"3-digit code combination: {lock3_digit1}{lock3_digit2}{lock3_digit3}")
lock4_digit1 = random.randint(1,6)
lock4_digit2 = random.randint(1,6)
lock4_digit3 = random.randint(1,6)
lock4_digit4 = random.randint(1,6)
print(f"4-digit code combination: {lock4_digit1}{lock4_digit2}{lock4_digit3}{lock4_digit4}")