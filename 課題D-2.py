class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        value = self.height * self.width
        return "{:.2f}".format(value)

    def diagonal(self):
        value = (self.height * self.height + self.width * self.width) ** 0.5
        return "{:.2f}".format(value)


rectangle1 = Rectangle(height=5, width=6)
print(rectangle1.area())  # 30.00
print(rectangle1.diagonal())  # 7.81

rectangle2 = Rectangle(height=3, width=3)
print(rectangle2.area())  # 9.00
print(rectangle2.diagonal())  # 4.24
