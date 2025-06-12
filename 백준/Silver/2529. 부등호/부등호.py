import sys

input = sys.stdin.readline

'''
백트래킹으로 가능한 모든 조합의 숫자를 사용
결과에를 정렬 후 가장 큰 값과 가장 작은 값을 출력
'''


def check(a, b, sign):
    if sign == '<':
        return a < b
    else:
        return a > b


def solve(depth, path):
    if depth == k + 1:
        ans.append(''.join(map(str, path)))
        return

    for num in range(10):
        if not visited[num]:
            if depth == 0 or check(path[-1], num, signs[depth - 1]):
                visited[num] = True
                solve(depth + 1, path + [num])
                visited[num] = False


k = int(input())
signs = list(input().split())

ans = []
visited = [False] * 10

solve(0, [])

ans.sort()
print(ans[-1])
print(ans[0])
