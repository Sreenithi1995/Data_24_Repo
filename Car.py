class Car:
    def __init__(self, car_make, max_speed):
        self.car_make = car_make
        self.max_speed = max_speed
        self.current_speed = 0

    def increase_speed(self, speed_increase):
      if self.current_speed + speed_increase > self.max_speed:
          print(f"Your car cannot go any quicker than {self.max_speed} miles")
          self.current_speed = self.max_speed
      else:
          self.current_speed += speed_increase


my_car = Car("Bentley", 200)

print(my_car.car_make)
print(my_car.current_speed)
my_car.increase_speed(150)
print(my_car.current_speed)
my_car.increase_speed(75)
print(my_car.current_speed)
