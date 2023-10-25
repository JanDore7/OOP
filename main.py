
class Vector:
    MIN_CORD = 0
    MAX_CORD = 100

    @classmethod
    def validate(cls, arg):
        return cls.MIN_CORD <= arg <= cls.MAX_CORD

    def __init__(self, x, y):
        self.x = self.y = 0
        # if Vector.validate(x) and Vector.validate(y):
        if self.validate(x) and self.validate(y): # Наиболее предпочтительный вариант
            self.x = x
            self.y = y

        print(self.norm2(self.x, self.y))

    def get_cord(self):
        return self.x, self.y

    @staticmethod
    def norm2(x, y):
        return x*x + y*y


v = Vector(100, 11)


