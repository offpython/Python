# 텍스트 파일 쓰기

file = open('/016_pythonTxt/test.txt', 'w')

strCnt = file.write('Hello PYTHON!')
print(f'strCnt : {strCnt}')

file.close()

# 실습1

import time

lt = time.localtime()

dateStr = '[' + str(lt.tm_year) + '년 ' + \
          str(lt.tm_mon) + '월 ' \
          + str(lt.tm_mday) + '일]'

todaySchedule = input('오늘 일정 : ')

file = open('/016_pythonTxt/test.txt', 'w')
file.write(dateStr + todaySchedule)
file.close()
