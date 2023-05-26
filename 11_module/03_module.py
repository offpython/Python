# 모듈 사용
## import, as

import calculator as cal

cal.add(10, 20)
cal.sub(10, 20)
cal.mul(10, 20)
cal.div(10, 20)

## from 모듈 import 기능 = 특정 기능만 이용
from calculator import add
from calculator import sub

# 또는
from calculator import add, sub

add(10, 20)
sub(10, 20)

## 전체 기능 가져올 때 = *
from calculator import *

cal.add(10, 20)
cal.sub(10, 20)
cal.mul(10, 20)
cal.div(10, 20)

# 실습1_scores
import scores as sc

korScore = int(input('국어 점수 입력 : '))
engScore = int(input('영어 점수 입력 : '))
matScore = int(input('수학 점수 입력 : '))

sc.addScore(korScore)
sc.addScore(engScore)
sc.addScore(matScore)

print(f'점수 : {sc.getScore()}')
print(f'총점 : {sc.getTotalScore()}')
print(f'평균 : {sc.getAvgScore()}')

