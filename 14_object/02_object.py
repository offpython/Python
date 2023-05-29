# 객체 속성 변경

class NewGenerationPC:

    def __init__(self, name, cpu, memory, ssd):
        self.name = name
        self.cpu = cpu
        self.memory = memory
        self.ssd = ssd

    def doExcel(self):
        print('EXCEL RUN!!')

    def doPhotoshop(self):
        print('PHOTOSHOP RUN!!')

    def printPCInfo(self):
        print(f'self.name : {self.name}')
        print(f'self.cpu : {self.cpu}')
        print(f'self.memory : {self.memory}')
        print(f'self.ssd : {self.ssd}')

myPc = NewGenerationPC('myPc', 'i5', '16G', '256G')
myPc.printPCInfo()

freindPc = NewGenerationPC('friendPc', 'i7', '32G', '512G')
freindPc.printPCInfo()

myPc.cpu = 'i9'
myPc.memory = '64G'
myPc.ssd = '1t'
myPc.printPCInfo()

# 실습1
class Calculator:

    def __init__(self, num1, num2):
        self.number1 = num1
        self.number2 = num2

    def add(self):
        result = self.number1 + self.number2
        return result

    def sub(self):
        result = self.number1 - self.number2
        return result

    def mul(self):
        result = self.number1 * self.number2
        return result

    def div(self):
        result = self.number1 / self.number2
        return result

newCarculator = Calculator(10, 20)
print(f'newCarculator.add() : {newCarculator.add()}')
print(f'newCarculator.sub() : {newCarculator.sub()}')
print(f'newCarculator.mul() : {newCarculator.mul()}')
print(f'newCarculator.div() : {newCarculator.div()}')
