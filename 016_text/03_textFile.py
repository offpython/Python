# 텍스트파일 열기

# uri = '/Users/soysauce/Documents/Study/python/016_pythonTxt/'

# 'w' 파일 모드
file = open(uri + 'Hello.txt', 'w')
file.write('Hello Python!')
file.close()

# 'a' 파일 모드
file = open(uri + 'Hello.txt', 'a')
file.write('\nNice to meet you.')
file.close()

# 'x' 파일 모드
# 기존 파일이 있을 경우 에러(FileExistsError)
file = open(uri + 'Hello_01.txt', 'x')
file.write('\nNice to meet you.')
file.close()

# 'r' 파일 모드
file = open(uri + 'Hello_01.txt', 'r')
str = file.read()
print(f'str : {str}')
file.close()

# 실습1
## 사용자가 입력한 숫자에 대한 소수를 구하고 이를 파일에 작성
uri = '/Users/soysauce/Documents/Study/python/016_pythonTxt/'

def writePrimeNumber(n):
    file = open(uri + 'prime_numbers.txt', 'a')
    file.write(str(n))
    file.write('\n')
    file.close()

inputNumber = int(input('0보다 큰 정수 입력 : '))

for number in range(2, (inputNumber + 1)):
    flag = True
    for n in range(2, number):
        if number % 2 == 0:
            flag = False
            break

    if flag:
        writePrimeNumber(number)

