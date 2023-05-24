# 함수란?
def addFun(x, y):
    return x + y

print(addFun(100, 50))

# 내장함수(파이썬 기본제공), 사용자함수(직접 선언)

# 함수는 특정 기능을 재사용하기 위해 사용
# ex) 덧셈 연산 5회 실행
def addCal():
    n1 = int(input('n1 입력 : '))
    n2 = int(input('n2 입력 : '))
    print(f'n1 + n2 = {n1 + n2}')