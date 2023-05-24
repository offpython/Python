# 반복문 04

# 실습1
busA = 15
busB = 13
busC = 8

totalMin = 60 * 17
for i in range(totalMin + 1):
    if i < 20 or i > (totalMin - 60): # a, b만 운행하는 경우
        if i % busA == 0 and i % busB == 0:
            print('busA와 busB 동시 정차!!', end='')
            hour = 6 + (i // 60)
            min = i % 60
            print('\t{}:{}'.format(hour, min))
    else:  # a, b, c 모두 운행하는 경우
        if i % busA == 0 and i % busB == 0:
            print('busA와 busB 동시 정차!!', end='')
            hour = 6 + (i // 60)
            min = i % 60
            print('\t{}:{}'.format(hour, min))
        elif i % busB == 0 and i % busC == 0:
            print('busB와 busC 동시 정차!!', end='')
            hour = 6 + (i // 60)
            min = i % 60
            print('\t{}:{}'.format(hour, min))
        elif i % busC == 0 and i % busA == 0:
            print('busC와 busA 동시 정차!!', end='')
            hour = 6 + (i // 60)
            min = i % 60
            print('\t{}:{}'.format(hour, min))