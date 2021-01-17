# 두배열의 원소교체 (A배열의 합이 가장 크게)
n, k = map(int, input().split())
arrayA = list(map(int, input().split()))
arrayB = list(map(int, input().split()))
arrayA.sort(reverse=False)
arrayB.sort(reverse=True)
for i in range(k):
    if arrayA[i] < arrayB[i]:
        arrayA[i], arrayB[i] = arrayB[i], arrayA[i]
    else:
        break
print(sum(arrayA))
