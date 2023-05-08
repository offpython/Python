# 다자택일 조건문 사용 시 주의할 점

# 조건식 순서가 중요하다.
# 조건 범위를 명시한다. (순서와 상관 없어짐)

# 실습1
carDisplacement = int(input('자동차 배기량 입력 : '))

if carDisplacement < 1000:
    print('세금 : 100,000원')
elif carDisplacement >= 1000 and carDisplacement < 2000:
    print('세금 : 200,000원')
elif carDisplacement >= 2000 and carDisplacement < 3000:
    print('세금 : 300,000원')
elif carDisplacement >= 3000 and carDisplacement < 4000:
    print('세금 : 400,000원')
elif carDisplacement >= 4000 and carDisplacement < 5000:
    print('세금 : 500,000원')
elif carDisplacement >= 5000:
    print('세금 : 600,000원')
