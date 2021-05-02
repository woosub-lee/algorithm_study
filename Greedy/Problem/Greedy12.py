import sys
input = sys.stdin.readline
print = sys.stdout.write
numberCount, targetCount = map(int, input().rstrip().split())
numbers = []
result = ""
printValue = ""
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
        if int(numbers[j][0]) < int(numbers[j+1][0]):
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
        elif int(numbers[j][0]) == int(numbers[j+1][0]):
            if int(numbers[j][-1]) < int(numbers[j+1][-1]):
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
            elif int(numbers[j][-1]) == int(numbers[j+1][-1]):
                if int(numbers[j]) < int(numbers[j+1]):
                    numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
for i in range(targetCount):
    if int(result+numbers[i]) > int(numbers[i]+result):
        result = result + numbers[i]
    else:
        result = numbers[i] + result
print(result)