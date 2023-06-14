# # 사용자 Exception 클래스
# ## Exception 클래스를 상속해서 사용자 예외 클래스를 만들 수 있다.
#
# class NotUseZeroException(Exception):
#
#     def __init__(self, n):
#         super().__init__(f'{n}은(는) 사용할 수 없습니다.')
#
#
# def divCalculator(n1, n2):
#     if n2 == 0:
#         raise NotUseZeroException(n2)
#     else:
#         print(f'{n1} / {n2} = {n1 / n2}')
#
# num1 = int(input('input number1 : '))
# num2 = int(input('input number2 : '))
#
#
# try:
#     divCalculator(num1, num2)
# except NotUseZeroException as e:
#     print(e)
#

# 실습1
## 관리자 암호를 입력하고 다음상태에 따라 예외 처리하는 예외 클래스 만들기
## 암호 5미만 : PasswordLengthShortException
## 암호 10초과 : PasswordLengthLongException
## 암호 잘못된 경우 : PasswordWrongException

class PasswordLengthShortException(Exception):
    def __init__(self, str):
        super().__init__(f'{str} : 길이 5미만!')

class PasswordLengthLongException(Exception):
    def __init__(self, str):
        super().__init__(f'{str} : 길이 10초과!')

class PasswordWrongException(Exception):
    def __init__(self, str):
        super().__init__(f'{str} : 잘못된 암호!')

adminPW = input('input admin password : ')

try:
    if len(adminPW) < 5:
        raise PasswordLengthShortException(adminPW)
    elif len(adminPW) > 10:
        raise PasswordLengthLongException(adminPW)
    elif adminPW != 'admin1234':
        raise PasswordWrongException(adminPW)
    elif adminPW == 'admin1234':
        print('빙고')

except PasswordLengthShortException as e1:
    print(e1)
except PasswordLengthLongException as e2:
    print(e2)
except PasswordWrongException as e3:
    print(e3)

