# 중첩함수
## 함수 안에 또 다른 함수가 있는 형태

def out_function():
    print('out_function called!')

    def in_function():
        print('in_function called!!')

    in_function() # 내부 함수를 함수 밖에서 호출할 수 없다.

out_function()

# 실습1
def calculator(n1, n2, operator):

    def addcal():
        print(f'덧셈 연산 : {n1 + n32}')

    def subcal():
        print(f'뺼셈 연산 : {n1 - n2}')

    def mulcal():
        print(f'곱셈 연산 : {n1 * n2}')

    def divcal():
        print(f'나눗셈 연산 : {n1 / n2}')

    if operator == 1:
        addcal()
    elif operator == 2:
        subcal()
    elif operator == 3:
        mulcal()
    elif operator == 4:
        divcal()

while True:
    num1 = float(input('실수 n1 입력 : '))
    num2 = float(input('실수 n2 입력 : '))
    operatorNum = int(input('1.덧셈 2.뺄셈 3.곱셈 4.나눗셈 5.종료 '))

    if operatorNum == 5:
        print('bye~')
        break

    calculator(num1, num2, operatorNum)