# 연산자 04

# 실습1
baseTemp = 29
step = 60
stepTemp = 0.8

height = int(input('고도 입력 : '))

targetTemp = baseTemp - ((height // step) * 0.8)

if height % step != 0:
    targetTemp -= stepTemp

print('지면 온도 : {}도'.format(baseTemp))
print('고도 %dm의 기온 : %.2f도' % (height, targetTemp))

# 실습2
bread = 197
milk = 152
studentCnt = 17

print('학생 한명이 갖게 되는 빵 개수 : {}'.format(bread // studentCnt))
print('학생 한명이 갖게 되는 우유 개수 : {}'.format(milk // studentCnt))

print('남는 빵 개수 : {}'.format(bread % studentCnt))
print('남는 우유 개수 : {}'.format(milk % studentCnt))

