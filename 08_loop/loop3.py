# 반복 범위 설정(range()함수)
# for i in range(1, 11, 2): = 1부터 10까지 2씩 증가

# 실습
startNum = int(input('반복의 시작 입력 : '))
endNum = int(input('반복의 끝 입력 : '))

for i in range(startNum, endNum + 1):
    print(i)

for j in range(startNum, endNum + 1, 2):
    print(j)

