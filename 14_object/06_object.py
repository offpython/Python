# # 생성자_01

# 초기화 방법 1
class Calculator:

    def __init__(self, n1, n2):
        print('[Calculator] __init__() called!!')
        self.num1 = n1
        self.num2 = n2


# 생성자 호출
cal = Calculator(10, 20)
print(f'cal.num1 : {cal.num1}')
print(f'cal.num2 : {cal.num2}')

# 초기화 방법 2
class Calculator:

    def __init__(self, n1, n2):
        print('[Calculator] __init__() called!!')
        # 객체가 항상 10, 100으로 초기화
        self.num1 = 10
        self.num2 = 100

# 생성자 호출
cal = Calculator(10, 20)
print(f'cal.num1 : {cal.num1}')
print(f'cal.num2 : {cal.num2}')

# 초기화 방법 3
class Calculator:

    def __init__(self, n):
        print('[Calculator] __init__() called!!')
        # 객체가 항상 10, 100으로 초기화
        self.num1 = n
        self.num2 = 400

# 생성자 호출
cal = Calculator(5)
print(f'cal.num1 : {cal.num1}')
# print(f'cal.num2 : {cal.num2}')

# 상위 클래스 초기화 하는 방법 1
class P_Class:

    def __init__(self, pNum1, pNum2):
        print('[P_Class] __init__() called!!')
        self.pNum1 = pNum1
        self.pNum2 = pNum2

class C_Class(P_Class):

    def __init__(self, cNum1, cNum2):
        print('[C_Class] __init__() called!!')

        # 상속 클래스 init메소드 강제 호출
        P_Class.__init__(self, cNum1, cNum2)

        self.cNum1 = cNum1
        self.cNum2 = cNum2

cls = C_Class(10, 20)

# 상위 클래스 초기화 하는 방법 2 (super()사용)
class P_Class:

    def __init__(self, pNum1, pNum2):
        print('[P_Class] __init__() called!!')
        self.pNum1 = pNum1
        self.pNum2 = pNum2

class C_Class(P_Class):

    def __init__(self, cNum1, cNum2):
        print('[C_Class] __init__() called!!')

        # super() 사용
        super().__init__(cNum1, cNum2)

        self.cNum1 = cNum1
        self.cNum2 = cNum2

cls = C_Class(10, 20)
