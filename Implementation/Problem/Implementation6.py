# 문자열 재정렬
# 알파벳 대문자와 숫자로만 이루어진 입력
# 알파벳 순으로 정렬 후 숫자는 모두더해서 출력
from collections import deque
Data = deque(list(input()))
Number = [str(i) for i in range(10)]
NumberSum = 0
for i in range(len(Data)):
    data = Data.popleft()
    if data in Number:
        NumberSum += int(data)
    else:
        Data.append(data)
Data = sorted(Data)
result = "".join(Data) + str(NumberSum)
print(result)
