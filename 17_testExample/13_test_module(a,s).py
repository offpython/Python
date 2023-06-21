# 모듈(07)

## 패키지와 모듈을 만들고 연산 결과 출력


# 패키지
from arithmetic import basicOperation as bo
from arithmetic import developerOperation as do

from shape import triangleSqureArea as tsa
from shape import circleArea as ca

inputNumber1 = float(input('숫자1 입력 : '))
inputNumber2 = float(input('숫자2 입력 : '))


print(f'{inputNumber1} + {inputNumber2} = {bo.add(inputNumber1, inputNumber2)}')
print(f'{inputNumber1} - {inputNumber2} = {bo.sub(inputNumber1, inputNumber2)}')
print(f'{inputNumber1} * {inputNumber2} = {bo.mul(inputNumber1, inputNumber2)}')
print(f'{inputNumber1} / {inputNumber2} = {bo.div(inputNumber1, inputNumber2)}')

print(f'{inputNumber1} + {inputNumber2} = {do.mod(inputNumber1, inputNumber2)}')
print(f'{inputNumber1} + {inputNumber2} = {do.flo(inputNumber1, inputNumber2)}')
print(f'{inputNumber1} + {inputNumber2} = {do.exp(inputNumber1, inputNumber2)}')

inputWidth = float(input('가로 길이 입력 : '))
inputHeight = float(input('세로 길이 입력 : '))

print(f'삼각형 넓이 : {tsa.calTriangleArea(inputWidth, inputHeight)}')
print(f'사각형 넓이 : {tsa.calSqureArea(inputWidth, inputHeight)}')

inputRadius = float(input('반지름 입력 : '))

print(f'원 넓이 : {ca.calCircleArea(inputRadius)}')


