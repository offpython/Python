# 비교연산자(문자 비교)

# 아스키코드
cha1 = 'A' # 65
cha2 = 'B' # 83

print('\'{}\' > \'{}\' : {}'.format(cha1, cha2, (cha1 > cha2)))
print('\'{}\' >= \'{}\' : {}'.format(cha1, cha2, (cha1 >= cha2)))
print('\'{}\' < \'{}\' : {}'.format(cha1, cha2, (cha1 < cha2)))
print('\'{}\' <= \'{}\' : {}'.format(cha1, cha2, (cha1 <= cha2)))
print('\'{}\' == \'{}\' : {}'.format(cha1, cha2, (cha1 == cha2)))
print('\'{}\' != \'{}\' : {}'.format(cha1, cha2, (cha1 != cha2)))

# 문자 > 아스키 코드 변환 = ord()
print('\'A\' -> {}'.format(ord('A')))
print('\'S\' -> {}'.format(ord('S')))

# 문자 > 숫자  = chr()
print(' 65 -> {}'.format(chr(65)))
print(' 83 -> {}'.format(chr(83)))

# 문자열 비교  (같다 or 같지않다)
str3 = 'Hello'
str4 = 'hello'

print('{} == {} : {}'.format(str3, str4, (str3 == str4)))
print('{} != {} : {}'.format(str3, str4, (str3 != str4)))

# 실습
userInputAlphabet = input('알파벳 입력 : ')
print('{} : {}'.format(userInputAlphabet, ord(userInputAlphabet)))

userInputASCII = int(input('아스키 코드 입력 : '))
print('{} : {}'.format(userInputASCII, chr(userInputASCII)))