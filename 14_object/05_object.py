# 클래스 상속

class NormalCar:

    def drive(self):
        print('[NormalCar] drive() called!!')

    def back(self):
        print('[NormalCar] back() called!!')

# NormalCar 클래스 상속
class TurboCar(NormalCar):

    def turbo(self):
        print('[TurboCar] turbo() called!!')

myTurboCar = TurboCar()

myTurboCar.turbo()
myTurboCar.drive()
myTurboCar.back()

# 실습1

class CalculatorSuper:

    def add(self, n1, n2):
        return n1 + n2

    def sub(self, n1, n2):
        return n1 - n2

# 클래스 상속
class CalculatorChild(CalculatorSuper):

    def mul(self, n1, n2):
        return n1 * n2

    def div(self, n1, n2):
        return n1 / n2

myCal = CalculatorChild()

print(myCal.add(10, 20))
print(myCal.sub(10, 20))
print(myCal.mul(10, 20))
print(myCal.div(10, 20))


