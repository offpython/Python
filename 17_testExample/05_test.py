# 함수(5)

## 등차수열 공식 : an = a1 + (n-1) * d
## 등차수열 합 공식 : sn = n * (a1 + an) / 2

## 등차수열의 n번째 값과 합을 출력
def sequenceCalculator(n1, d, n):

    valueN = 0; sumN = 0;

    i = 1
    while i <= n:

        if i == 1:
            valueN = n1
            sumN += valueN
            print(f'{i}번째 항의 값 : {valueN}')
            print(f'{i}번째 항까지의 합 : {sumN}')

            i += 1
            continue

        valueN += d
        sumN += valueN
        print(f'{i}번째 항의 값 : {valueN}')
        print(f'{i}번째 항까지의 합 : {sumN}')

        i += 1

inputN1 = int(input('n1 입력 :'))
inputD = int(input('공차 입력 :'))
inputN = int(input('n 입력 :'))

sequenceCalculator(inputN1, inputD, inputN)

