# 팀 결성 (서로소 집합)
def FindTeam(students, student):
    if students[student] != student:
        students[student] = FindTeam(students, students[student])
    return students[student]


def CombineTeam(students, studentA, studentB):
    studentA = FindTeam(students, studentA)
    studentB = FindTeam(students, studentB)
    if studentA > studentB:
        students[studentA] = studentB
    else:
        students[studentB] = studentA


def isSameTeam(students, studentA, studentB):
    studentA = FindTeam(students, studentA)
    studentB = FindTeam(students, studentB)
    if studentA == studentB:
        print('YES')
    else:
        print('NO')


NumberOfStudent, NumberOfCommand = map(int, input().split())
Students = [i for i in range(NumberOfStudent+1)]
for i in range(NumberOfCommand):
    KindOfCommand, StudentA, StudentB = map(int, input().split())
    if KindOfCommand == 0:
        CombineTeam(Students, StudentA, StudentB)
    elif KindOfCommand == 1:
        isSameTeam(Students, StudentA, StudentB)

"""
input
7 3
0 1 2
0 2 3
1 1 3
"""
"""
output
YES
"""

