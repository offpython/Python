# 산술 연산자(곱셈, 나눗셈)

# 문자(열) 곱셈
str = 'Hi '
result = str * 5

print('result : {}'.format(result))

# 숫자(정수,실수) 나눗셈
num1 = 10
num2 = 30

result = num1 / num2

print('result : {}'.format(result))
print('result : %.2f' % result)

# 0을 나눗셈 하는 경우 = 결과 항상 0
num0 = 0

result0 = num0 / num1
print('result0 : {}'.format(result0))

# # 0으로 나누는 경우 = 나눌 수 없음
# result00 = num1 / num0
# print('result0 : {}'.format(result0))

# 나눗셈 결과는 항상 float
result = int(num2 / num1)

print('result : {}'.format(result))
print('type of result : {}'.format(type(result)))

# 실습
korScore = int(input('국어 점수 : '))
engScore = int(input('영어 점수 : '))
matScore = int(input('수학 점수 : '))

totalScore = korScore + engScore + matScore
avgScore = totalScore / 3

print('국어 점수 : {}'. format(korScore))
print('영어 점수 : {}'. format(engScore))
print('수학 점수 : {}'. format(matScore))
print('합계 : {}'. format(totalScore))
print('평균 : %.2f' % avgScore)
