# 함수(4)
## 1. 재귀함수를 이용해서 팩토리얼 함수 만들기

def fomatedNumber(n):
    return format(n, ',')

def recursionFun(n):

    if n == 1:
        return n

    return n * (recursionFun(n-1))

inputNumber = int(input('Input Number : '))
print(fomatedNumber(recursionFun(inputNumber)))

## 2, 단리/월복리 계산기 함수 만들기

def fomatedNumber(n):
    return format(n, ',')

#단리
def singleRateCalculator(m, t, r):

    totalMoney = 0
    totalRateMoney = 0

    for i in range(t):
        totalRateMoney = totalRateMoney + m * (r * 0.01)

    totalMoney = m + totalRateMoney
    return int(totalMoney)

#월복리
def multiRateCalculator(m, t, r):

    t = t * 12
    rpm = (r / 12) * 0.01

    totalMoney = m

    for i in range(t):
        totalMoney = totalMoney + (totalMoney * rpm)

    return int(totalMoney)

money = int(input('예치금(원) : '))
term = int(input('기간(년) : '))
rate = int(input('연 이율(%) : '))

print(' ' * 30)
print('[단리 계산기]')
print('=' * 30)
print(f'예치금 : {fomatedNumber(money)}원')
print(f'예치기간 : {term}년')
print(f'연 이율 : {rate}%')
print('-' * 30)
print(f'{term}년 후 총 수령액: {fomatedNumber(singleRateCalculator(money, term, rate))}원')
print('=' * 30)
print(' ' * 30)
print('[월복리 계산기]')
print('=' * 30)
print(f'예치금 : {fomatedNumber(money)}원')
print(f'예치기간 : {term}년')
print(f'연 이율 : {rate}%')
print('-' * 30)
print(f'{term}년 후 총 수령액: {fomatedNumber(multiRateCalculator(money, term, rate))}원')
print('=' * 30)