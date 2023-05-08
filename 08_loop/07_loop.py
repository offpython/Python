# 반복문 제어(continue)
# 실행 중단하고 다음 반복 실행문으로 넘어감

for i in range(100):
    if i % 7 != 0:
        continue
    print('{}는 7의 배수입니다.'.format(i))

# else 키워드
# 반복문이 종료된 후 실행

cnt = 0
for i in range(1, 100):
    if i % 7 != 0:
        continue
    print('{}는 7의 배수입니다.'.format(i))
    cnt += 1

else:
    print('99까지의 정수 중 7의 배수는 {}개입니다.'.format(cnt))

# 실습
minNum = 0

for j in range(1, 101):
    if j % 3 != 0 or j % 7 != 0:
        continue

    print('공배수 : {}'.format(j))

    if minNum == 0:
        minNum = j

else:
    print('최소공배수 : {}'.format(minNum))