import sys
from collections import deque

input = sys.stdin.readline

'''
s를 t가 되는 최소 연산 수
가능한 경우가 여러개라면, 사전 순으로 앞서는 것을 출력 (* > + > - > /)
처음에는 경우를 모두 구하고 정렬해서 구해야되나 생각했는데, 그냥 사전 순으로 차례대로 bfs를 하면 당연히 가장 먼저 나오는 답이 사전순으로 가장 빠르게 나온 답
'''


def solve():
    visited = set([s])

    q = deque()
    q.append((s, ""))   # now, 기호들

    ops = [
        ('*', lambda x: x * x),
        ('+', lambda x: x + x),
        ('-', lambda x: 0),
        ('/', lambda x: 1 if x != 0 else None)  # 0이 아니라면 자기 자신으로 나누므로, 계속 1이 나옴
    ]

    while q:
        now, path = q.popleft()

        for ops_char, ops_func in ops:
            ops_func_now = ops_func(now)

            # 사용할 수 없는 연산이거나 sik이 None이라면 패스
            if ops_func_now is None:
                continue

            # 0 상태는 연산에 의미가 없음
            if ops_func_now == 0:
                continue

            # t보다 크고 1도 아닐 때는 연산 의미 없음
            if ops_func_now > t:
                continue

            if ops_func_now in visited:
                continue

            next_path = path + ops_char

            if ops_func_now == t:
                return next_path

            visited.add(ops_func_now)
            q.append((ops_func_now, next_path))

    return -1


s, t = map(int, input().split())

if s == t:
    print(0)
    sys.exit()

print(solve())
