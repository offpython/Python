# # finally
# ## 예외 발생과 상관없이 항상 실행
#
# try:
#     inputData = input('input number : ')
#     numInt = int(inputData)
#
# except:
#     print('exception raised')
#     print('not number')
#
# else:
#     if numInt % 2 == 0:
#         print('even number!')
#     else:
#         print('odd number!')
#
# finally:
#     print(f'input data: {inputData}')
#
# 실습1
## 사용자로부터 숫자 5개 받아 짝수/홀수/실수와 입력한 모든 데이터를 각각 출력하는 프로그램

eveList = []; oddList = []; floatList = []
dataList = []

n = 1
while n < 6:

    try:
        data = input('input number : ')
        floatNum = float(data)

    except:
        print('exception raised!')
        print('input number again!')
        continue

    else:
        if floatNum - int(floatNum) != 0:
            print('float number!')
            floatList.append(floatNum)
        else:
            if floatNum % 2 == 0:
                print('even number!')
                eveList.append(int(floatNum))
            else:
                print('odd number')
                oddList.append(int(floatNum))

        n += 1

    finally:
        dataList.append(data)

print(f'data list: {eveList}')
print(f'data list: {oddList}')
print(f'data list: {floatList}')
print(f'data list: {dataList}')


