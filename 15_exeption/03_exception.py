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