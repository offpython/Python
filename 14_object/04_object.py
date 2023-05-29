# 얕은복사와 깊은복사

## 얕은 복사란, 객체 주소를 복사하는 것으로 객체 자체가 복사되지 않는다.
##
class TemCls:

    def __init__(self, n, s):
        self.number = n
        self.str = s

    def printClsInfo(self):
        print(f'self.number : {self.number}')
        print(f'self.str : {self.str}')

# 얕은 복사
# tc1 = TemCls(10, 'Hello')
# tc2 = tc1
#
# tc2.number = 3.14
# tc2.str = 'bye'
#
# tc1.printClsInfo()
# tc2.printClsInfo()

## 깊은 복사
# import copy
#
# tc1 = TemCls(10, 'Hello')
# tc2 = copy.copy(tc1)
#
# tc2.number = 20
# tc2.str = 'bye'
#
# tc1.printClsInfo()
# tc2.printClsInfo()

# 리스트 복사
import copy

scores = [9, 8, 5, 7, 6, 10]
scoresCopy = []

# 얕은복사
# scoresCopy = scores
# print(f'id(scores) : {id(scores)}')
# print(f'id(scoresCopy) : {id(scoresCopy)}')

# # 깊은 복사1_ for문 이용
# for s in scores:
#     scoresCopy.append(s)
#
# print(f'id(scores) : {id(scores)}')
# print(f'id(scoresCopy) : {id(scoresCopy)}')

# # 깊은 복사2_ extend이용
# scoresCopy.extend(scores)
# print(f'id(scores) : {id(scores)}')
# print(f'id(scoresCopy) : {id(scoresCopy)}')

# # 깊은 복사3_ 리스트 자체 함수 copy이용
# scoresCopy = socres.copy()
# print(f'id(scores) : {id(scores)}')
# print(f'id(scoresCopy) : {id(scoresCopy)}')
#
# # 깊은 복사4_ 슬라이싱 이용
# scoresCopy = scores[:]
# print(f'id(scores) : {id(scores)}')
# print(f'id(scoresCopy) : {id(scoresCopy)}')

# 실습1
plaOriSco = [8.7, 9.1, 8.9, 9.0, 7.9, 9.5, 8.8, 8.3]
plaCopSco = plaOriSco[:]

plaOriSco.sort()
print(f'plaOriSco : {plaOriSco}')

plaCopSco.sort()
plaCopSco.pop(0)
plaCopSco.pop()
print(f'plaCopSco : {plaCopSco}')

oriTot = round(sum(plaOriSco), 2)
oriAvg = round(sum(plaOriSco) / len(plaOriSco), 2)
print(f'Original Total : {oriTot}')
print(f'Original Average : {oriAvg}')

copTot = round(sum(plaCopSco), 2)
copAvg = round(sum(plaCopSco) / len(plaCopSco), 2)
print(f'Copy Total : {copTot}')
print(f'Copy Average : {copAvg}')

print(f'oriAvg - copAvg : {round(oriAvg - copAvg, 2)}')