# 반복문

#구구단
print('{} * {} = {}'.format(2, 1,(2 * 1)))
print('{} * {} = {}'.format(2, 2,(2 * 2)))
print('{} * {} = {}'.format(2, 3,(2 * 3)))
print('{} * {} = {}'.format(2, 4,(2 * 4)))
print('{} * {} = {}'.format(2, 5,(2 * 5)))
print('{} * {} = {}'.format(2, 6,(2 * 6)))
print('{} * {} = {}'.format(2, 7,(2 * 7)))
print('{} * {} = {}'.format(2, 8,(2 * 8)))
print('{} * {} = {}'.format(2, 9,(2 * 9)))

for i in range(1, 10):
    print('{} * {} = {}'.format(3, i, (3 * i)))

# 메일 발송
print('{}선수에게 메일 발송!'.format('박찬호'))
print('{}선수에게 메일 발송'.format('박세리'))
print('{}선수에게 메일 발송'.format('박지성'))
print('{}선수에게 메일 발송'.format('김연경'))
print('{}선수에게 메일 발송'.format('이승엽'))

players = ['박찬호', '박세리', '박지성', '김연경', '이승엽']
for players in players:
    print('{}선수에게 메일 발송'.format(players))

# 횟수에 의한 반복
for i in range(100):
    print('i > {}'.format(i))

# 조건에 의한 반속
num = 0
while (num < 10):
    print('num > {}'.format(num))
    num += 1
