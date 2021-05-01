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
numbers = sorted(numbers + [maxValue for i in range(targetCount-numberCount)], reverse=True)
for i in range(targetCount):
    print(numbers[i] + ' ')
print('\n')
for i in range(targetCount):
    if int(result+numbers[i]) > int(numbers[i]+result):
        result = result + numbers[i]
        printValue = printValue + ' ' + numbers[i]
    else:
        result = numbers[i] + result
        printValue = numbers[i] + ' ' + printValue
print(printValue+'\n')
print(result)