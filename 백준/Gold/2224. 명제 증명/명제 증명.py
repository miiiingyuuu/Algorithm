import sys

input = sys.stdin.readline


def change(c):
    if 'A' <= c <= 'Z':
        return ord(c) - ord('A')
    else:
        return 26 + (ord(c) - ord('a'))


def change_reverse(i):
    if i < 26:
        return chr(ord('A') + i)
    else:
        return chr(ord('a') + (i - 26))


N = int(input())
possible = [[False] * 52 for _ in range(52)]

for _ in range(N):
    P, _, Q = input().split()
    u, v = change(P), change(Q)
    possible[u][v] = True

# 플로이드-워셜로 알아보기
for k in range(52):
    for i in range(52):
        if possible[i][k]:
            for j in range(52):
                if possible[k][j]:
                    possible[i][j] = True

results = []
for i in range(52):
    for j in range(52):
        if i != j and possible[i][j]:
            results.append(f"{change_reverse(i)} => {change_reverse(j)}")

results.sort()

print(len(results))
print("\n".join(results))
