# 산술 연산자(나머지와 몫)

# % = 나머지, // = 몫
num1 = 10
num2 = 3

result = num1 // num2
print(result)

# divmod()함수 = 나머지와 몫 한번에 구함
result = divmod(num1, num2)    #(3,1)
print('result: {}'.format(result))

print('몫 : {}'.format(result[0]))
print('나머지 : {}'.format(result[1]))

# 실습
allStuCnt = int(input('전체 학생 수 : '))
stuCntOfGroup = int(input('한 모둠 학생 수 : '))

groupCnt = allStuCnt // stuCntOfGroup
overStuCnt = allStuCnt % stuCntOfGroup

print('전체 학생 수 : {}'.format(allStuCnt))
print('한 모둠 학생 수 : {}'.format(stuCntOfGroup))
print('모둠 수 : {}'.format(groupCnt))
print('남는 학생 수 : {}'.format(overStuCnt))

result = divmod(allStuCnt, stuCntOfGroup) # (6,1)
print('전체 학생 수 : {}'.format(allStuCnt))
print('한 모둠 학생 수 : {}'.format(stuCntOfGroup))
print('모둠 수 : {}'.format(result[0]))
print('남는 학생 수 : {}'.format(result[1]))

# 실습2
employee = 123
apple = 4
result = divmod(employee, apple)
print('사과를 나누어 줄 수 있는 최대 직원 수 : {}'.format(result[0]))
print('남는 사과 개수 : {}'.format(result[1]))