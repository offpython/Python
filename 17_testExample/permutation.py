# 모듈(04)

## 순열 계산 모듈을 만들고 결과 출력

def getPermutationCnt(n, r, logPrint = True):

    result = 1
    for n in range(n, (n - r), -1):
        if logPrint: print('n : {}'.format(n)) #로그찍기
        result = result * n

    return result

# 모듈 이용_ 경우의 수까지 반환해줌
from itertools import permutations

def getPermutations(ns, r):

    pList = list(permutations(ns, r))
    print(f'{len(ns)}P{r}개수 : {len(pList)}')

    for n in permutations(ns, r):
        print(n, end=', ')
