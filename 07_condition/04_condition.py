# 다자택일 조건문(if~elif문)
# 여러 가지 조건식 결과에 따라 실행문이 결정됨.

exampleScore = int(input('시험 성적 입력 : '))
grade = ' '

if exampleScore >= 90:
    grade = 'A'
elif exampleScore >= 80:
    grade = 'B'
elif exampleScore >= 70:
    grade = 'C'
elif exampleScore >= 60:
    grade = 'D'
else:
    grade = 'F'

print('성적 : {} \t 학점 : {}'.format(exampleScore, grade))

# 실습1
print('게절 : 봄, 여름, 가을, 겨울')
seasonStr = input('계절 입력 : ')

if seasonStr == '봄':
    print('{} : {}'.format('봄', 'Spring'))
elif seasonStr == '여름':
    print('{} : {}'.format('여름', 'Summer'))
elif seasonStr == '가을':
    print('{} : {}'.format('가을', 'Fall'))
elif seasonStr == '겨울':
    print('{} : {}'.format('겨울', 'Winter'))
else:
    print('검색할 수 없습니다.')

# 실습2
print('1.카페라떼(3.5) \t 2.에스프레소(3.0) \t 3.아메리카노(2.0) \t 4.곡물라떼(4.0) \t 5.밀크티(4.3)')
userSelectionNumber = int(input('메뉴 선택 : '))

print('-----------------------')
if userSelectionNumber == 1:
    print('메뉴 : 카페라떼')
    print('가격 : 3,500원')
elif userSelectionNumber == 2:
    print('메뉴 : 에스프레소')
    print('가격 : 3,000원')
elif userSelectionNumber == 3:
    print('메뉴 : 아메리카노')
    print('가격 : 2,000원')
elif userSelectionNumber == 4:
    print('메뉴 : 곡물라떼')
    print('가격 : 4,000원')
elif userSelectionNumber == 5:
    print('메뉴 : 밀크티')
    print('가격 : 4,500원')
else:
    print('검색할 수 없습니다.')
print('-----------------------')