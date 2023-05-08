# 조건식(if문)

if 10 > 5 :
    print('10은 5보다 크다.')
    print('또 다른 실행문!!!')

print('조건문이 끝났어요.')

num1 = 10
num2 = 20

if num1 == num2:
    print('num1 <= num2')

# 실습 1
korScore = int(input('국어 점수 입력 : '))
engScore = int(input('영어 점수 입력 : '))
matScore = int(input('수학 점수 입력 : '))

avgScore = (korScore + engScore + matScore) / 3
print('평균 : {}'.format(avgScore))

if avgScore >= 90:
    print('참 잘했어요!')

# 실습 2
highTemperature = 28
lowTemperature = 20

innerTemperature = int(input('실내 온도 : '))

if innerTemperature >= highTemperature:
    print('냉방 작동!')

if innerTemperature < lowTemperature:
    print('난방 작동!')