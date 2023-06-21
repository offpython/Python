# 모듈(03)

## 로또 모듈을 만들기

import random

userNums = []; randNums = []; collNums = []
randBonusNum = 0

def setUserNums(ns):  # 사용자입력숫자
    global userNums
    userNums = ns

def getUserNums():
    return userNums

def setRandNums():
    global randNums
    randNums = random.sample(range(1, 46), 6)

def getRandNums():
    return randNums

def setBonusNum():
    global randBonusNum
    while True:
        randBonusNum = random.randint(1, 45)
        if randBonusNum not in randNums:
            break

def getBonusNum():
    return randBonusNum

def lottoResult():
    global userNums
    global randNums
    global collNums

    collNums = []
    for un in userNums:
        if un in randNums:
            collNums.append(un)

    if len(collNums) == 6:
        print('1등 당첨!')
        print(f'번호 : {collNums}')

    elif (len(collNums) == 5) and (randBonusNum in userNums):
        print('2등 당첨!')
        print(f'번호 : {collNums}, 보너스 번호 : {randBonusNum}')

    elif len(collNums) == 5:
        print('3등 당첨!')
        print(f'번호 : {collNums}')

    elif len(collNums) == 4:
        print('4등 당첨!')
        print(f'번호 : {collNums}')

    elif len(collNums) == 3:
        print('5등 당첨!')
        print(f'번호 : {collNums}')

    else:
        print('꽝! 다음 기회에')
        print(f'기계 번호 : {randNums}')
        print(f'보너스 번호 : {randBonusNum}')
        print(f'선택 번호 : {userNums}')
        print(f'일치 번호 : {collNums}')

def startLotto():
    n1 = int(input('번호(1~45) 입력 : '))
    n2 = int(input('번호(1~45) 입력 : '))
    n3 = int(input('번호(1~45) 입력 : '))
    n4 = int(input('번호(1~45) 입력 : '))
    n5 = int(input('번호(1~45) 입력 : '))
    n6 = int(input('번호(1~45) 입력 : '))
    selectNums = [n1, n2, n3, n4, n5, n6]

    setUserNums(selectNums)
    setRandNums()
    setBonusNum()

    lottoResult()





