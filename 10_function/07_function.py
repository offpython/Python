# 전역변수와 지역변수

# 전역변수
## 함수 밖에 선언된 변수로, 어디에서나 사용은 가능하지만 함수 안에서 수정할 수 없다.
num_out = 10
def printNumbers():
    num_out = 20  #지역변수
    print(f'num_out : {num_out}')

printNumbers()
print(f'num_out : {num_out}')

# 지역변수
## 함수 안에서 선언된 변수로, 함수 안에서만 사용 가능하다.
def printNumbers():
    num_in = 20
    print(f'num_in : {num_in}')

 #print(f'num_in : {num_in}') #불가

# global 키워드
## global을 사용하면 함수 안에서도 전역변수의 값을 수정할 수 있다.
num_out = 10
def printNumbers():
    global num_out
    num_out = 20
    print(f'num_out : {num_out}')

printNumbers()
print(f'num_out : {num_out}')

