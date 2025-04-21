import sys

input = sys.stdin.readline


def solve():
    result = []

    def dfs(start, current, visited, path):
        visited[current] = True
        path.append(current)
        next_node = lst[current]

        if not visited[next_node]:
            dfs(start, next_node, visited, path)
        elif next_node in path:
            cycle_start = path.index(next_node)
            result.extend(path[cycle_start:])

    for i in range(1, n+1):
        visited = [False] * (n+1)
        path = []
        dfs(i, i, visited, path)

    result = sorted(set(result))

    return result


n = int(input())
lst = [0]
for _ in range(n):
    lst.append(int(input()))

ans = solve()

print(len(ans))
for num in ans:
    print(num)