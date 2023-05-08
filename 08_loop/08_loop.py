# 반복문 제어(break)
# 반복 실행 중 break를 만나면 반복문을 빠져나온다.

num = 0
while True:
    print('Hello')

    num += 1
    if num >= 5:
        break

print('The END')

sum = 0
searchNum = 0
for i in range(1, 101):
    sum += i

    if sum > 100:
        searchNum = i
        break

print('searchNum : {}'.format(searchNum))

# 실습1
result = 1
num = 0
for j in range(1, 11):
    result *= j

    if result > 50:
        num = j
        break

print('num : {} \t result : {}'.format(num, result))

# 실습2
limitWeight = 2200
currentWeight = 800
date1 = 1

while True:
    if currentWeight >= 2200:
        break

    date1 += 1
    currentWeight += 70

print('이유식 중단 날짜 : {}'.format(date1))

