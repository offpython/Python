# 양자택일 조건문(if~else문)
# 양자택일 조건문

passScore = 80

myScore = int(input('점수 입력 : '))

if myScore >= passScore:
    print('PASS!!')
else:
    print('FAIL!!');

# PASS (조건문에 대한 실행문이 정해지지 않았을 때)
if myScore >= passScore:
    pass
else:
    pass

# len()
print(len('가나다'))

# 실습1
seniorAge = 65

passengerAge = int(input('나이 입력 : '))
if passengerAge >= seniorAge:
    print('무료 대상 승객입니다.')
else:
    print('유료 대상 승객입니다.')

# 실습2
floatNum = float(input('소수 입력 : '))

if floatNum - int(floatNum) >= 0.5:
    print('올림 : {}'.format(int(floatNum) + 1))

else:
    print('내림 : {}'.format(int(floatNum)))