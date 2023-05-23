# 조건문 04

part = int(input('업종 선택(1. 가정용 \t 2.대중탕용 \t 3.공업용) : '))
userWater = int(input('사용량 : '))
unitPrice = 0

if part == 1:
    unitPrice = 540

elif part == 2:
    if userWater <= 50:
        unitPrice = 820
    elif userWater > 50 and userWater <= 300:
        unitPrice = 1920
    elif userWater > 300:
        unitPrice = 2400

elif part == 3:
    if userWater <= 500:
        unitPrice = 240
    else:
        unitPrice = 470

print('=' * 30)
print('상수도 요금표')
print('-' * 30)
print('사용량 \t : \t 요금')
userPrice = userWater * unitPrice
print('{} \t : \t {}원'.format(userWater, format(userPrice, ',')))
print('=' * 30)
