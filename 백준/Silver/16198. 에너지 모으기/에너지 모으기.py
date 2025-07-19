import sys

input = sys.stdin.readline

'''
N개의 에너지 구슬이 주어졌을 때, 모을 수 있는 에너지의 최대값을 계산
'''


def solve(cur_weights, cur_energy):
    global max_energy

    if len(cur_weights) == 2:
        if cur_energy > max_energy:
            max_energy = cur_energy
        return

    for i in range(1, len(cur_weights) - 1):
        # i번째 구슬을 제거하여 얻는 에너지 계산
        energy_to_add = cur_weights[i - 1] * cur_weights[i + 1]

        # i번째 구슬을 제외한 새로운 리스트 생성
        next_weights = cur_weights[:i] + cur_weights[i + 1:]

        # 재귀 호출
        solve(next_weights, cur_energy + energy_to_add)


n = int(input())
weights = list(map(int, input().split()))

max_energy = 0

solve(weights, 0)

print(max_energy)
