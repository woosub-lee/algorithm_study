import sys
input = sys.stdin.readline
print = sys.stdout.write
numberCount, targetCount = map(int, input().rstrip().split())
targetCount -= numberCount
numbers = list(input().rstrip().split())
result = ""
numbers = sorted(numbers, reverse=True)
for i in range(numberCount):
    if int(result+numbers[i]) > int(numbers[i]+result):
        result = result + numbers[i]
    else:
        result = numbers[i] + result
numbers = sorted(numbers, key=lambda x: (-1*len(x), -1*int(x)))
for i in range(targetCount):
    if int(result+numbers[0]) > int(numbers[0]+result):
        result = result + numbers[0]
    else:
        result = numbers[0] + result
print(result)