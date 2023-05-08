# if~else문과 조건식

# 조건식 결과에 따른 실행만 하는 경우
# 조건식 결과를 변수에 할당하는 경우
# 모든 조건식 > if ~ else 문으로 변경 가능
# if ~ else > 조건식으로 변경 가능한 건 아님

# 실습1
rainPercentage = int(input('비올 확률 입력 : '))
minRainPercentage = 55

print('우산을 챙기세요.') if rainPercentage >= minRainPercentage else print('양산을 챙기세요.')

if rainPercentage >= minRainPercentage:
    print('우산을 챙기세요.')
else:
    print('양산을 챙기세요.')

# 실습2
lowTemperature = int(input('최저 기온 입력 : '))
highTemperature = int(input('최고 기온 입력 : '))

difTemperature = highTemperature - lowTemperature
if difTemperature >= 11:
    print('일교차 : {}'.format(difTemperature))
    print('감기 조심하세요.')
else:
    print('일교차 : {}'.format(difTemperature))
    print('산책하기 좋은 날씨입니다.')