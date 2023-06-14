# try ~ except ~ else
# 예외가 발생하지 않은 경우에 실행하는 구문

nums = []
n = 1
while n < 6:

    try:
        num = int(input('input number : '))

    except:
        print('예외 발생')
        continue

    else:
        if num % 2 == 0:
            nums.append(num)
            n += 1

        else:
            print('입력한 숫자는 홀수 입니다.', end='')
            print('다시 입력하세요.')
            continue

print(f'nums : {nums}')

# 실습1
## 사용자로부터 숫자 5개를 받아 짝수/홀수/실수로 구분해서 각각을 리스트에 저장하는 프로그램

eveList = []; oddList = []; floatList = []

n = 1
while n < 6:

    try:
        num = float(input('input number : '))

    except:
        print('exception raised!')
        print('input number again')
        continue

    else:
        if num - int(num) != 0:
            print('float number!')
            floatList.append(num)

        else:
            if num % 2 == 0:
                print('even number!')
                eveList.append(int(num))

            else:
                print('odd number!')
                oddList.append(int(num))

        n += 1

print(f'even list : {eveList}')
print(f'odd list : {oddList}')
print(f'float list : {floatList}')