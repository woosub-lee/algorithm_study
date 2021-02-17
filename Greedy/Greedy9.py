# 볼링공 고르기
# 두사람이 서로 다른 무게를 가진 볼링공을 고르기
# 고를 수 있는 경우의 수 구하기
NumberOfBall, MaximumWeight = map(int, input().split())
NumberOfCases = 0
Balls = list(map(int, input().split()))

for i in range(NumberOfBall-1):
    CurrentBall = Balls[i]
    for ball in Balls[i+1:]:
        if CurrentBall != ball:
            NumberOfCases += 1

print(NumberOfCases)

