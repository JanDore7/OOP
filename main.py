
class Point:
    color = 'red'
    circle = 2

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return (self.x, self.y)


pt = Point()
print(pt.__dict__)
print(10*'@')
pt.set_coords(1, 2)
print(pt.get_coords())

f = getattr(pt, 'get_coords')
print(f())
