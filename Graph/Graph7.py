# 커리큘럼 (위상 정렬)
from collections import deque
from copy import deepcopy
NumberOfLecture = int(input())
Lectures = [[] for i in range(NumberOfLecture+1)]
LecturesIndegree = [0 for i in range(NumberOfLecture+1)]
Time = [0 for i in range(NumberOfLecture+1)]
Queue = deque()
for i in range(1, NumberOfLecture+1):
    Lecture = list(map(int, input().split()))
    Time[i] = Lecture.pop(0)
    for j in Lecture[:-1]:
        LecturesIndegree[i] += 1
        Lectures[j].append(i)

Result = deepcopy(Time)
for i in range(1, NumberOfLecture+1):
    if LecturesIndegree[i] == 0:
        Queue.append(i)
while Queue:
    CurrentLecture = Queue.popleft()
    for i in Lectures[CurrentLecture]:
        Result[i] = max(Result[i], Result[CurrentLecture] + Time[i])
        LecturesIndegree[i] -= 1
        if LecturesIndegree[i] == 0:
            Queue.append(i)

for i in range(1, NumberOfLecture+1):
    print(Result[i])



