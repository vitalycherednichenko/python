class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value > 0:
            self._radius = value
        else:
            raise ValueError("Радиус должен быть положительным.")


circle = Circle(5)
print(circle.radius)  # 5
circle.radius = 10
print(circle.radius)  # 10