# with ~ as문
## with ~ as문을 이용하면 파일 닫기(close)를 생략할 수 있다.

# uri = '/Users/soysauce/Documents/Study/python/016_pythonTxt/'

# file = open(uri + 'with_as.txt', 'a')
# file.write('python study!')
# file.close()
#
# file = open(uri + 'with_as.txt', 'r')
# str = file.read()
# print(f'str : {str}')
# file.close()

# with open(uri + 'with_as_01.txt', 'a') as f:
#     f.write('python study!')
#
# with open(uri + 'with_as_01.txt', 'r') as f:
#     print(f.read())

# 실습1
## 로또 번호 생성기 프로그램을 만들고 파일에 번호를 출력

import random

uri = '/Users/soysauce/Documents/Study/python/016_pythonTxt/'

def writeNumbers(nums):
    for idx, num in enumerate(nums):
        with open(uri + 'lotto.txt', 'a') as f:
            if idx < len(nums) - 2:
                f.write(str(num) + ', ')
            elif idx == len(nums) - 2:
                f.write(str(num))
            elif idx == len(nums) - 1:
                f.write('\n')
                f.write('Bonus : ' + str(num))
                f.write('\n')

rNums = random.sample(range(1, 46), 7)
print(f'rNums : {rNums}')

writeNumbers(rNums)