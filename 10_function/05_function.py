# 데이터 반환

# return 키워드를 이용하면 함수 실행 결과를 호출부로 반환할 수 있다.
def calculator(n1, n2):
    result = n1 + n2

    return result

returnValue = calculator(10, 20)

print(f'returnValue = {returnValue}')

# 함수가 return을 만나면 실행을 종료한다.
def divideNumber(n):

    if n % 2 == 0:
        return '짝수'
    else:
        return '홀수'

    print('Hello') #return 이후 실행이라 프린트 안됨

returnValue2 = divideNumber(5)
print(f'returnValue2 : {returnValue2}')

# 실습1
def cmToMm(cm):
    result = cm * 10

    return result

length = float(input('길이(cm)입력 : '))
returnValue3 = cmToMm(length)
print(f'returnValue3 : {returnValue3}')

# 실습2
import random

def getOddRandomNumber():

    while True:
        rNum = random.randint(1, 100)
        if rNum % 2 != 0:
            break
        return rNum

print(f'returnValue : {getOddRandomNumber()}')




