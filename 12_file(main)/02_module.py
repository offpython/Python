# 실행(메인)파일 01

# 실습1_unitConversion

import unitConversion as uc

inputNumber = int(input('길이(cm) 입력 : '))

returnValue = uc.cmToMm(inputNumber)
print(f'returnValue : {returnValue}mm')

returnValue = uc.cmToInch(inputNumber)
print(f'returnValue : {returnValue}inch')

returnValue = uc.cmToM(inputNumber)
print(f'returnValue : {returnValue}m')

returnValue = uc.cmToFt(inputNumber)
print(f'returnValue : {returnValue}ft')