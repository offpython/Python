# 모듈(05)

## 조합 계산 모듈을 만들고 결과 출력

import combination as ct

# numbN = int(input('numN 입력 : '))
# numbR = int(input('numR 입력 : '))
#
# ct.getCombinationCnt(numbN, numbR)
# print(f'{numbN}C{numbR} : {ct.getCombinationCnt(numbN, numbR, logPrint=False)}') #로그 출력 싫을 땐 False 써줌

listVar = [1, 2, 3, 4, 5, 6, 7, 8]
rVar = 3
ct.getCombinations(listVar, rVar)
