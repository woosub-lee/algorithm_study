def FindParent(array, current):
    if array[current] != current:
        array[current] = FindParent(array, array[current])
    return array[current]


def UnionParent(array, element1, element2):
    element1 = FindParent(array, element1)
    element2 = FindParent(array, element2)
    if element2 > element1:
        array[element2] = element1
    else:
        array[element1] = element2

# 서로소 집합을 이용한 사이클 여부 판별
def isCycled(array, element1, element2):
    if FindParent(array, element1) == FindParent(array, element2):
        return True
    return False


# 크루스칼 알고리즘 (최소신장트리 구하기)
NumberOfNode = int(input())
NumberOfEdge = int(input())
Nodes = [i for i in range(NumberOfNode+1)]
Edges = []
CostOfTree = 0
for i in range(NumberOfEdge):
    FirstNode, SecondNode, Distance = map(int, input().split())
    Edges.append([(FirstNode, SecondNode), Distance])
Edges = sorted(Edges, key=lambda x: x[1])
for Edge in Edges:
    # 사이클 여부 확인, 사이클을 존재하게 만드는 간선이면 continue
    if isCycled(Nodes, Edge[0][0], Edge[0][1]):
        continue
    # 아닐시 서로소집합에 추가, 거리 합산
    UnionParent(Nodes, Edge[0][0], Edge[0][1])
    CostOfTree += Edge[1]
print(CostOfTree)
"""
input
7
9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25
"""
"""
output
159
"""
