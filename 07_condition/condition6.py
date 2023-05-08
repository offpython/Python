# 중첩 조건문
# 조건문 안에 또 다른 조건문이 있을 수 있음

exampleScore = int(input('시험 점수 입력 : '))

if exampleScore < 60:
    print('재시험 대상입니다.')
else:
    if exampleScore >= 90:
        print('A')
    elif exampleScore >= 80:
        print('B')
    elif exampleScore >= 70:
        print('C')
    elif exampleScore >= 60:
        print('D')


# 실습1
selectNum = int(input('출퇴근 대상인가? 1.Yes \t 2.No \t 입력 : '))

if selectNum == 1:
    print('교통 수단을 선택하세요.')
    trans = int(input('1.도보, 자전거 \t 2.버스, 지하철 \t 3. 자가용 \t 입력 : '))
    if trans == 1:
        print('세금 감면 5%')
    elif trans == 2:
        print('세금 감면 3%')
    elif trans == 3:
        print('추가 세금 1%')

elif selectNum == 2:
    print('세금 변동 없음')
else:
    print('잘못 입력했습니다.')

