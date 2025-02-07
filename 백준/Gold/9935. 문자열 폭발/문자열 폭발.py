import sys

input = sys.stdin.readline

words = input().strip()
N = len(words)
bomb_word = input().strip()
M = len(bomb_word)

stack = []
for i in range(N):
    stack.append(words[i])
    if ''.join(stack[-M:]) == bomb_word:
        for _ in range(M):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')
