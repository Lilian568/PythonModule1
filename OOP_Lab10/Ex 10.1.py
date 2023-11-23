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