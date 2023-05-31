# 객체지향 프로그래밍

## 클래스 만들기
class Car:

    def __init__(self, col, len):
        self.color = col
        self.length = len

    def doStop(self):
        print('STOP!!')

    def doStart(self):
        print('START!!')

    def printCarInfo(self):
        print(f'self.color : {self.color}')
        print(f'self.length : {self.length}')

## 객체 생성
### 객체는 클래스의 생성자를 호출한다.
car1 = Car('red', 200)
car2 = Car('blue', 300)

car1.printCarInfo()
car2.printCarInfo()

car1.doStop()
car1.doStart()

# 실습1
class Plane:

    def __init__(self, col, len, wgt):
        self.color = col
        self.length = len
        self.weight = wgt

    def departure(self):
        print('DEPARTURE')

    def arrival(selfs):
        print('ARRIVAL')

    def printPlaneInfo(self):
        print(f'self.color : {self.color}')
        print(f'self.length : {self.length}')
        print(f'self.weight : {self.weight}')

plane1 = Plane('red', 100, 2000)
plane2 = Plane('blue', 200, 3000)
plane3 = Plane('yellow', 300, 4000)

plane1.departure()
plane2.printPlaneInfo()
plane3.arrival()





