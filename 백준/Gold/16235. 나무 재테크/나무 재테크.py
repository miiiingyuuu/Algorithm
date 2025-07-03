import sys
from collections import deque

input = sys.stdin.readline


'''
각 칸에 영양분의 양이 숫자로 나타나져 있고, 나무는 여러 그루일 수도 있음(처음엔 모두 5의 양분)
1. 봄: 나무가 자신의 나이만큼 양분을 먹는다. 두 그루 이상일때는 나이가 어린 나무부터 양분을 먹음(자신의 나이만큼 양분을 먹지 못하면 즉사), 이후 나이가 1 증가
2. 여름: 봄에 죽은 나무가 양분이 됨 -> 죽은 나무의 반이 칸의 양분으로 추가 됨(소수점 아래는 버림)
3. 가을: 나무의 나이가 5의 배수인 나무의 8방향에 나이가 1인 나무가 생김
4. 겨울: 각 칸에 input만큼 양분을 추가

봄에 양분을 주고 죽는게 결정이 나니까 봄 + 여름을 함께 묶어서 하나의 함수로 진행하고
가을과 겨울은 각각 하는 역할이 별개이므로 따로 해서 3개의 함수로 풀기
'''


def spring_and_summer():
    for i in range(n):
        for j in range(n):
            if trees[i][j]:
                survived = deque()
                dead_nutrient = 0

                # 봄: 어린 나무부터 양분을 섭취
                while trees[i][j]:
                    age = trees[i][j].popleft()
                    if land[i][j] >= age:
                        land[i][j] -= age
                        survived.append(age + 1)
                    else:
                        # 여름: 죽은 나무는 양분으로
                        dead_nutrient += age // 2

                trees[i][j] = survived
                land[i][j] += dead_nutrient


def fall():
    for i in range(n):
        for j in range(n):
            if trees[i][j]:
                for age in trees[i][j]:
                    if age % 5 == 0:
                        # 가을: 나이가 5의 배수인 나무가 8방향의 인접한 칸에 나이가 1인 나무가 추가로 생김
                        for di, dj in [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]:
                            ni = i + di
                            nj = j + dj
                            if 0 <= ni < n and 0 <= nj < n:
                                trees[ni][nj].appendleft(1)


def winter():
    for i in range(n):
        for j in range(n):
            # 겨울: input으로 받은 A만큼 양분 추가
            land[i][j] += A[i][j]


def solve():
    for year in range(k):
        spring_and_summer()
        fall()
        winter()

    ans = 0
    for i in range(n):
        for j in range(n):
            ans += len(trees[i][j])

    return ans


n, m, k = map(int, input().split())    # n: board 크기, m: 나무 개수, k: 년 수
A = [list(map(int, input().split())) for _ in range(n)] # 겨울에 추가할 양분에 대한 정보
land = [[5] * n for _ in range(n)]  # 초기 땅의 양분
trees = [[deque() for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, z = map(int, input().split()) # x, y: 나무의 위치, z: 해당 나무의 나이
    trees[x - 1][y - 1].append(z)

print(solve())
