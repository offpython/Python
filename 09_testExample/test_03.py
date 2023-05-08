# 데이터와 변수 사용법_02

pi = 3.14
radius = float(input('반지름(cm)입력: '))

circleArea = pi * radius * radius
circleLength = 2 * pi * radius

print('원의 넓이\t : %d' % circleArea)
print('원의 둘레길이\t : %d' % circleLength)

print('원의 넓이\t : %.1f' % circleArea)
print('원의 둘레길이\t : %.1f' % circleLength)

print('원의 넓이\t : %.3f' % circleArea)
print('원의 둘레길이\t : %.3f' % circleLength)

# 데이터와 변수 사용법_03
# str[0] : str에 저장된 문자열에서 첫 번째 문자를 반환

name = input('이름 입력 : ')
mail = input('메일 입력 : ')
id = input('아이디 입력 : ')
pw = input('비밀번호 입력 : ')
privateNumber1 = input('주민번호 앞자리 입력 : ')
privateNumber2 = input('주민번호 뒷자리 입력 : ')
address = input('주소 입력 : ')

print('-' * 30)
print(f'이름 : {name}')
print(f'메일 : {mail}')
print(f'아이디 : {id}')
pwStar = '*' * len(pw)
print(f'비밀번호 : {pwStar}')
privateNumberStar = privateNumber2[0] + ('*' * 6)
print(f'주민번호 : {privateNumber1} - {privateNumberStar}')
print(f'주소 : {address}')
print('-' * 30)


