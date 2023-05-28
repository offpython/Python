# math 모듈

## 수학 관련 함수

listVar = [2, 5, 3.14, 58, 10, 2]

### 합
print(f'sum : {sum(listVar)}')

### 최댓값
print(f'max : {max(listVar)}')

### 최솟값
print(f'min : {min(listVar)}')

### 거듭제곱
print(f'pow(13의 2 거듭제곱) : {pow(13, 2)}')
print(f'pow(13의 3 거듭제곱) : {pow(13, 3)}')
print(f'pow(13의 4 거듭제곱) : {pow(13, 4)}')

# 반올림
print(f'round(3.141592의 첫번째 자리까지 반올림 : {round(3.141592, 1)}')
print(f'round(3.141592의 두번째 자리까지 반올림 : {round(3.141592, 2)}')
print(f'round(3.141592의 세번째 자리까지 반올림 : {round(3.141592, 3)}')

import math

# 절대값
print(f'-10의 절댓값 : {math.fabs(-10)}')
print(f'-0.12895의 절댓값 : {math.fabs(-0.12895)}')

# 올림
print(f'0.12895의 올림 : {math.ceil(0.12895)}')
print(f'-0.12895의 올림 : {math.ceil(-0.12895)}')

# 내림
print(f'0.12895의 내림 : {math.floor(0.12895)}')
print(f'-0.12895의 내림 : {math.floor(-0.12895)}')

# 버림
print(f'0.12895의 버림 : {math.trunc(0.12895)}')
print(f'-0.12895의 버림 : {math.trunc(-0.12895)}')

# 최대공약수
print(f'14, 21의 최대공약수  : {math.gcd(14, 21)}')

# 팩토리얼
print(f'10의 팩토리얼 : {math.factorial(10)}')

# 제곱근
print(f'4의 제곱근 : {math.sqrt(4)}')
print(f'12의 제곱근 : {math.sqrt(12)}')







