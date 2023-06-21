# writelines()
## writelines()는 리스트(List) 또는 튜플 데이터를 파일에 쓰기 위한 함수

languages = ['c/c++', 'java', 'c#', 'python', 'javascript']

uri = '/Users/soysauce/Documents/Study/python/016_pythonTxt/'

# 기존 방식
for item in languages:
    with open(uri + 'languages.txt', 'a') as f:
        f.write(item)
        f.write('\n')

#  writelines() 사용
with open(uri + 'languages_01.txt', 'a') as f:
    f.writelines(item + '\n' for item in languages)

with open(uri + 'languages_01.txt', 'r') as f:
    print(f.read())

# 실습1
## 딕셔너리에 저장된 과목별 점수를 파일에 저장하는 코드 작성

uri = '/Users/soysauce/Documents/Study/python/016_pythonTxt/'

scoreDic = {'kor' : 85, 'eng' : 90, 'mat' : 92, 'sci' : 79, 'his' : 82}
for key in scoreDic.keys():
    with open(uri + 'scoreDic.txt', 'a') as f:
        f.write(key + '\t:' + str(scoreDic[key]) + '\n')

# 정렬없이
scoreDic = {'kor' : 85, 'eng' : 90, 'mat' : 92, 'sci' : 79, 'his' : 82}
scoreList = [85, 90, 92, 79, 82]
with open(uri + 'scores_list.txt', 'a') as f:
    print(scoreList, file=f)

