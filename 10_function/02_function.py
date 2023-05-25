# 함수 선언
def addCal():
    n1 = int(input('n1 입력 : '))
    n2 = int(input('n2 입력 : '))
    print(f'n1 + n2 = {n1 + n2}')
# 함수 호출
addCal()

# 실습1
def printWeatherInfo():
    print('오늘 날씨는 맑습니다. 기온은 25도 입니다.')

printWeatherInfo()
printWeatherInfo()
printWeatherInfo()

# 실습2
def calFun():
    n3 = int(input('n3 입력 : '))
    n4 = int(input('n4 입력 : '))

    print(f'n3 * n4 = {n3 * n4}')
    print(f'n3 / n4 = {round(n3 / n4, 2)}')

calFun()

