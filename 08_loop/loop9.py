# 중첩반복문
# 반복문 안에 또 다른 반복문 선언

for i in range(1, 10):
    for j in range(i):
        print('*', end='')
    print()

for i2 in range(10, 0, -1):
    for j2 in range(i2):
        print('*', end='')
    print()

# 실습

for i3 in range(1, 10):
    for j3 in range(2, 10):
        result = j3 * i3
        print('{} * {} = {}\t'.format(j3, i3, result), end='')
