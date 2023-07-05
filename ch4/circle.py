import math


class Circle:
    def __init__(self, radius) -> None:
        """
        __변수명 : private 와 동일
        """
        self.__radius = radius

    def getCircum(self):
        return 2 * math.pi * self.__radius

    def getArea(self):
        return math.pi * (self.__radius**2)

    def getRadius(self):
        return self.__radius

    def setRadius(self, radius):
        self.__radius = radius


Circle = Circle(10)
# print(Circle.__radius) #AttributeError: 'Circle' object has no attribute '__radius'
# __radius접근 ==> getter, setter 이용
print("반지름 :{}".format(Circle.getRadius()))
print("원의 둘레 :{}".format(Circle.getCircum()))
print("원의 면적 :{}".format(Circle.getArea()))
