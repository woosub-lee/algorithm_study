# 가장 가까운 공통 조상
# 외부코드에서 입력을 제공받음 (https://www.acmicpc.net/problem/3584 참고)
"""
실수했던 점: 비교대상을 항상 최신의 노드로 하였다.

기억해야할 점: node들의 부모를 가까운 순으로 기록하여 처리하였다.
"""
nodes = []


def find_parent(node):
    if nodes[node] == node:
        return node
    return nodes[node]


for i in range(int(input())):
    nodeCount = int(input())
    nodes = [_ for _ in range(nodeCount+1)]
    for _ in range(nodeCount-1):
        parentNode, childNode = map(int, input().split())
        nodes[childNode] = parentNode
    targetNode1, targetNode2 = map(int, input().split())
    node1_parents = [targetNode1]
    node2_parents = [targetNode2]
    while targetNode1 != targetNode2:
        targetNode1 = find_parent(targetNode1)
        targetNode2 = find_parent(targetNode2)
        node1_parents.append(targetNode1)
        node2_parents.append(targetNode2)
    for parent in node1_parents:
        if parent in node2_parents:
            print(parent)
            break
