# 서로소 집합을 활용한 사이클 판별
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


NumberOfElement, NumberOfEdge = map(int, input().split())
Elements = [i for i in range(NumberOfElement+1)]
Cycle = False

for i in range(NumberOfEdge):
    FirstNode, SecondNode = map(int, input().split())
    # 사이클 판별 (FirstNode와 SecondNode의 속해있는 집합이 같음)
    if FindParent(Elements, FirstNode) == FindParent(Elements, SecondNode):
        Cycle = True
        break
    else:
        UnionParent(Elements, FirstNode, SecondNode)

print(Cycle)

"""
input
3 3
1 2
1 3
2 3
"""
"""
output
True
"""


