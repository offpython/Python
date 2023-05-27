# 실행(메인)파일 01 _add/sub/mul/divModule 실습

## __name__에는 모듈 이름이 저장되거나 '__main__'이 저장된다.

import addModule
import subModule
import mulModule
import divModule

def mod(n1, n2):
    return n1 % n2

if __name__ == '__main__':
    print(addModule.add(10, 20))
    print(subModule.sub(10, 20))
    print(mulModule.mul(10, 20))
    print(divModule.div(10, 20))




