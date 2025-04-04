import sys

input = sys.stdin.readline


n = int(input())
players = list(map(int, input().split()))

scores = [0] * n

card_to_idx = {}
for i, card in enumerate(players):
    card_to_idx[card] = i

for i, card in enumerate(players):
    for divisor in range(1, int(card**0.5) + 1):
        if card % divisor == 0:
            if divisor in card_to_idx:
                j = card_to_idx[divisor]
                scores[j] += 1
                scores[i] -= 1

            other_divisor = card // divisor
            if other_divisor != divisor and other_divisor in card_to_idx:
                j = card_to_idx[other_divisor]
                scores[j] += 1
                scores[i] -= 1

print(*scores)