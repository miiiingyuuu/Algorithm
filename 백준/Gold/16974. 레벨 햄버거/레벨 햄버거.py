import sys

input = sys.stdin.readline


'''
레벨 L의 버거에서 아래 X장을 먹었을 때, 먹은 패티는 몇 장?
0: P(1, 1), 1: BPPPB(5, 2+1), 2: B BPPPB P BPPPB B(13, 6+1), 3: B B BPPPB P BPPPB B P B BPPPB P BPPPB B B(29, 14+1)
4: B B B BPPPB P BPPPB B P BPPPB P BPPPB B B P B B BPPPB P BPPPB B P BPPPB P BPPPB B B B
층 개수: (i-1)*2+3, 패티 개수: (i-1)*2+1
'''


def solve(level, tar):
    # 0층 버거 일 경우 패티 1장을 먹는 경우 밖에 없음
    if level == 0:
        return 1 if tar == 1 else 0

    # 먹으려는 패티가 0장이면 반드시 0
    if tar == 0:
        return 0

    # 아래 중에 해당되는 경우에 재귀적으로 더 들어가기
    # 먹으려는 층의 수가 이전 층보다 작을 경우, 재귀적으로 더 들어가기
    elif tar <= 1 + total_layers[level - 1]:
        return solve(level - 1, tar - 1)    # 가장 아래 B 먹고, 해당 층에서 패티 개수 해결
    # 먹으려는 층의 수 + 1이 이전 층의 수 + 2와 동일하다면, 이전 층의 패티 수 + 1를 반환
    elif tar == 1 + total_layers[level - 1] + 1:
        return total_patties[level - 1] + 1 # 가운데 패티 + 이전 층의 패티 수를 반환
    # 먹으려는 층의 수가 (이전 층 * 2) - 1보다 작다면
    elif tar <= 1 + total_layers[level - 1] + 1 + total_layers[level - 1]:
        return total_patties[level - 1] + 1 + solve(level - 1, tar - (2 + total_layers[level - 1]))
    else:
        return total_patties[level]


l, x = map(int, input().split())

# 각 층의 층 수와 패티 수를 계산하여 저장
total_layers = [0] * (l + 1)
total_patties = [0] * (l + 1)

# 0레벨 버거는 1층에 패티 1장
total_layers[0] = 1
total_patties[0] = 1

for i in range(1, l + 1):
    total_layers[i] = 2 * total_layers[i-1] + 3
    total_patties[i] = 2 * total_patties[i-1] + 1

print(solve(l, x))
