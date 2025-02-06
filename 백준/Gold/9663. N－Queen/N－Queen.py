import sys

input = sys.stdin.readline

def dfs(row):
    global cnt
    # 모든 행에 퀸을 배치했다면 해답 카운트 증가
    if row == N:
        cnt += 1
        return

    for i in range(N):
        # col[i]: i번째 열에 퀸이 없음
        # diag1[row+i]: 왼쪽 아래에서 오른쪽 위 방향 대각선에 퀸이 없음
        # diag2[row-i+N-1]: 왼쪽 위에서 오른쪽 아래 방향 대각선에 퀸이 없음
        if not col[i] and not diag1[row+i] and not diag2[row - i + N - 1]:
            # 현재 위치에 퀸 배치
            arr[row][i] = 1
            # 열과 대각선 방향 사용 체크
            col[i] = 1
            diag1[row + i] = 1
            diag2[row - i + N - 1] = 1
            # 다음 행으로 이동
            dfs(row + 1)
            # 백트래킹: 현재 위치의 퀸과 체크했던 것들을 해제
            arr[row][i] = 0
            col[i] = 0
            diag1[row + i] = 0
            diag2[row - i + N - 1] = 0


# N x N 체스판 크기 입력
N = int(input())
# 체스판 배열 초기화
arr = [[0] * N for _ in range(N)]
# 해답의 개수를 저장할 변수
cnt = 0
# 열 사용 여부를 체크하는 배열
col = [0] * N
# 대각선 방향 체크를 위한 배열 (왼쪽 아래 -> 오른쪽 위)
diag1 = [0] * (N * 2 - 1)
# 대각선 방향 체크를 위한 배열 (왼쪽 위 -> 오른쪽 아래)
diag2 = [0] * (N * 2 - 1)

dfs(0)  # 0행부터 시작
print(cnt)