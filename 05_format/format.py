# format()함수와 형식문자

userName = 'Hong gil dong'
userAge = 21

print(userName)
print(userAge)

print('User name : {}'.format(userName))
print('User age : {}'.format(userAge))

# 순서 바꾸기
print('User name : {1}, User age : {0}'. format(userName, userAge))

print('나의 이름은 {0}이고, 나이는 {1}살 입니다. 이름 {0}은 아버지께서 지어주셨습니다.'
      . format(userName, userAge))

# 형식 문자를 이용한 데이터 출력
# %s = 문자열, %d = 정수, %f = 실수

print('User name : %s' % userName)
print('User age : %d' % userAge)

print('User name : %s, User age : %d' %(userName, userAge))

pi = 3.14

print('pi : %f' % pi)
print('pi : %d' % pi)

# 소숫점 자릿수 정하기
print('pi : %f' % pi)
print('pi : %.1f' % pi)
print('pi : %.2f' % pi)

# 실습

radius = float(input('반지름 입력 : '))
pi = float(input('원주율 입력 : '))
print('radius : %.1f' % radius)
print('pi : %f' % pi)
print('radius : %.1f, pi : %f' % (radius, pi))
print('radius : %.6f, pi : %f' % (radius, pi))
print('radius : %.2f, pi : %.2f' % (radius, pi))

circleArea = radius * radius * pi
print('circleArea = %f' % circleArea)