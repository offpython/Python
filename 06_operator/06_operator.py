# 비교연산자(숫자비교)

num1 = 10
num2 = 5

result = num1 > num2
print('num1 > num2 : {}'.format(result))

result = num1 >= num2
print('num1 > num2 : {}'.format(result))

result = num1 < num2
print('num1 > num2 : {}'.format(result))

result = num1 <= num2
print('num1 > num2 : {}'.format(result))

result = num1 == num2
print('num1 > num2 : {}'.format(result))

result = num1 != num2
print('num1 > num2 : {}'.format(result))

# 실습 1
userInputNumber1 = int(input('첫 번째 숫자 입력 : '))
userInputNumber2 = int(input('두 번째 숫자 입력 : '))

print('{} > {} : {}'.format(userInputNumber1, userInputNumber2, (userInputNumber1 > userInputNumber2)))
print('{} >= {} : {}'.format(userInputNumber1, userInputNumber2, (userInputNumber1 >= userInputNumber2)))
print('{} < {} : {}'.format(userInputNumber1, userInputNumber2, (userInputNumber1 < userInputNumber2)))
print('{} <= {} : {}'.format(userInputNumber1, userInputNumber2, (userInputNumber1 <= userInputNumber2)))
print('{} == {} : {}'.format(userInputNumber1, userInputNumber2, (userInputNumber1 == userInputNumber2)))
print('{} != {} : {}'.format(userInputNumber1, userInputNumber2, (userInputNumber1 != userInputNumber2)))

# 실습2

maxLength = 5200
maxWidth = 1985

myCarLength = int(input('정장 길이 입력: '))
myCarWidth = int(input('전폭 길이 입력: '))

print('전장 가능 여부 : {}'.format(maxLength >= myCarLength))
print('전폭 가능 여부 : {}'.format(maxWidth >= myCarWidth))