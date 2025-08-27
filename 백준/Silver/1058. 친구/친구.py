import sys

input = sys.stdin.readline


N = int(input())
friends = [input().strip() for _ in range(N)]

ans = 0

for i in range(N):
    visited = [False] * N   # i의 2-친구 체크
    for j in range(N):
        if i == j:
            continue

        if friends[i][j] == 'Y':
            visited[j] = True
        else:
            # 중간에 k를 통해 연결되어 있는 경우
            for k in range(N):
                if friends[i][k] == 'Y' and friends[k][j] == 'Y':
                    visited[j] = True
                    break

    ans = max(ans, sum(visited))

print(ans)
