# 모듈 제작

import random

def getLottoNumbers():
    result = random.sample(range(1, 45), 6)

    return result

