import Problem
import sys
import io

code_string = None
output_result = None
problemNum = 0
problemDatas = Problem.ProblemData()

def GetData():
    global problemNum
    global problemDatas
    global code_string

    problemNum = 1406
    code_string = """
from sys import stdin

# 연결리스트의 노드 클래스
class ListNode:
    def __init__(self, val, prev, next):
        self.val = val
        self.prev = prev
        self.next = next

# 연결리스트의 head
head = ListNode('dummy', None, None)
curr = head

init = input() # 초기 문자열
for i in range(len(init)): # 초기 문자열을 연결리스트로 만들어 둠
    new_node = ListNode(init[i], None, None)
    curr.next = new_node
    new_node.prev = curr
    curr = new_node

# 명령어들 처리
for _ in range(int(input())):
    command = stdin.readline().rstrip()
    if command == 'L':
        if curr.val != 'dummy':
            curr = curr.prev
    elif command == 'D':
        if curr.next:
            curr = curr.next
    elif command == 'B':
        if curr.val != 'dummy':
            curr = curr.prev
            if curr.next.next:
                curr.next = curr.next.next
                curr.next.prev = curr
            else:
                curr.next = None
    else:
        new_node = ListNode(command[-1], None, None)
        if curr.next:
            new_node.next = curr.next
            curr.next.prev = new_node
        curr.next = new_node
        new_node.prev = curr
        curr = new_node

# head 다음 노드부터 출력
print_node = head.next
while print_node:
    print(print_node.val, end='')
    print_node = print_node.next"""
    problemDatas = Problem.GetProblemValue(problemNum)

#코드 실행
def CodeRun():
    global output_result
    global problemDatas

    for problemData in problemDatas:
        inputs = problemData.GetInputs()
        results = problemData.GetResults()

        #입력 값 개수에 맞는 입력값 대입
        input_string = " ".join(map(str, inputs))  # 입력값을 한 줄로 만듦
        input_data = io.StringIO(input_string + "\n")
        sys.stdin = input_data

        #출력 값 받기 설정
        output_capture = io.StringIO()
        sys.stdout = output_capture

        #코드 실행 시도
        try:
            exec(code_string)
        except SystemExit as e:
            print("error")
        except Exception as e:
            print("오류 발생")
            print(e)

        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__

        output_result = output_capture.getvalue()

        #정답 체점
        result_bool = ScoreTheAnswer(results)
        if(result_bool == False):
            return False
    return True

# 정답 채점
def ScoreTheAnswer(results):
    global output_result

    print(output_result + ' ' + results[0])
    output_result = output_result.replace("\n", "")
    if(output_result == results[0]):
        return True
    return False

def Main():
    GetData()
    result_bool = CodeRun()

    if(result_bool == False):
        print("정답 아님")
    else:
        print("정답")
    print("result:", output_result)

Main()