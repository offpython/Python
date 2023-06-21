# 모듈(04)

## 순열 계산 모듈을 만들고 결과 출력

import permutation as pt

numN = int(input('numN 입력 : '))
numR = int(input('numR 입력 : '))

#def getPermutationCnt 이용 시,
print(f'{numN}P{numR} = {pt.getPermutationCnt(numN, numR, logPrint=True)}') # 로그 출력 싫을 땐 False 써줌

# 모듈 itertools에서 Permutations 이용 시(반환 내용까지 보여줌),
listVar = [1, 2, 3, 4, 5, 6, 7, 8]
rVar = 3

pt.getPermutations(listVar, rVar)