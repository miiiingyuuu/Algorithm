import sys
from collections import deque

input = sys.stdin.readline

'''
껍질을 벗기듯이 각각 껍질들끼리만 숫자를 바꿔주면 되는 형태
각 껍질을 따로 1차원 배열로 추출하여 회전한 후, 다시 2차원 배열 형태로 만들기
'''


def solve(arr):
    layers = min(n, m) // 2

    for l in range(layers):
        q = deque()

        # 각 껍질의 요소를 큐에 넣기(위, 오른쪽, 아래, 왼쪽 순)
        for i in range(l, m - l):   # 위쪽
            q.append(arr[l][i])
        for i in range(l + 1, n - l - 1):   # 오른쪽
            q.append(arr[i][m - l - 1])
        for i in range(m - l - 1, l - 1, -1):   # 아래쪽
            q.append(arr[n - l - 1][i])
        for i in range(n - l - 2, l, -1):   # 왼쪽
            q.append(arr[i][l])

        q.rotate(-r)

        # 회전 후 arr에 다시 해당 값 넣기
        for i in range(l, m - l):   # 위쪽
            arr[l][i] = q.popleft()
        for i in range(l + 1, n - l - 1):   # 오른쪽
            arr[i][m - l - 1] = q.popleft()
        for i in range(m - l - 1, l - 1, -1):   # 아래쪽
            arr[n - l - 1][i] = q.popleft()
        for i in range(n - l - 2, l, -1):   # 왼쪽
            arr[i][l] = q.popleft()

    return arr


n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

solve(arr)

for row in arr:
    print(*row)
