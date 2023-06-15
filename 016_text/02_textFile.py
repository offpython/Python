# # 텍스트파일 읽기
#
# file = open('/Users/soysauce/Documents/Study/python/016_pythonTxt/test.txt', 'r')
#
# str = file.read()
# print(f'str : {str}')
#
# file.close()
#
# # 실습1
# import time
#
# lt = time.localtime()
#
# # dateStr = '[' + str(lt.tm_year) + '년 ' + \
# #           str(lt.tm_mon) + '월 ' \
# #           + str(lt.tm_mday) + '일]'
#
# dateStr = '[' + time.strftime('%Y-%m-%d %H:%M:%S %p') + ']'
#
# todaySchedule = input('오늘 일정 : ')
#
# file = open('/Users/soysauce/Documents/Study/python/016_pythonTxt/test.txt', 'w')
# file.write(dateStr + todaySchedule)
# file.close()

# 실습1
## 텍스트파일에서 'Python'을 '파이썬'으로 변경해서 다시 저장

file = open('/Users/soysauce/Documents/Study/python/016_pythonTxt/about_python.txt', 'r', encoding='UTF8')

str = file.read()
print(f'str : {str}')

file.close()

str = str.replace('python','파이썬', 2)
print(f'str : {str}')

file = open('/Users/soysauce/Documents/Study/python/016_pythonTxt/about_python.txt', 'w', encoding='UTF8')
file.write(str)

file.close()

