# 산술 연산자(덧셈, 뺄셈)

# 덧셈
# 실수 + 실수
num1 = 3.14
num2 = 0.12

print('num1 + num2 = %.2f' %(num1 + num2))

# 문자
str1 = 'Good'
str2 = ' '
str3 = 'morning'

print(str1 + str2 + str3)


# 숫자 + 문자 = 불가
print(str1 + num1)

# 실습_덧셈
korScore = int(input('국어 점수 : '))
engScore = int(input('영어 점수 : '))
matScore = int(input('수학 점수 : '))

total = (korScore + engScore + matScore)

print('국어 점수 : {}'.format(korScore))
print('영어 점수 : {}'.format(engScore))
print('수학 점수 : {}'.format(matScore))
print('합계 : {}'.format(total))

# 뺼셈
partTimeMoney = int(input('알바비 : '))
cardMoney = int(input('카드값 : '))

result = partTimeMoney - cardMoney
print('알바비 : {}'.format(partTimeMoney))
print('카드값 : {}'.format(cardMoney))
print('남는돈 : {}'.format(result))