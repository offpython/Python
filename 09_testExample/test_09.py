# 연산자 04

# 실습1
baseTemp = 29
step = 60
stepTemp = 0.8

height = int(input('고도 입력 : '))

targetTemp = baseTemp - (height // step * stepTemp)

print('지면 온도 : 29')
print('고도 {}의 기온 : {}'.format(height, tagetTemp))

