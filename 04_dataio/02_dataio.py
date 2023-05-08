# 데이터 출력

userName = 'hong gil dong'
print(userName)

userAge = 20
print(userAge)

# 콤마를 이용한 자동 데이터 출력
print('User name : ', userName)
print('User age : ', userAge)
print('User name : ', userName, ', User age : ', userAge)

# 연속 데이터 막기 (=\n)
print('3 * 5 = ', end='')
print(3 * 5)

# 포맷 문자열 데이터 출력
print(f'User name : {userName}')
print(f'User age : {userAge}')

print(f'User name : {userName}, User age : {userAge}')

# 특수문자 (\n = 개행, \t = 탭)
print(f'User name : {userName} \nUser age : {userAge}')
print(f'User name :\t {userName} \nUser age : \t{userAge}')

# 실습
width = float(input('가로 길이 : '))
height = float(input('세로 길이 : '))

triangle = width * height / 2
print('width : ', width, end='')
print(', height : ', height, end='')
print(', triangle : ', triangle, end='')

print(f'width : {width}, height : {height}, triangle : {triangle}')
