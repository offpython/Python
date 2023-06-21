# 모듈(05)

## 조합 계산 모듈을 만들고 결과 출력

def getCombinationCnt(n, r, logPrint = True): #로그찍기

    resultP = 1
    resultR = 1
    resultC = 1

    for n in range(n, (n-r), -1):
        resultP = resultP * n
    if logPrint:
        print(f'resultP: {resultP}') #로그찍기

    for n in range(r, 0, -1):
        resultR = resultR * n
    if logPrint: print(f'resultR: {resultR}')  #로그찍기

    resultC = int(resultP / resultR)
    if logPrint: print(f'resultC: {resultC}')  #로그찍기

    return resultC

# 파이썬 모듈 이용

from itertools import combinations

def getCombinations(ns, r):
    cList = list(combinations(ns, r))
    print(f'{len(ns)}C{r} : {len(cList)}')

    for n in combinations(ns, r):
        print(n, end=', ')