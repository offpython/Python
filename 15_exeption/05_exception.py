# # exception 클래스
# ## exception은 예외를 담당하는 클래스
#
# num1 = int(input('input number1 : '))
# num2 = int(input('input number2 : '))
#
# try:
#     print(f'num1 / num2 = {num1 / num2}')
#
# # 어떤 예외가 발생했는지 정보 이용
# except Exception as e:
#     print('0으로 나눌 수 없습니다.')
#     print(f'exception : {e}')
#
# print(f'num1 * num2 = {num1 * num2}')
# print(f'num1 - num2 = {num1 - num2}')
# print(f'num1 + num2 = {num1 + num2}')

# # raise
# ## raise 키워드를 이용하면 예외를 발생시킬 수 있음
#
# def divCalculator(n1, n2):
#
#     if n2 != 0:
#         print(f'{n1} / {n2} = {n1 / n2}')
#     else:
#         raise Exception('0으로 나눌 수 없습니다.')
#
# num1 = int(input('input number1 : '))
# num2 = int(input('input number2 : '))
#
# try:
#     divCalculator(num1, num2)
#
# except Exception as e:
#     print(f'exception : {e}')

# 실습1
## 사용자가 문자메세지를 보낼 떄 10글자 이하면 sms, 초과하면 mms 발송하는 프로그램
def sendSMS(msg):

    if len(msg) > 10:
        raise Exception('길이 초과! MMS 전환 후 발송!', 1)
    else:
        print('SMS 발송!')

def sendMMS(msg):

    if len(msg) <= 10:
        raise Exception('길이 미달! SMS 전환 후 발송!', 2)
    else:
        print('MMS 발송!')


msg = input('input message : ')

try:
    sendSMS(msg)

except Exception as e:
    # args는 exception에 설정한 파라미터임. 배열형식이기 때문.
    print(f'exception : {e.args[0]}')
    print(f'exception : {e.args[1]}')

    if e.args[1] == 1:
        sendMMS(msg)
    elif e.args[1] == 2:
        sendSMS(msg)


