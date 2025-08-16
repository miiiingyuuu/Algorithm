import sys

input = sys.stdin.readline


def solve():
    ans = float('inf')

    for u in range(1, N+1):
        for v in graph[u]:
            # 작은 친구 수 기준으로 찾기
            x, y = u, v
            if friends_cnt[u] > friends_cnt[v]:
                x, y = y, x

            for w in graph[x]:
                if w in graph[y]:
                    # 3명이 공통 친구라면 친구수가 최소값이 될 것(서로 중복되는 2명 * 3을 빼기)
                    tmp = friends_cnt[x] + friends_cnt[y] + friends_cnt[w] - 6
                    ans = min(ans, tmp)

    return ans if ans != float('inf') else -1


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
friends_cnt = [0] * (N+1)

# 그래프와 친구 수 입력
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    friends_cnt[a] += 1
    friends_cnt[b] += 1

# 집합으로 변환시키기
for i in range(1, N+1):
    graph[i] = set(graph[i])

print(solve())
