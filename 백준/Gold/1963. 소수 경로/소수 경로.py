import sys
from collections import deque

input = sys.stdin.readline


'''
4자리의 소수를 에라토테네스의 체로 구하고
num1 -> num2로 가는데 걸리는 단계 수를 bfs를 통해 구하기
num1을 문자열 형태로 바꿔서 한 자리씩 바꿔보면서 소수가 되는지 확인하면서 최종적으로 변하기 까지의 cnt를 세기
'''


def solve(now, tar):
    # now와 tar이 처음부터 같은 경우
    if now == tar:
        return 0

    visited = {now}

    q = deque()
    q.append((now, 0))  # 시작 숫자, cnt

    while q:
        cur_num, cnt = q.popleft()

        # 숫자를 문자열로 변환하여 각 자리의 변경을 쉽게 하기
        str_cur_num = str(cur_num)

        # 4개의 자리수를 순회
        for i in range(4):
            # 0 ~ 9까지의 숫자로 시도
            for j in range(10):
                # 첫번째 자리가 0이 되는 경우는 4자리 숫자가 안됨
                if i == 0 and j == 0:
                    continue

                str_tmp_num = str_cur_num[:i] + str(j) + str_cur_num[i+1:]
                tmp_num = int(str_tmp_num)

                # 목표 숫자를 찾았으면 끝
                if tmp_num == tar:
                    return cnt + 1

                # tmp_num이 방문하지 않은 소수라면 큐에 추가
                if tmp_num in prime_set and tmp_num not in visited:
                    visited.add(tmp_num)
                    q.append((tmp_num, cnt + 1))

    return "Impossible"


t = int(input())

# 4자리(1000 ~ 9999 사이)의 소수 구하기
is_prime = [True] * 10000
is_prime[0] = is_prime[1] = False

for i in range(2, 100):
    if is_prime[i]:
        # i의 배수들을 소수에서 제외
        for j in range(i*i, 10000, i):
            is_prime[j] = False

prime_set = {i for i in range(1000, 10000) if is_prime[i]}

for _ in range(t):
    num1, num2 = map(int, input().split())
    print(solve(num1, num2))
