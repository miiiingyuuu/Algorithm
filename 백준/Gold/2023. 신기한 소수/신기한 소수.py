import sys

input = sys.stdin.readline


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def solve(number, digit):
    if digit == N:
        return print(number)

    for next_digit in range(10):
        next_num = number * 10 + next_digit
        if is_prime(next_num):
            solve(next_num, digit + 1)


N = int(input().strip())
for number in [2, 3, 5, 7]:
    solve(number, 1)