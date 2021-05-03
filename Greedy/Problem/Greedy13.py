import sys
from string import ascii_uppercase
input = sys.stdin.readline
temp = [str(_) for _ in range(10)]+list(ascii_uppercase)
dict36 = {temp[i]: i for i in range(36)}
zIncreasing10 = [0 for i in range(36)]
result10 = 0
result36 = ''
for i in range(int(input().rstrip())):
    number36 = input().rstrip()
    for j in range(len(number36)):
        now = 36**(len(number36)-j-1)
        result10 += dict36[number36[j]]*now
        zIncreasing10[dict36[number36[j]]] += (35-dict36[number36[j]]) * now
changeCount = int(input())
result10 += sum(sorted(zIncreasing10, reverse=True)[:changeCount])
while result10 > 35:
    result36 += temp[result10 % 36]
    result10 = result10 // 36
result36 = (result36+temp[result10])[::-1]
print(result36)
