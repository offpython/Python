# 산술연산자(거듭제곱)

num1 = 2
num2 = 3

result0 = num1 ** num2
print('result0 : {}'. format(result0))

# n의 m제곱근의 공식 = n**(1/m)
# 2의 제곱근 구하기
result = 2 ** (1/2)
print('reuslt : %.2f' % result)
# 2의 3제곱근 구하기
result = 2 ** (1/3)
print('reuslt : %.2f' % result)
# 2의 4제곱근 구하기
result = 2 ** (1/4)
print('reuslt : %.2f' % result)

# sqrt()함수를 이용한 제곱근 구하기, 2제곱근만 구함
import math
print(math.sqrt(5))

# pow()함수를 이용한 거듭제곱 구하기
print(math.pow(5, 8))

# 실습
firstMonthMoney = 200
after12Month = ((firstMonthMoney * 0.01) ** 12) * 100

print('12개월 후 용돈 : {}'.format(after12Month))

after12Month = int(after12Month)
strResult = format(after12Month, ',')
print(strResult, '원')