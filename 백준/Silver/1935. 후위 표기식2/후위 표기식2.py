import sys

input = sys.stdin.readline


n = int(input())
sik = input().strip()

values = {}
for i in range(n):
    values[chr(65 + i)] = float(input())

stack = []
for char in sik:
    if 'A' <= char <= 'Z':
        stack.append(values[char])
    else:
        b = stack.pop()
        a = stack.pop()

        if char == '+':
            stack.append(a+b)
        elif char == '-':
            stack.append(a-b)
        elif char == '*':
            stack.append(a*b)
        elif char == '/':
            stack.append(a/b)

print(f'{stack[0]:.2f}')