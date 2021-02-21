# 문자열 압축
# 외부코드에서 문자열 s 제공 (https://programmers.co.kr/learn/courses/30/lessons/60057 참조)
from collections import deque


def solution(s):
    StrData = s
    StrLength = len(s)
    Result = 'a' * 1001

    for unit in range(1, StrLength + 1):

        Queue = deque()
        for i in range(0, StrLength, unit):
            Queue.append(StrData[i:i + unit])
        Queue.append('')

        PastStr = Queue.popleft()
        ZippedStr = ''
        count = 1

        while Queue:
            CurrentStr = Queue.popleft()
            if PastStr == CurrentStr:
                count += 1
            elif count > 1:
                ZippedStr += str(count) + PastStr
                PastStr = CurrentStr
                count = 1
            else:
                ZippedStr += PastStr
                PastStr = CurrentStr
                count = 1
        if len(Result) > len(ZippedStr):
            Result = ZippedStr

    answer = len(Result)
    return answer