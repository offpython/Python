# 모듈 불러오기

# calmodule
import calmodule

calmodule.add(10, 20)
calmodule.sub(10, 20)
calmodule.mul(10, 20)
calmodule.div(10, 20)

# 실습 1_lottoMachine
import lottoMachine

result = lottoMachine.getLottoNumbers()
print(f'lottoNumbers : {result}')

# 실습 2_reverseString
import reverseStr

userInput = input('문자열 입력 : ')
reverseString = reverseStr.reverseStr(userInput)
print(f'reversedString : {reverseString}')