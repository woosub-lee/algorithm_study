# 좌표 압축
# 외부에서 입력을 제공받음 (https://www.acmicpc.net/problem/18870 참고)
"""
실수했던 점: 성공적으로 구현함

기억해야할 점: 딕셔너리로 position을 표현할 수 있었음.
"""
import sys
numberOfPositions = int(sys.stdin.readline().rstrip())
positions = list(map(int, sys.stdin.readline().rstrip().split()))
sortedPositions = sorted(set(positions))
indexOfPositions = {}
for i in range(len(sortedPositions)):
    indexOfPositions[sortedPositions[i]] = i
for position in positions:
    sys.stdout.write(str(indexOfPositions[position])+' ')



