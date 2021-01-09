n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))


def dfs(y, x):
    if y == -1 or y == n or x == -1 or x == m:
        return False
    if graph[y][x] == 0:
        graph[y][x] = 1
        dfs(y-1, x)
        dfs(y+1, x)
        dfs(y, x-1)
        dfs(y, x+1)
        return True
    return False


result = 0
for y in range(n):
    for x in range(m):
        if dfs(y, x) == True:
            result += 1

print(result)
