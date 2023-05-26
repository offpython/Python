# 모듈 생성

scores = []

def addScore(s):
    scores.append(s)

def getScore():
    return scores

def getTotalScore():
    total = 0
    for s in scores:
        total += s

    return total

def getAvgScore():
    avg = getTotalScore() / len(scores)

    return avg
