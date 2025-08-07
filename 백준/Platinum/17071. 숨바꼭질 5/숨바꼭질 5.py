import sys
from collections import deque

input = sys.stdin.readline

'''
수빈이: 1초 -> x-1 or x+1 이동, 순간이동: 2*x
동생: 매 초마다 가속이 붙어 K + time 만큼 증가
방문 여부 확인은 여동생이 지나간 자리와 수빈이가 지나간 자리를 같이 확인해야 하는 듯
-> 이렇게 하니까 시간 초과 발생: 해당 시간 안에 도착하는지 궁금한거니까, 짝수 시간에 도착했는지, 홀수 시간에 도착했는지로 방문 여부 판별
'''


def solve():
    visited = [[False, False] for _ in range(end)]
    visited[N][0] = True  # visited[cur][time]: 동생의 현재 위치에 0(짝수) or 1(홀수) 시간에 도착했는지 판별

    q = deque()
    q.append((N, 0))  # 수빈이 위치, 시간

    while q:
        subin, time = q.popleft()

        sister = K + time * (time + 1) // 2  # time까지 증가하는 등차수열의 합

        if sister >= end:
            return -1
        if visited[sister][time % 2]:
            return time

        # 뒤로 한 칸 가는 경우, 앞으로 가는 경우, 순간이동 하는 경우
        for next_pos in (subin - 1, subin + 1, subin * 2):
            if 0 <= next_pos < end and not visited[next_pos][(time + 1) % 2]:
                visited[next_pos][(time + 1) % 2] = True
                q.append((next_pos, time + 1))

    return -1


N, K = map(int, input().split())
end = 500001

print(solve())
