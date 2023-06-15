# readlines()
## 파일의 모든 데이터를 읽어서 리스트 형태로 반환

# uri = '/Users/soysauce/Documents/Study/python/016_pythonTxt/'
#
# with open(uri + 'lans.txt', 'r') as f:
#     lanList = f.readlines()
#
# print(f'lanList : {lanList}')
# print(f'lanList tpye : {type(lanList)}')
#
## 한 행만 읽기
# with open(uri + 'lans.txt', 'r') as f:
#     line = f.readline()
#
#     while line != '':
#         print(f'line : {line}', end = '')
#         line = f.readline()
#
# 실습1
## 파일에 저장된 과목별 점수를 파이썬에서 읽어, 딕셔러니에 저장하는 코드 작성

scoreDic = {}

uri = '/Users/soysauce/Documents/Study/python/016_pythonTxt/'
with open(uri + 'scores.txt', 'r') as f:
    line = f.readline()

    while line != '':
        tempList = line.split(':')
        scoreDic[tempList[0]] = int(tempList[1].strip('\n'))
        line = f.readline()

print(f'scoreDic : {scoreDic}')