# site-packages에 있는 모듈은 어디서나 사용할 수 있다.

# import sys
#
# for path in sys.path:
#     print(path)

from calculator import cal
print(f'cal.add(10, 20) : {cal.add(10, 20)}')
print(f'cal.sub(10, 20) : {cal.sub(10, 20)}')
print(f'cal.mul(10, 20) : {cal.mul(10, 20)}')
print(f'cal.div(10, 20) : {cal.div(10, 20)}')

