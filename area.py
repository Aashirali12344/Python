class Polygon:
    def __init__(self, dimensions):
        self.dimensions = dimensions

    def calculate_area(self):
        pass

class Rectangle(Polygon):
    def calculate_area(self):
        length, width = self.dimensions
        return length * width

class Triangle(Polygon):
    def calculate_area(self):
        base, height = self.dimensions
        return 0.5 * base * height

rect = Rectangle([10, 5])
tri = Triangle([10, 8])

print(f"Rectangle Area: {rect.calculate_area()}")
print(f"Triangle Area: {tri.calculate_area()}")