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

# 실습1
