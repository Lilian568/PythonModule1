# Ex 9.1
class Car():
    def __init__(self, registration=int, maximum_speed=str, current_speed=str, travelled_distance=str):
        self.registration = registration
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def __str__(self):
        return (f"Registration Number: {self.registration}\n"
                f"Maximum speed: {self.maximum_speed} km/h\n"
                f"Current speed: {self.current_speed} km/h\n"
                f"Travelled Distance: {self.travelled_distance} km")


new_car = Car("ABC-123", "142", "0", "0")
print(new_car)


# EX9.2
class Car:
    def __init__(self, registration, maximum_speed, current_speed, travelled_distance):
        self.registration = registration
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        if self.current_speed + speed_change < 0:
            self.current_speed = 0
        elif self.current_speed + speed_change > self.maximum_speed:
            self.current_speed = self.maximum_speed
        else:
            self.current_speed += speed_change

    def __str__(self):
        return (f"Registration Number: {self.registration}\n"
                f"Maximum Speed: {self.maximum_speed} km/h"
                f"\nCurrent Speed: {self.current_speed} km/h"
                f"\nTravelled Distance: {self.travelled_distance} km")


new_car = Car("ABC-123", 142, 0, 0)

print("Initial Speed of the Car:")
print(new_car)
new_car.accelerate(30)
print("\nSpeed of the Car after Accelerating by +30 km/h:")
print(new_car)


new_car.accelerate(70)
print("\nSpeed of the Car after Accelerating by +70 km/h:")
print(new_car)

new_car.accelerate(50)
print("\nSpeed of the Car after Accelerating by +50 km/h:")
print(new_car)

new_car.accelerate(-200)
print("\nSpeed of the Car after Applying the Emergency Brake:")
print(new_car)

#EX9.3
class Car:
    def __init__(self, registration, maximum_speed, current_speed, travelled_distance):
        self.registration = registration
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        self.current_speed
        if self.current_speed + speed_change < 0:
            self.current_speed = 0
        elif self.current_speed + speed_change > self.maximum_speed:
            self.current_speed = self.maximum_speed
        else:
            self.current_speed += speed_change


    def drive(self, hours):
        distance = self.current_speed * hours
        self.travelled_distance +=distance
    def __str__(self):
        return (f"Registration Number: {self.registration}\n"
                f"Maximum Speed: {self.maximum_speed} km/h"
                f"\nCurrent Speed: {self.current_speed} km/h"
                f"\nTravelled Distance: {self.travelled_distance} km")
new_car = Car("ABC-123", 142, 0, 0)

print("Initial Speed of the Car:")
print(new_car)
new_car.accelerate(30)
print("\nSpeed of the Car after Accelerating by +30 km/h:")
print(new_car)


new_car.accelerate(70)
print("\nSpeed of the Car after Accelerating by +70 km/h:")
print(new_car)

new_car.accelerate(50)
print("\nSpeed of the Car after Accelerating by +50 km/h:")
print(new_car)
new_car.drive(1.5)
print("\nTravelled Distance of the Car after Driving for 1.5 hours:")
print(new_car)

#EX9.4
import random
class Car:
    def __init__(self, registration, maximum_speed, current_speed, travelled_distance):
        self.registration = registration
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        if self.current_speed + speed_change < 0:
            self.current_speed = 0
        elif self.current_speed + speed_change > self.maximum_speed:
            self.current_speed = self.maximum_speed
        else:
            self.current_speed += speed_change

    def drive(self):
        pass


    def drive(self, hours):
        distance = self.current_speed * hours
        self.travelled_distance += distance
    def __str__(self):
        return (f"Registration Number: {self.registration}"
                f"\nMaximum Speed: {self.maximum_speed} km/h"
                f"\nCurrent Speed: {self.current_speed} km/h"
                f"\nTravelled Distance: {self.travelled_distance} km")
cars = [Car(f"ABC-{i+1}",random.randint(100, 200)) for i in range(10)]
while True:
    for car in cars:
        car.accelerate(random.randint(-10, 15))
        car.drive(1)
    if any(car.travelled_distance >= 10000 for car in cars):
        break
print("{:<12} {:<14} {:<13} {:<18}".format("Car", "Maximum Speed (km/h)", "Current Speed", "Travelled Distance (km)"))
for car in cars:
    print("{:<12} {:<14} {:<13} {:<18}".format(car.registration,car.maximum_speed,car.current_speed, car.travelled_distance))