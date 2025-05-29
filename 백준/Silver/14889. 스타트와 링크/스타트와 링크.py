import sys
from itertools import combinations
input = sys.stdin.readline


def cal_ability(team):
    ability = 0
    for i in range(len(team)):
        for j in range(i+1, len(team)):
            ability += board[team[i]][team[j]] + board[team[j]][team[i]]

    return ability


def solve():
    ans = float('inf')
    people = list(range(n)) # 사람을 반으로 나누기 위해 people 만들기

    # 조합으로 가능한 경우의 수를 팀으로 나눠 ability 차이의 최솟값 찾기
    for s_team in combinations(people, n // 2):
        l_team = list(set(people) - set(s_team))  # 팀 나누기
        s_ability = cal_ability(s_team)
        l_ability = cal_ability(l_team)

        diff = abs(s_ability - l_ability)

        ans = min(ans, diff)
        # 차이가 0인게 제일 낮은 값이므로 0이 나오면 바로 break
        if ans == 0:
            break

    return ans


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

print(solve())