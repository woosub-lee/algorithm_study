# 모험가 길드
# 공포심이 N인 모험가는 N명 이상과 팀을 이루어야함
# 그룹의 최댓값을 구하여라
numberOfExplorer = int(input())
fearOfExplorers = list(map(int, input().split()))
fearOfExplorers = sorted(fearOfExplorers)
numberOfGroup = 0
explorerEachParty = 0
for fear in fearOfExplorers:
    explorerEachParty += 1
    if explorerEachParty >= fear:
        numberOfGroup += 1
        explorerEachParty = 0
print(numberOfGroup)
