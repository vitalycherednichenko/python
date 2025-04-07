# Transform a method into a class method.


class Vector:
    x = 0
    y = 0
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y):
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

    def get_coord(self):
        return self.x, self.y


v = Vector(10, 20)

print(Vector.validate(1))
print(v.get_coord())