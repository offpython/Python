# 추상클래스
## 상위 클래스에서 하위 클래스에 메서드 구현을 강요한다.

# 모듈 필요
from abc import ABCMeta
from abc import abstractmethod

class AirPlane(metaclass=ABCMeta): # 강제성 띄는 클래스에 모듈 붙혀줌

    @abstractmethod # 데코레이션 붙혀줌
    def flight(self):
        pass

    def foward(self):
        print('전진!!')

    def backward(self):
        print('후진!!')

class Airline(AirPlane):

    def __init__(self, c):
        self.color = c

    # 구현
    def flight(self):
        print('시속 400km/h 비행!!')

class ZetPlane(AirPlane):

    def __init__(self, c):
        self.color = c

    # 구현
    def flight(self):
        print('시속 700km/h 비행!! ')

al = Airline('red')
al.flight()
al.foward()
al.backward()

al = Airline('blue')
al.flight()
al.foward()
al.backward()

# 실습1
from abc import ABCMeta
from abc import abstractmethod

class Calculator(metaclass=ABCMeta):

    @abstractmethod
    def add(self, n1, n2):
        pass

    @abstractmethod
    def sub(self, n1, n2):
        pass

    @abstractmethod
    def mul(self, n1, n2):
        pass

    @abstractmethod
    def div(self, n1, n2):
        pass

class DeveloperCalculator(Calculator):

    def add(self, n1, n2):
        print(n1 + n2)

    def sub(self, n1, n2):
        print(n1 - n2)

    def mul(self, n1, n2):
        print(n1 * n2)

    def div(self, n1, n2):
        print(n1 / n2)

    def mod(self, n1, n2):
        print(n1 % n2)

    def flo(self, n1, n2):
        print(n1 // n2)

cal = DeveloperCalculator()
cal.add(10, 20)
cal.sub(10, 20)
cal.mul(10, 20)
cal.div(10, 20)
cal.mod(10, 20)
cal.flo(10, 20)