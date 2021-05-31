# 바이러스
# 외부에서 입력예제 제공 (https://programmers.co.kr/learn/courses/30/lessons/2606 참고)
"""
실수했던 점: 문제의 요구사항을 간과해 1번 노드 또한 답에 포함시켰다.

기억해야할 점: 그래프형태의 dfs를 구현하였다.
"""
nodeCount = int(input())
edgeCount = int(input())
graph = [[] for i in range(nodeCount+1)]
visited = [False for i in range(nodeCount+1)]
numberOfInfectedNode = 0
for i in range(edgeCount):
    firstNode, secondNode = list(map(int, input().split()))
    graph[firstNode].append(secondNode)
    graph[secondNode].append(firstNode)

def dfs(nowNode):
    global visited
    global numberOfInfectedNode
    for nextNode in graph[nowNode]:
        if not visited[nextNode]:
            visited[nextNode] = True
            dfs(nextNode)
            numberOfInfectedNode += 1
    
visited[1] = True
dfs(1)
print(numberOfInfectedNode)
