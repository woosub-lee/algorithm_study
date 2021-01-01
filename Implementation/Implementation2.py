# 3이 하나라도 들어있는 시각 찾기
n = int(input())
result = 0
for hour in range(n+1):
    if '3' in str(hour):
        result += 3600
        continue
    for minute in range(60):
        if '3' in str(minute):
            result += 60
            continue
        for second in range(60):
            if '3' in str(second):
                result += 1
print(result)