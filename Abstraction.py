# An abstract class is created by importing a class named 'ABC'
# from the 'abc' library.
from abc import ABC

# Here, the class 'ABC' is imported to and inherited by the class 'Shape'.
# The class 'Shape' becomes an abstract class when we define abstract methods
# in it. Abstract methods cannot contain any implementation, so we use the
# 'pass' statement to define abstract methods.
class Shape(ABC):
    def calculate_area(self):  # Here, 'calculate_area' is the abstract method of
                               # the abstract class 'Shape'.
        pass


class Circle(Shape):
    radius = 4

    def calculate_area(self):
        return 3.14 * self.radius * self.radius


cir = Circle()  # Object created for the class 'Circle'

# Call to 'calculate_area' method defined inside the class 'Circle'.
print("Area of a circle:", cir.calculate_area())
