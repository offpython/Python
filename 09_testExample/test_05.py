# 데이터와 변수 사용법_05

# 실습1
selectNumber = input('언어 선택(Choose your language): 1.한국어 \t 2.English')

if selectNumber == '1':
    menu = '1.샌드위치 \t 2.햄버거 \t 3.쥬스 \t 4.커피 \t 5.아이스크림'
elif selectNumber == '2':
    menu = '1.Sandwich \t 2.Hamberger \t 3.Juice \t 4.Coffee \t 5.Icecream'

print(menu)

# 실습2
import datetime

today = datetime.datetime.today()

myAge = input('나이 입력 : ')
if myAge.isdigit():
   afterAge = 100 - int(myAge)
   myHundred = today.year + afterAge

   print('{}년({}년후)에 100살!!'.format(myHundred, afterAge자))

else:
    print('잘못 입력했습니다.')