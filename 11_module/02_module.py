# 모듈 불러오기

# calmodule
import calculator

calculator.add(10, 20)
calculator.sub(10, 20)
calculator.mul(10, 20)
calculator.div(10, 20)

# 실습 1_lottoMachine
import lottoMachine

result = lottoMachine.getLottoNumbers()
print(f'lottoNumbers : {result}')

# 실습 2_reverseString
import reverseStr

userInput = input('문자열 입력 : ')
reverseString = reverseStr.reverseStr(userInput)
print(f'reversedString : {reverseString}')