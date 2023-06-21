# 함수(6)

## 등비 수열(일반항) 공식 : an = a1 * r^(n-1)
## 등비 수열(합) 공식 sn = a1 * r^(n-1) / (1-r)

## 등비수열의 n번째 값과 합을 출력
def sequenceCal(n1, r, n):

    valueN = 0; sumN = 0

    i = 1
    while i <= n:

        if i == 1:
            valueN = n1
            sumN += valueN
            print(f'{i}번째 항의 값 : {valueN}')
            print(f'{i}번째 항까지의 합 : {sumN}')

            i += 1
            continue

        valueN *= r
        sumN += valueN
        print(f'{i}번째 항의 값 : {valueN}')
        print(f'{i}번째 항까지의 합 : {sumN}')

        i += 1

inputN1 = int(input('a1 입력 : '))
inputR = int(input('공비 입력 : '))
inputN = int(input('n 입력 : '))

sequenceCal(inputN1, inputR, inputN)