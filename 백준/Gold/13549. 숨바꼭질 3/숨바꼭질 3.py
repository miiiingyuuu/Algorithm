from collections import deque

def find_min_time(N, K):
    max_pos = 100001  # 최대 위치 제한
    visited = [False] * max_pos
    times = [-1] * max_pos

    q = deque([(N, 0)])  # (위치, 시간)
    visited[N] = True
    times[N] = 0

    while q:
        pos, time = q.popleft()

        if pos == K:  # 목표 지점 도달
            return time

        # 순간이동 (2*X) - 0초 소요되므로 먼저 처리
        if pos * 2 < max_pos and not visited[pos * 2]:
            visited[pos * 2] = True
            times[pos * 2] = time
            q.appendleft((pos * 2, time))  # 우선순위가 높으므로 앞쪽에 추가

        # 걷기 (X-1, X+1) - 1초 소요
        for next_pos in (pos - 1, pos + 1):
            if 0 <= next_pos < max_pos and not visited[next_pos]:
                visited[next_pos] = True
                times[next_pos] = time + 1
                q.append((next_pos, time + 1))

    return -1  # 도달할 수 없는 경우

# 입력 받기
N, K = map(int, input().split())
print(find_min_time(N, K))
