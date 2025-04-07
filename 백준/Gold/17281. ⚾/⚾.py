import sys
from itertools import permutations
input = sys.stdin.readline


def solve():
    max_score = 0

    players = [i for i in range(1, 9)]

    for perm in permutations(players):
        lineup = list(perm[:3]) + [0] + list(perm[3:])

        score = 0
        hitter_idx = 0

        for inning in innings:
            b1, b2, b3 = 0, 0, 0 # 1, 2, 3루 주자
            out_cnt = 0

            while out_cnt < 3:
                result = inning[lineup[hitter_idx]]
                hitter_idx = (hitter_idx + 1) % 9

                if result == 0:
                    out_cnt += 1
                elif result == 1:
                    score += b3
                    b1, b2, b3 = 1, b1, b2
                elif result == 2:
                    score += b2 + b3
                    b1, b2, b3 = 0, 1, b1
                elif result == 3:
                    score += b1 + b2 + b3
                    b1, b2, b3 = 0, 0, 1
                elif result == 4:
                    score += b1 + b2 + b3 + 1
                    b1, b2, b3 = 0, 0, 0

        max_score = max(max_score, score)

    return max_score


n = int(input())
innings = [list(map(int, input().split())) for _ in range(n)]

print(solve())