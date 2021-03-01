# 특정 거리의 도시 찾기
# 외부에서 입력예제 제공 (https://www.acmicpc.net/problem/18352 참고)
"""
실수했던 점: 출력에 오류가 있었다.

기억해야할 점: deque를 이용해 bfs를 사용할 수 있었다.
"""

import sys
from collections import deque
n, m, k, x = map(int, sys.stdin.readline().rstrip().split())
edges = []
for i in range(m):
    startNode, endNode = map(int, sys.stdin.readline().rstrip().split())
    edges.append([startNode, endNode])
graph = [[] for i in range(n+1)]
visited = [False for i in range(n+1)]
for edge in edges:
    graph[edge[0]].append(edge[1])
queue = deque([x])
distances = [-1 for i in range(n+1)]
distances[x] = 0
while queue:
    nowNode = queue.popleft()
    for nextNode in graph[nowNode]:
        if distances[nextNode] == -1:
            distances[nextNode] = distances[nowNode] + 1
            queue.append(nextNode)

if distances.count(k) != 0:
    for i in range(1, len(distances)):
        if distances[i] == k:
            print(i)
else:
    print(-1)



