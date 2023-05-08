# 데이터와 변수 사용법_04

# BMI = 몸무게(kg) / (신장(m) * 신장(m))
weight = input('체중 입력(g): ')
height = input('신장 입력(cm): ')

if weight.isdigit():
    weight = int(weight) / 10

if height.isdigit():
    height = int(height) / 100

print('체중 : {}kg'.format(weight))
print('신장 : {}m'.format(height))

bmi = weight / (height * height)
print('BMI : %.2f' % bmi)

# 실습2
num1 = 10
num2 = 20
print('num1 : {}, num2 : {}'.format(num1, num2))

tempNum = num1
num1 = num2
num2 = tempNum
print('num1 : {}, num2 : {}'.format(num1, num2))

# 실습3
midtermScore = input('중간 고사 점수 : ')
finalScore = input('기말 고사 점수 : ')

if midtermScore.isdigit() and finalScore. isdigit():
    midtermScore = int(midtermScore)
    finalScore = int(finalScore)

    totalScore = midtermScore + finalScore
    avgScore = totalScore / 2
    print('총점 : {}, 평균 : {}'.format(totalScore, avgScore))

else:
    print('잘못 입력했습니다.')