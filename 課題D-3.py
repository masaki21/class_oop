class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        value = self.side * self.side
        if value == int(value):
            return int(value)
        return "{:.2f}".format(value)

    def diagonal(self):
        value = (self.side * self.side + self.side * self.side) ** 0.5
        return "{:.2f}".format(value)


square1 = Square(side=1.5)
print(square1.area())  # 2.25
print(square1.diagonal())  # 2.12

square2 = Square(side=15)
print(square2.area())  # 225
print(square2.diagonal())  # 21.21
