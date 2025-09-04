# 보기에서 주어진 행렬의 번호 값을 잘 확인해야함

N = int(input())
arr = [[0]*1001 for _ in range(1001)]
for n in range(1, N+1):
    sj, si, w, h = map(int, input().split())
    for i in range(si, si+h):
        for j in range(sj, sj+w):
            arr[i][j] = n

ans = [0] * (N+1)
for lst in arr:
    for i in lst:
        ans[i] += 1
print(*ans[1:], end='')