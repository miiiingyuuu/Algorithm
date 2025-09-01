import sys

input = sys.stdin.readline


'''
1. 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리 정하기
2. 1을 만족하는 칸이 여러 개면, 인접한 칸에서 비어있는 칸이 가장 많은 칸으로 자리 정하기
3. 2를 만족하는 칸이 여러 개면, 행의 번호가 가장 작은 칸, 그러한 칸도 여러개면 열의 번호가 가장 작은 칸으로 자리 정하기
'''

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 자리 배치하기
def solve(board):
    for student in students:
        candidates = []

        for x in range(N):
            for y in range(N):
                if board[x][y] != 0:
                    continue

                like_cnt = 0    # 인접한 좋아하는 학생 수
                empty_cnt = 0   # 인접한 빈 자리 수

                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < N and 0 <= ny < N:
                        if board[nx][ny] in likes[student]:
                            like_cnt += 1
                        elif board[nx][ny] == 0:
                            empty_cnt += 1

                # 조건: 좋아하는 학생 수, 빈자리 수, 행, 열
                candidates.append((like_cnt, empty_cnt, x, y))

        # 1번 조건인 좋아하는 학생 수가 내림차순으로 정렬: 많은 사람부터 자리에 놓아야 함
        candidates.sort(reverse=True)
        _, _, x, y = candidates[0]
        board[x][y] = student


N = int(input())
board = [[0] * N for _ in range(N)]
students = []   # 학생번호
likes = dict()  # 그 학생이 좋아하는 학생 4명

for _ in range(N**2):
    data = list(map(int, input().split()))
    student, lst = data[0], data[1:]
    students.append(student)
    likes[student] = lst

# 1. 조건에 맞게 자리 배치하기
solve(board)

# 2. 만족도 계산
satisfaction = 0
score = [0, 1, 10, 100, 1000]   # 0, 1, 2, 3, 4

for x in range(N):
    for y in range(N):
        student = board[x][y]
        like_cnt = 0
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] in likes[student]:
                    like_cnt += 1

        satisfaction += score[like_cnt]

print(satisfaction)
