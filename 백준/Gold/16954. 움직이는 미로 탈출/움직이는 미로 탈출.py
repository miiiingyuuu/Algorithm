import sys
from collections import deque

input = sys.stdin.readline


'''
벽이 행 아래로 계속 내려가면서 범위에서 벗어나면 벽이 없어지는 게임에서 왼쪽 제일 아래에서 시작해서 오른쪽 위로 가야함
움직이는 방향은 그러면 위, 오른쪽 위, 오른쪽이 최선의 움직임? -> 인줄 알았는데 최소거리를 따지기 보다는 어떻게든 그냥 탈출하면 되서 8방향 보는게 맞다.
벽만 없다면 계속해서 자유롭게 이동해서 오른쪽 위에만 도착하면 되기 때문에 방문여부를 딱히 체크할 필요가 없는 것 같다.
다음 1초 동안 일어나는 일의 순서
1. 캐릭터가 먼저 움직임(가만히 있을 수도 있음)
2. 벽이 행 아래로 움직임
3. 벽이랑 캐릭터가 부딪히면 더 이상 캐릭터는 움직일 수 없음(0)
'''


def solve():
    visited = [[False] * 8 for _ in range(8)]

    q = deque()
    q.append((7, 0))

    while q:
        # 현재 시간에 탐색해야 할 위치의 수
        q_size = len(q)

        for _ in range(q_size):
            x, y = q.popleft()
            # 기저 조건: 오른쪽 끝에 도달 했을 경우
            if x == 0 and y == 7:
                return 1

            # 1. 사람이 먼저 이동 (9방향)
            for d in range(9):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < 8 and 0 <= ny < 8 and board[nx][ny] != '#' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))

        # 2. 벽이 행 아래로 이동
        # 맨 아랫줄이 사라지고 맨 윗줄은 빈칸을 추가함으로써 행이 아래로 움직였음을 표시
        board.pop()
        board.insert(0, list('........'))

        # 3. 캐릭터가 움직일 수 있는 장소 방문 여부 조정 및 벽과 사람이 만났는지 확인
        # 벽과 충돌한 요소들은 제거
        q = deque([(x, y) for x, y in q if board[x][y] == '.'])

        # 어떻게든 목적지에만 도착하면 되므로 방문여부를 다시 초기화
        visited = [[False] * 8 for _ in range(8)]

    return 0


board = [list(input().strip()) for _ in range(8)]

# 캐릭터가 움직이는 방향(좌상, 상, 우상, 좌, 중앙, 우, 좌하, 하, 우하)
dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]

print(solve())
