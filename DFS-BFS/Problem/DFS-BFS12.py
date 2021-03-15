# DFS와 BFS
# 외부에서 입력을 제공받음 (https://www.acmicpc.net/problem/1260 참고)
"""
실수했던 점: sorted(graph[i])를 그래프를 만들기전에 진행함

기억해야할 점: dfs와 bfs를 각각 구현 성공해냄
            dfs는 재귀함수로
            bfs는 큐 자료형으로
"""
from sys import stdin
from collections import deque
nodeCount, edgeCount, startNode = map(int, stdin.readline().rstrip().split())
graph = [[] for i in range(nodeCount+1)]
Bvisited = [False for i in range(nodeCount+1)]
Dvisited = [False for i in range(nodeCount+1)]
Bresult = []
Dresult = []
for i in range(edgeCount):
  node1, node2 = map(int, stdin.readline().rstrip().split())
  graph[node1].append(node2)
  graph[node2].append(node1)
for i in range(len(graph)):
  graph[i] = sorted(graph[i])
def bfs(start):
  queue = deque([start])
  Bvisited[start] = True
  while queue:
    now = queue.popleft()
    Bresult.append(now)
    for node in graph[now]:
      if Bvisited[node] == False:
        queue.append(node)
        Bvisited[node] = True


def dfs(now):
  Dresult.append(now)
  for node in graph[now]:
    if Dvisited[node] == False:
      Dvisited[node] = True
      dfs(node)


Dvisited[startNode] = True
dfs(startNode)
for i in range(len(Dresult)):
  print(Dresult[i], end=' ')
print()

bfs(startNode)
for i in range(len(Bresult)):
  print(Bresult[i], end=' ')
print()