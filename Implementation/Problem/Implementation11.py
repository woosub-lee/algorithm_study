# 외벽 점검
# 외부 코드에서 n, weak, dist를 제공받음 (https://programmers.co.kr/learn/courses/30/lessons/60062 참고)
"""
실수했던점:

기억해야할 점:
"""

from itertools import permutations
def solution(n, weak, dist):
    answer = len(dist) + 1
    Length = len(weak)
    Walls = weak + [point+n for point in weak]
    friendsList = list(permutations(dist, len(dist)))
    for startPoint in range(Length):
        for friends in friendsList:
            count = 1
            position = Walls[startPoint] + friends[count-1]
            for index in range(startPoint, startPoint+Length):
                if position < Walls[index]:
                    count += 1
                    if count > len(dist):
                        break
                    position = Walls[index] + friends[count-1]
            answer = min(answer, count)
    if answer > len(dist):
            return -1
    return answer