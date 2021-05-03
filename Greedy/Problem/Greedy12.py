import sys
input = sys.stdin.readline
print = sys.stdout.write
numberCount, targetCount = map(int, input().rstrip().split())
numbers = []
result = ""
maxValue = "0"
for i in range(numberCount):
    isBigger = False
    numbers.append(input().rstrip())
    if len(numbers[i]) > len(maxValue):
        isBigger = True
    elif len(numbers[i]) == len(maxValue):
        if int(numbers[i]) > int(maxValue):
            isBigger = True
    if isBigger:
        maxValue = numbers[i]
numbers = numbers + [maxValue for i in range(targetCount-numberCount)]
for i in range(targetCount-1, 0, -1):
    for j in range(i):
        if int(numbers[j]+numbers[j+1]) < int(numbers[j+1]+numbers[j]):
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
for i in range(targetCount):
    result = result + numbers[i]
print(result)