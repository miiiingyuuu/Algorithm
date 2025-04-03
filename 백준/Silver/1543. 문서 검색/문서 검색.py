import sys

input = sys.stdin.readline


word = list(input().rstrip())
tar = list(input().rstrip())

cnt = 0
now = 0

while now < len(word):
    if word[now:now+len(tar)] == tar:
        now += len(tar)
        cnt += 1
    else:
        now += 1

print(cnt)