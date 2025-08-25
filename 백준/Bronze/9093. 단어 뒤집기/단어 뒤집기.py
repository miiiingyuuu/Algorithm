import sys

input = sys.stdin.readline


T = int(input())
for _ in range(T):
    stnc = list(input().split())
    ans = []
    for word in stnc:
        reversed_word = ''.join(reversed(word))
        ans.append(reversed_word)

    print(*ans)