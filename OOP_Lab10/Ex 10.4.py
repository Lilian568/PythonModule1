import random
class Car:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.distance_covered = 0

    def drive(self):
        change = random.randint(-5, 5)
        self.speed += change
        self.distance_covered += self.speed

    def __str__(self):
        return f"{self.name:10} {self.speed:6}km/h {self.distance_covered} km"


class Race:
    def __init__(self, name, distance, car_list):
        self.name = name
        self.distance = distance
        self.car_list = car_list

    def hour_passes(self):
        for car in self.car_list:
            car.drive()

    def print_status(self):
        print(f"{'Car Name':10} | {'Speed':6} | {'Distance Covered'}")
        print('-' * 35)
        for car in self.car_list:
            print(car)

    def race_finished(self):
        return any(car.distance_covered >= self.distance for car in self.car_list)


cars = [Car(f"Car {i}", random.randint(100, 200)) for i in range(1, 11)]

race = Race("Grand Demolition Derby", 8000, cars)
hour = 0


while not race.race_finished():
    if hour % 10 == 0:
        print(f"\nrace Status after {hour} hours:")
        race.print_status()
    race.hour_passes()
    hour += 1
print("\nFinal Race Results:")
race.print_status()
