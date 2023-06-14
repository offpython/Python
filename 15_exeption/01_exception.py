# 예외
## 문법적인 문제는 없으나, 실행 중 발생하는 예상하지 못한 문제이다.

# ZeroDivisionError: division by zero (입력값 10, 0)
def add(n1, n2):
    print(n1 + n2)

def div(n1, n2):
    print(n1 / n2)

firstNum = int(input('first number : '))
secondNum = int(input('second number : '))

add(firstNum, secondNum)
div(firstNum, secondNum)

# print(10/0)도 마찬가지

# ValueError: invalid literal for int() with base 10: 'Hello'
print(int('Hello'))

# IndexError: list index out of range
list = [1, 2, 3, 4, 5, 6]
print(list[6])



