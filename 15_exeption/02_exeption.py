# 예외처리
## 발생된 예외를 별도 처리함으로써 프로그램 전체의 실행에 문제가 없도록 함

### 예외 발생 예상 구문을 try ~ except로 감싼다
n1 = 10; n2 = 0

try:
    print(n1 / n2)
except:
    print('예상치 못한 문제가 발생했습니다.')
    print('다음 프로그램은 정상 실행됩니다.')

print(n1 * n2)
print(n1 - n2)
print(n1 + n2)

# 실습1
## 사용자로부터 숫자 5개를 입력받을 때, 숫자가 아닌 자료형이 입력하면 예외처리하는 프로그램 
nums = []

n = 1
while n < 6:

    try:
        num = int(input('input number : '))
    except:
        print('예외 발생!!')
        continue

    nums.append(num)
    n += 1

print(f'nums : {nums}')
