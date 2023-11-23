class Elevator:
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


class Building:
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
