# 외벽 점검
# 외부 코드에서 n, weak, dist를 제공받음 (https://programmers.co.kr/learn/courses/30/lessons/60062 참고)
"""
실수했던 점: -1을 반환하는 코드를 생각하지 못했다.
           예외처리, 종료조건등을 확실히 하자.

기억해야할 점: permutations 를 임포트해 순열을 구할 수 있었다.
             2바퀴 어치 리스트를 만들어 구현을 간단히 할 수 있었다.
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