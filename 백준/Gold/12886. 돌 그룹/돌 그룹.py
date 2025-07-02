import sys
from collections import deque

input = sys.stdin.readline

'''
문제에서 작은 수를 x, 큰 수를 y라고 했을때 모든 그룹 a, b, c의 돌의 갯수를 같게 하려고 함
x+x, y-x를 하면서 옮기는건데, 사실상 갯수가 많은 돌에서 작은돌의 갯수만큼 옮긴다는 생각을 하면 될듯
돌의 수는 실제로 변하지 않으니까, a+b+c가 3으로 나눠지지 않으면 애초에 답이 성립이 안되고, 나머지 경우를 bfs를 통해 경우를 구해 나눠지면 1을 출력 
'''


def solve(a, b, c):
    sum_val = a + b + c

    if sum_val % 3 != 0:
        return 0

    # visited[x][y] = x와 y를 비교 했는지 체크하기 위한 2차원 배열
    visited = [[False] * sum_val for _ in range(sum_val)]

    q = deque()
    a, b, c = sorted([a, b, c])
    q.append((a, b))
    visited[a][b] = True

    while q:
        x, y = q.popleft()
        z = sum_val - x - y

        # 3개의 값이 같아졌다면 1 반환
        if x == y == z:
            return 1

        # 가능한 경우를 반복문을 돌며 값 정리하기
        for i, j in ((x, y), (x, z), (y, z)):
            if i == j:
                continue

            small, big = sorted([i, j])
            tmp_small = small + small
            tmp_big = big - small
            new_nums = sorted([tmp_small, tmp_big, sum_val - i - j])

            if not visited[new_nums[0]][new_nums[1]]:
                visited[new_nums[0]][new_nums[1]] = True
                q.append((new_nums[0], new_nums[1]))

    return 0


a, b, c = map(int, input().split())

print(solve(a, b, c))
