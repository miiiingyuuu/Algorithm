import sys
from collections import deque
input = sys.stdin.readline


def solve():
    visited = [False] * (f+1)
    q = deque()
    q.append((s, 0))
    visited[s] = True

    while q:
        now, cnt = q.popleft()

        if now == g:
            return cnt

        # 방문 여부를 확인하여 u만큼 올라가고, d만큼 내려가는 경우로 나눠서 최소 횟수 알아내기
        for nf in (now + u, now - d):
            if 1 <= nf <= f and not visited[nf]:
                visited[nf] = True
                q.append((nf, cnt + 1))

    return "use the stairs"


f, s, g, u, d = map(int, input().split())   # f: 층 수, s: 현재 위치, g: 목표, u: 위로 u, d: 아래로 d

print(solve())