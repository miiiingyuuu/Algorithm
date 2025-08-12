import sys
from collections import deque

input = sys.stdin.readline

'''
첫자리 숫자가 1로 시작하고 0또는 1로만 구성된 숫자가 N으로 나눠떨어지면 해당 숫자가 답
숫자가 계속해서 커질 우려가 있으므로, N보다 작은 수의 나머지를 방문여부로 잡아서 해당 나머지가 발생한적이 있다면 패스
bfs로 순회하면서 찾으면 될듯
'''


def solve(num):
    visited = [False] * (num+1)
    q = deque()

    q.append(('1', 1 % num))  # 1로 시작, N으로 나눴을 때의 나머지(0이면 답)
    visited[1 % num] = True

    while q:
        now_str, rem = q.popleft()

        if rem == 0:
            return now_str

        # 0 추가 하는 경우
        next_rem = (rem * 10) % num
        if not visited[next_rem]:
            visited[next_rem] = True
            q.append((now_str + '0', next_rem))

        # 1 추가 하는 경우
        next_rem = (rem * 10 + 1) % num
        if not visited[next_rem]:
            visited[next_rem] = True
            q.append((now_str + '1', next_rem))

    return 'BRAK'


T = int(input())
for tc in range(T):
    N = int(input().strip())
    print(solve(N))
