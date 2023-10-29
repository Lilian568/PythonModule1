# EX10.1
class Elevator():
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = self.bottom_floor

    def go_to_floor(self, target_floor):
        if target_floor < self.bottom_floor or target_floor > self.top_floor:
            print("Invalid input. Try again!")
            return
        while self.current_floor != target_floor:
            if self.current_floor < target_floor:
                self.floor_up()
            else:
                self.floor_down()
        return self.current_floor

    def floor_up(self):
        self.current_floor += 1

    def floor_down(self):
        self.current_floor -= 1


elevator = Elevator(bottom_floor=1, top_floor=10)
target_floor = 5
elevator.go_to_floor(5)
print("Moving the elevator to floor", target_floor)
elevator.go_to_floor(1)
print("Moving the elevator back to bottom floor")


# EX10.2
class Building():
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.num_elevators = num_elevators
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_num, destinaiton_floor):
        if elevator_num < 0 or elevator_num >= self.num_elevators:
            print("Invalid number. Try again.")
            return

        elevator = self.elevators[elevator_num]
        print(f"Elevator running from {elevator_num} to floor {destinaiton_floor}")
        elevator.go_to_floor(destinaiton_floor)


building = Building(bottom_floor=1, top_floor=10, num_elevators=3)
building.run_elevator(0, 7)
building.run_elevator(3, 8)
building.run_elevator(2, 9)


# EX10.3
class Building():
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.num_elevators = num_elevators
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_num, destinaiton_floor):
        if elevator_num < 0 or elevator_num >= self.num_elevators:
            print("Invalid number. Try again.")
            return

    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom_floor)
            print(f"Fire alarm active. Elevator is now on the bottom floor.")


building = Building(bottom_floor=1, top_floor=10, num_elevators=3)
building.fire_alarm()

# EX10.4
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
