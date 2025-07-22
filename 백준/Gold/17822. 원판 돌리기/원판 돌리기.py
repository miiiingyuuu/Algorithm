import sys
from collections import deque

input = sys.stdin.readline


'''
회전하는 함수 1개 만들고,
회전을 완료한 원판에서 인접한 숫자가 있는지 확인하는 함수 1개
해당 원판의 평균을 구하고, 그 평균보다 큰 수에서 -1, 작은 수는 +1
'''


def check(graph):
    to_delete = set()
    for i in range(1, n+1):
        for j in range(m):
            cur_val = graph[i][j]
            if cur_val == 0:
                continue

            # 같은 원판에서 양 옆을 확인
            for dj in [-1, 1]:
                nj = (j + dj) % m
                if graph[i][nj] == cur_val:
                    to_delete.add((i, j))
                    to_delete.add((i, nj))

            # 위아래 원판 확인
            for di in [-1, 1]:
                ni = i + di
                if 1 <= ni <= n:
                    if graph[ni][j] == cur_val:
                        to_delete.add((i, j))
                        to_delete.add((ni, j))

    # 지울게 있다면 0으로 만들기
    if to_delete:
        for x, y in to_delete:
            graph[x][y] = 0
        return True
    else:
        # 인접한 수가 없으면 평균 계산 후 조정
        total = 0
        cnt = 0
        for i in range(1, n+1):
            for j in range(m):
                if graph[i][j] != 0:
                    total += graph[i][j]
                    cnt += 1

        if cnt == 0:
            return False

        avg = total / cnt

        for i in range(1, n+1):
            for j in range(m):
                if graph[i][j] == 0:
                    continue
                if graph[i][j] > avg:
                    graph[i][j] -= 1
                elif graph[i][j] < avg:
                    graph[i][j] += 1

        return False


def graph_rotate(tar, direction, num, cur_graph):
    for idx in range(1, n+1):
        if idx % tar == 0:
            if direction == 0:
                cur_graph[idx].rotate(num)
            else:
                cur_graph[idx].rotate(-num)

    return cur_graph


n, m, t = map(int, input().split())
graph = [deque() for _ in range(n+1)]
for i in range(1, n+1):
    nums = list(map(int, input().split()))
    graph[i].extend(nums)

for _ in range(t):
    x, d, k = map(int, input().split()) # x의 배수인 원판, d(0: 시계, 1: 반시계), k칸 회전
    graph_rotate(x, d, k, graph)
    check(graph)

ans = 0
for i in range(1, n+1):
    ans += sum(graph[i])

print(ans)
