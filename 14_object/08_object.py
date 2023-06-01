# 다중 상속
## 단, 다중 상속 남발 시 비슷한 클래스명으로 인해 혼동할 수 있음

class Car01:
    def drive(self):
        print('drive() method called!!')

class Car02:
    def turbo(self):
        print('turbo() method called!!')

class Car03:
    def fly(self):
        print('fly() method called!!')

class Car(Car01, Car02, Car03):
    def __init__(self):
        pass

myCar = Car()

myCar.drive()
myCar.turbo()
myCar.fly()

# 실습1
class BasicCalculator:

    def add(self, n1, n2):
        return n1 + n2

    def sub(self, n1, n2):
        return n1 - n2

    def mul(self, n1, n2):
        return n1 * n2

    def div(self, n1, n2):
        return n1 / n2

class DeveloperCalculator:

    def mod(self, n1, n2):
        return n1 % n2

    def flo(self, n1, n2):
        return n1 // n2

    def exp(self, n1, n2):
        return n1 ** n2

class NewCalculator(BasicCalculator, DeveloperCalculator):

    def __init__(self):
        pass

cal = NewCalculator()
cal.add(10, 20)
print(f'cal.add(10, 20) : {cal.add(10, 20)}')
print(f'cal.sub(10, 20) : {cal.sub(10, 20)}')
print(f'cal.mul(10, 20) : {cal.mul(10, 20)}')
print(f'cal.div(10, 20) : {cal.div(10, 20)}')
print(f'cal.mod(10, 20) : {cal.mod(10, 20)}')
print(f'cal.flo(10, 20) : {cal.flo(10, 20)}')
print(f'cal.exp(2, 5) : {cal.exp(2, 5)}')



