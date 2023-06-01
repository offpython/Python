# 오버라이딩
## 하위 클래스에서 상위 클래스의 메서드를 재정의한다.

class Robot:

    def __init__(self, c, h, w):
        self.color = c
        self.height = h
        self.weight = w

    def fire(self):
        print('미사일 발사!!')

    def printRobotInfo(self):
        print(f'self. color = {self.color}')
        print(f'self. height = {self.height}')
        print(f'self. weight = {self.weight}')

class NewRobot(Robot):

    def __init__(self, c, h, w):
        super().__init__(c, h, w)

    # 오버라이딩 (미사일 -> 레이저발사)
    def fire(self):
        print('레이저 발사!!')

myRobot = NewRobot('red', 200, 300)
myRobot.printRobotInfo()
myRobot.fire()

# 실습1_오버라이딩 (기존 -> 기존 + 단위)
class TriangleArea:

    def __init__(self, w, h):
        self.width = w
        self.height = h

    def printTriangleInfo(self):
        print(f'width : {self.width}')
        print(f'heigth : {self.height}')

    def getArea(self):
        return self.width * self.height / 2

class NewTriangleArea(TriangleArea):
    def __init__(self, w, h):
        super().__init__(w, h)

    def getArea(self):
        return str(super().getArea()) + '㎠'

ta = NewTriangleArea(7, 5)
ta.printTriangleInfo()
ta.getArea()
triangleArea = ta.getArea()
print(f'Triangle Area : {triangleArea}')



