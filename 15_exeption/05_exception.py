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

# raise
## raise 키워드를 이용하면 예외를 발생시킬 수 있음

def divCalculator(n1, n2):

    if n2 != 0:
        print(f'{n1} / {n2} = {n1 / n2}')
    else:
        raise Exception('0으로 나눌 수 없습니다.')

num1 = int(input('input number1 : '))
num2 = int(input('input number2 : '))

try:
    divCalculator(num1, num2)

except Exception as e:
    print(f'exception : {e}')