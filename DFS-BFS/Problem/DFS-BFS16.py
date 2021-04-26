# 여행경로
# 외부에서 입력예제 제공 (https://programmers.co.kr/learn/courses/30/lessons/43164 참고)
"""
실수했던 점: result를 설정할때 깊은 복사가 아니라 얕은 복사가 이루어져서 리스트를 이루는데 어려움을 격었다.

기억해야할 점: dfs에서 deepcopy를 고려해야 할 수도 있겠다.
"""
import copy
number_of_tickets = 0
used_tickets = []
airport_tickets = []
result = []
def dfs(depth, path):
    global result
    global used_tickets
    if depth == number_of_tickets:
        if not result:
            result = copy.deepcopy(path)
        return
    for i in range(number_of_tickets):
        if airport_tickets[i][0] == path[-1] and used_tickets[i] != True:
            path.append(airport_tickets[i][1])
            used_tickets[i] = True
            dfs(depth + 1, path)
            path.pop(len(path) - 1)
            used_tickets[i] = False

def solution(tickets):
    global number_of_tickets
    global used_tickets
    global airport_tickets
    tickets.sort()
    number_of_tickets = len(tickets)
    used_tickets = [False for i in range(number_of_tickets)]
    airport_tickets = tickets
    dfs(0, ["ICN"])
    return result