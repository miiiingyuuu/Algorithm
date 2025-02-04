import sys

input = sys.stdin.readline

def make_stars(n):
    if n == 3:
        return ['  *  ', ' * * ', '*****']
    
    # 이전 패턴을 재귀적으로 생성
    stars = make_stars(n // 2)
    
    # 현재 패턴의 크기에 맞는 빈 배열 생성
    result = []
    
    # 이전 패턴의 위쪽 공백을 포함하여 추가
    for line in stars:
        result.append(' ' * (n // 2) + line + ' ' * (n // 2))
    
    # 이전 패턴을 좌우로 복사하여 추가
    for line in stars:
        result.append(line + ' ' + line)
    
    return result

def print_stars(n):
    result = make_stars(n)
    for line in result:
        print(line)

# 입력 받기
n = int(input())
print_stars(n)