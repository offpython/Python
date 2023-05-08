# 무한루프

n = 1
while n < 10:
    print('Hello')
    n += 1

flag = True
num = 0
sum = 0

while flag:
    num += 1
    sum += num
    print('{}까지의 합 : {}'.format(num, sum))

    if sum >= 1000:
        flag = False

# 실습
import random

sum1 = 0
data = 0
flag = True

while flag:
    patientCount = random.randint(50, 100)
    sum1 += patientCount
    data += 1
    print('날짜 : {}, \t 오늘 환자수 : {}, \t 누적환자수 : {}'.format(data, patientCount, sum1))

    if sum1 >= 10000:
        flag = False

    pass