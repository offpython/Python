# 함수 내에서 또 다른 함수 호출
def fun1():
    print('fun1 호출!')
    fun2()
    print('fun2 호출 후에 실행')
def fun2():
    print('fun2 호출!')
    fun3()
def fun3():
    print('fun3 호출!')

fun1()

# pass 사용
def printTodayWeather():
    print('오늘 날씨는 매우 좋아요.')
def printTomorrowWeather():
    pass

printTodayWeather()
printTomorrowWeather()

# 실습1
def guguDan2():
    for i in range(1, 10):
        print('2 * {} = {}'.format(i, 2 * i))
    guguDan3()
def guguDan3():
    for i in range(1, 10):
        print('3 * {} = {}'.format(i, 3 * i))
    guguDan4()

def guguDan4():
    for i in range(1, 10):
        print('4 * {} = {}'.format(i, 4 * i))
    guguDan5()
def guguDan5():
    for i in range(1, 10):
        print('5 * {} = {}'.format(i, 5 * i))

guguDan2()