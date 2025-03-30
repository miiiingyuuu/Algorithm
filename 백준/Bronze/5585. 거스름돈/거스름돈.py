import sys

input = sys.stdin.readline


price = int(input())

change = 1000 - price

coins = [500, 100, 50, 10, 5, 1]

cnt = 0

for coin in coins:
    # 코인 갯수 세기
    coin_cnt = change // coin

    # 남은 거스름돈 계산
    change -= coin_cnt * coin

    # 총 필요한 코인 갯수 갱신
    cnt += coin_cnt

print(cnt)

