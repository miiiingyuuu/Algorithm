import sys

input = sys.stdin.readline
'''
꼭 팀의 수가 n/2가 될 필요가 없이 최소한의 실력차가 나오게 해야함
백트래킹으로 팀원의 수를 조절하며 최소값을 구하기
'''


def cal_stats():
    global ans
    s_team, l_team = 0, 0
    
    for i in range(n):
        for j in range(n):
            if visited[i] and visited[j]:
                s_team += stats[i][j]
            elif not visited[i] and not visited[j]:
                l_team += stats[i][j]

    ans = min(ans, abs(s_team - l_team))
    
    if ans == 0:
        print(0)
        sys.exit(0)


def solve(depth):
    if depth == n:
        cal_stats()
        return
    
    visited[depth] = True
    solve(depth + 1)
    visited[depth] = False
    solve(depth + 1)


n = int(input())
stats = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
ans = float('inf')

solve(0)

print(ans)