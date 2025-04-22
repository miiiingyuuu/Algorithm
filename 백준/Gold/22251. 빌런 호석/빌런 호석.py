import sys

input = sys.stdin.readline


n, k, p, x = map(int, input().split())  # n: 층수, k: 자리 수, p: 반전시킬 수, x: 멈춰 있는 층

# 숫자 표현 0~9 이진수 표현
led = [0b1111110, 0b0110000, 0b1101101, 0b1111001, 0b0110011, 0b1011011, 0b1011111, 0b1110000, 0b1111111, 0b1111011]

# 현재 층의 K자리 표현
x_str = str(x).zfill(k)
cnt = 0

for i in range(1, n+1):
    if i == x:
        continue
    # i층을 K자리로 표현할때, 뒤집히는 갯수의 합을 세기
    i_str = str(i).zfill(k)
    flips = sum(bin(led[int(x_str[j])] ^ led[int(i_str[j])]).count('1') for j in range(k))
    if 1 <= flips <= p:
        cnt += 1

print(cnt)