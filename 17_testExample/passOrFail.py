# 모듈(01)

## 과목별 점수를 입력하면 합격 여부를 출력하는 모듈 만들기 (평균:60, 과락:40)
def exampleResult(s1, s2, s3, s4, s5):

    passAvgScore = 60
    limitScore = 40

    def getTotal():
        totalScore = s1 + s2 + s3 + s4 + s5
        print(f'총점 : {totalScore}')
        return totalScore

    def getAverage():
        avg = getTotal() / 5
        print(f'평균 : {avg}')
        return avg

    def printPassOrFail():
        print(f'{s1}: Pass') if s1 >= limitScore else print(f'{s1}: Fail')
        print(f'{s2}: Pass') if s2 >= limitScore else print(f'{s2}: Fail')
        print(f'{s3}: Pass') if s3 >= limitScore else print(f'{s3}: Fail')
        print(f'{s4}: Pass') if s4 >= limitScore else print(f'{s4}: Fail')
        print(f'{s5}: Pass') if s5 >= limitScore else print(f'{s5}: Fail')

    def printFinalPassOrFail():

        if getAverage() >= passAvgScore:
            if s1 >= limitScore and s2 >= limitScore and s3 >= limitScore and s4 >= limitScore and s5 >= limitScore:
                print('Final Pass!!')
            else:
                print('Final Fail!!')
        else:
            print('Final Pass!!')

    getAverage()
    printPassOrFail()
    printFinalPassOrFail()



