import math
#Ex 3.1
i =  float(input("Enter the length of a zander in centimeters"))
if i >= 42:
    print("the zander can caught the fish")
else:
    print("the zander release the fish back into the lake.")

#Ex3.2
i = (input("enter the cabin class of a cruise ship"))
if i == "LUX":
     print("upper-deck cabin with a balcony.")
elif i== "A":
    print("above the car deck, equipped with a window.")
elif i=="B":
    print("windowless cabin above the car deck.")
elif i=="C":
    print("windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")

#Ex3.3
gender = (input(" What is your biological gender? "))
hemoglobin_value = float(input("Enter your hemoglobin value (g/l): "))
if gender =="female":
    if 117 <= hemoglobin_value <= 155:
        print("Your hemoglobin level is normal for female")
    elif hemoglobin_value < 117:
        print ("Your hemoglobin level is low for female")
    else:
        print("Your hemoglobin level is high for female")
elif gender == "male":
    if 134 <= hemoglobin_value <= 167:
        print("Your hemoglobin level is normal for male")
    elif hemoglobin_value < 134:
        print("Your hemoglobin level is low for male")
    else:
        print("Your hemoglobin level is high for male")
else:
     print("Your value is invalid")

#Ex3.4
year = int(input ("Enter the year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 ==0):
    print("This is a leap year. ")
else:
    print ("This is not a leap year. ")
