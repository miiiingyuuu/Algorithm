import sys

input = sys.stdin.readline

'''
order의 숫자를 하나씩 가져와서 stack에 해당 노드와 연결된 노드가 있다면 pop을 해주고 stack에 추가
stack에서 pop을 시키면서 모든 요소가 pop이 되었는데, 연결된 다음 노드가 없다는 것은 dfs 탐색한 순서가 틀렸다는 것
'''


def solve():
    if order[0] != 1:
        return 0

    stack = [order[0]]

    for i in range(1, n):
        tmp_val = order[i]
        while stack and tmp_val not in graph[stack[-1]]:
            stack.pop()
            if not stack:
                return 0

        stack.append(tmp_val)

    return 1


n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

order = list(map(int, input().split()))

print(solve())
