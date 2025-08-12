import sys

input = sys.stdin.readline


def solve_sung(sung_money):
    sung = 0

    # 성민이 계산
    up_cnt = 0
    down_cnt = 0
    for i in range(1, len(data)):
        if data[i] > data[i - 1]:
            up_cnt += 1
            down_cnt = 0
        elif data[i] < data[i - 1]:
            down_cnt += 1
            up_cnt = 0
        else:
            up_cnt = down_cnt = 0

        # 3일 연속 상승: 매도
        if up_cnt >= 3 and sung > 0:
            sung_money += sung * data[i]
            sung = 0

        # 3일 연속 하락: 매수
        if down_cnt >= 3 and sung_money >= data[i]:
            buy = sung_money // data[i]
            sung += buy
            sung_money -= buy * data[i]

    return sung_money + sung * data[-1]


def solve_jun(jun_money):
    jun = 0

    # 준현이 계산
    for i in data:
        if jun_money >= i:
            buy = jun_money // i
            jun += buy
            jun_money -= buy * i

    return jun_money + jun * data[-1]


N = int(input())
data = list(map(int, input().split()))

j_ans = solve_jun(N)
s_ans = solve_sung(N)

if j_ans > s_ans:
    print("BNP")
elif j_ans < s_ans:
    print("TIMING")
else:
    print("SAMESAME")
