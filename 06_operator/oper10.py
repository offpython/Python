# 조건식

num1 = 10
num2 = 10

numResult = True if num1 > num2 else False
print('num1 > num2 : {}'.format(numResult))

print ('num1은 num2보다 크다.') if numResult else ('num1은 num2보다 크지 않다.')

# 실습1
listSnowAmount = 30
snowAmount = int(input('적설량 입력(mm): '))

print('적설량 : {}mm, {}'.format(snowAmount, '대설 경보 발령 !!')) if snowAmount >= listSnowAmount else \
    print('적설량 : {}mm, {}'.format(snowAmount, '대설 경보 해제 !!'))

# 실습2
#import operator
passScore1 = 60
passScore2 = 70

korScore = int(input('국어 점수 : '))
engScore = int(input('영어 점수 : '))
matScore = int(input('수학 점수 : '))

totalScore = korScore + engScore + matScore
avgScore = totalScore / 3

print('국어 : PASS') if korScore >= passScore1 else print('국어 : FAIL')
print('영어 : PASS') if engScore >= passScore1 else print('영어 : FAIL')
print('수학 : PASS') if matScore >= passScore1 else print('수학 : FAIL')
print('시험 : PASS') if avgScore >= passScore2 else print('시험 : FAIL')

print('총점 : {}, 평균 : {}'.format(totalScore, avgScore))
