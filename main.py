

class Point:
    def __new__(cls, *args, **kwargs):
        print(f'вызов __new__ для {str(cls)}')
        return super().__new__(cls)

    def __init__(self, x=0, y=0):
        print(f'вызов __init__ для {self}')
        self.x = x
        self.y = y


pt = Point()
