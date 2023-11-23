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