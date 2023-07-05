# class Parent:
#     def __init__(self) -> None:
#         self.value="테스트"
#         print("Parent클래스의 __init__호출")

#     def test(self):
#         print("Parent 클래스의 test호출")

# class Child(Parent):
#     def __init__(self) -> None:
#         super().__init__() #부모 클래스의 생성자 호출
#         print("Child클래스의 __init__호출")

# child = Child()
# child.test()
# print("부모의 value={}".format(child.value))

#자동차 클래스 상속
class Car:
    speed =0

    def upSpeed(self,value):
        self.speed = self.speed+value
        print("현재 속도(슈퍼클래스) : %d" %self.speed)
    
    def downSpeed(self,value):
        self.speed = self.speed-value

class SeDan(Car):
    seatNum=0

    def upSpeed(self,value):
        # '''
        # 오버라이딩
        # '''
        self.speed = self.speed+value
        if self.speed>150:
            self.speed=150
            print("현재 속도(자식클래스) : %d" %self.speed)


    def getSeatNum(self):
        return self.seatNum
    
class Truck(Car):
    capacity = 0

    def getCapacity(self):
        return self.capacity
    
sedan1,truck1=SeDan(),Truck()

sedan1.upSpeed(200)
# sedan1.downSpeed(20)
sedan1.seatNum=5

truck1.upSpeed(150)
truck1.capacity=100

print("승용차의 속도는 {}km, 좌석수는 {}개 입니다".format(sedan1.speed,sedan1.getSeatNum()))
print("트럭의 속도는 {}km, 좌석수는 {}개 입니다".format(truck1.speed,truck1.getCapacity()))