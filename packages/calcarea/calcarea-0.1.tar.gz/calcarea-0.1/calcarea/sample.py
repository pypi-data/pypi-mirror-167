class Circle:
    pi = 3.14

    def __init__(self, redius):
        self.radius = redius

    def calculate_area(self):
        return self.pi * self.radius * self.radius

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

# function
def area(shape):
    # call action
    return shape.calculate_area()

# create object
cir = Circle(int(input("radius: ")))
print("Area of circle: ", area(cir))
rect = Rectangle(int(input("length: ")), int(input("breadth: ")))

# call common function

print("Area of rectangle", area(rect))