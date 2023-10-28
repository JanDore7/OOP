class Point:
    def __init__(self, x=0 , y=0):
        self.__x = x
        self.__y = y

    def se_cord(self, x, y):
        if type(x) in (int, float) and type(y) in (int, float):
            self.__x = x
            self.__y = y
        raise ValueError("Координаты должны быть числами")

    def get_cord(self):
        return self.__x, self.__y


