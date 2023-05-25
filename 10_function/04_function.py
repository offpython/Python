# 인수와 매개변수

def greet(customer):
    print('{} 고객님, 안녕하세요.'.format(customer))

greet('홍길동')
greet('박찬호')

# 인수와 매개변수 개수 일치
def greet(customer1, customer2):
    print('{}, {} 고객님. 안녕하세요.'.format(customer1, customer2))

greet('홍길동', '박찬호')

def calculator(n1, n2):
    print(f'{n1} + {n2} = {n1 + n2}')
    print(f'{n1} + {n2} = {n1 - n2}')
    print(f'{n1} + {n2} = {n1 * n2}')
    print(f'{n1} + {n2} = {n1 / n2}')

calculator(10, 20)

# 매개변수가 정해지지 않은 경우 '*' 이용
def printNumber(*numbers):
    for number in numbers:
        print(numbers, end="")
    print()

printNumber()
printNumber(10)
printNumber(10, 20)
printNumber(10, 20, 30)

# 실습1
korScore = int(input('국어 점수 입력 : '))
engScore = int(input('영어 점수 입력 : '))
matScore = int(input('수학 점수 입력 : '))

def printScore(kor, eng, mat):
    sum = kor + eng + mat
    avg = sum / 3

    print(f'총점 : {sum}')
    print(f'평균 : {round(avg, 2)}')

printScore(korScore, engScore, matScore)