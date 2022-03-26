import math
class Polygon:
    __r=0
    __area=0
    def __init__(self, r):
        self.__r=r
        self.calc_area()
    def calc_area(self):
        self.__area=(((self.__r**2) * math.sqrt(3))/4)*6
    def r(self):
        return self.__r
    def area(self):
        return self.__area
        self.calc_area()
print("Введите радиус окружности, для вычисления площади 6-угольника")
p=Polygon(int(input()))
print("Polygon area: ", p.area())
print("radius: ",p.r())

