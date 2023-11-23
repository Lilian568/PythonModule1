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