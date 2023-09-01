import math

class Shape:
    def __init__(self, name) -> None:
        self.name = name

    def perimiter(self):
        raise NotImplementedError("perimiter")

    def area(self):
        raise NotImplementedError("area")

    def density(self, weight):
        return weight / self.area()

class Square(Shape):
    def __init__(self, name, side) -> None:
        super().__init__(name)
        self.side = side

    def perimiter(self):
        return self.side * 4

    def area(self):
        return self.side ** 2

class Circle(Shape):
    def __init__(self, name, radius) -> None:
        super().__init__(name)
        self.radius = radius

    def perimiter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2

examples = [Square("square", 5), Circle("circle", 5)]
for thing in examples:
    n = thing.name
    p = thing.perimiter()
    a = thing.area()
    print(f"{n} perimeter: {p:.2f}, area: {a:.2f}")
    d = thing.density(10)
    print(f"{n} density: {d:.2f}")
