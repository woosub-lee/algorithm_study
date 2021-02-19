# 럭키 스트레이트
# 점수를 반으로 쪼개서 각 숫자의 합이 같으면 발동
# ex) 123,402 1+2+3 = 6, 4+0+2 = 6
CurrentScore = list(map(int, input()))
FrontSum = sum(CurrentScore[:len(CurrentScore)//2])
BackSum = sum(CurrentScore[len(CurrentScore)//2:])
if FrontSum == BackSum:
    print('LUCKY')
else:
    print('READY')

