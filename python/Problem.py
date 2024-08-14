class ProblemData:
    inputs = ['']
    results = ['']

    def GetInputs(self):
        return self.inputs

    def GetResults(self):
        return self.results

#1000
# ProblemData 인스턴스를 생성하여 리스트에 저장
problemData = [ProblemData() for _ in range(1)]

# 각 문제에 대한 입력과 결과를 설정
problemData[0].inputs = ['1', '2']
problemData[0].results = ['3']

#1406
problemData1 = [ProblemData() for _ in range(3)]

# 각 문제에 대한 입력과 결과를 설정
problemData1[0].inputs = ['abcd\n', '3\n', 'P', 'x\n', 'L\n', 'P', 'y\n']
problemData1[0].results = ['abcdyx']

problemData1[1].inputs = ['abc\n', '9\n', 'L\n', 'L\n', 'L\n', 'L\n', 'L\n', 'P', 'x\n', 'L\n', 'B\n', 'P', 'y\n']
problemData1[1].results = ['yxabc']

problemData1[2].inputs = ['dmih\n', '11\n', 'B\n', 'B\n', 'P x\n', 'L\n', 'B\n', 'B\n', 'B\n', 'P' ,'y\n',
                         'D\n', 'D\n', 'P', 'y\n']
problemData1[2].results = ['yxz']

# 문제 데이터 딕셔너리에 저장
problemDict = [
    {
        "problemNum": 1000,
        "problemValue": problemData
    },
    {
        "problemNum": 1406,
        "problemValue": problemData1
    }
]

def GetProblemValue(problemNum):
    for problem in problemDict:
        if problem["problemNum"] == problemNum:
            return problem["problemValue"]
    return None

# 문제 번호가 1000일 때만 출력
#if problemDict["problemNum"] == Problem_Number:
#    for i in range(1):
#        print(f"Problem {i+1}:")
#        print("Problem Number:", problemDict["problemNum"])  # 문제 번호 출력
#        print("Inputs:", problemDict["problemValue"][i].inputs)  # i번째 문제의 입력
#        print("Results:", problemDict["problemValue"][i].results)  # i번째 문제의 결과
#        print() #줄바꿈
        
#if __name__ == "__main__":
#    main()
