import sys
from collections import deque

input = sys.stdin.readline

'''
1. 화면에 있는 이모티콘을 클립보드에 복사
2. 클립보드에 있는 이모티콘을 화면에 붙여넣기
3. 화면에 있는 이모티콘 중 하나를 삭제
화면의 이모티콘 개수, 클립보드 이모티콘 개수, 연산횟수를 q에 담아서 bfs를 진행
'''


def solve():
    visited = [[False] * (s + 1) for _ in range(s + 1)]  # visited[i][j] - i: 화면 이모티콘 개수, j: 클립보드 이모티콘 개수
    q = deque()
    q.append((1, 0, 0))  # 화면 이모티콘 개수, 클립보드 이모티콘 개수, time
    visited[1][0] = True

    while q:
        screen, clipboard, ans = q.popleft()

        if screen == s:
            return ans

        # 클립보드에 복사
        if not visited[screen][screen]:
            visited[screen][screen] = True
            q.append((screen, screen, ans + 1))

        # 클립보드의 이모티콘을 화면에 붙여넣기
        if clipboard > 0 and screen + clipboard <= s and not visited[screen + clipboard][clipboard]:
            visited[screen + clipboard][clipboard] = True
            q.append((screen + clipboard, clipboard, ans + 1))

        # 화면에서 이모티콘 하나 삭제
        if screen > 1 and not visited[screen - 1][clipboard]:
            visited[screen - 1][clipboard] = True
            q.append((screen - 1, clipboard, ans + 1))


s = int(input())

print(solve())
