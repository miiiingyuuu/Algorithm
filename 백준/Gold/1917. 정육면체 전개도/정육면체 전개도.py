import sys

input = sys.stdin.readline

# 정육면체 전개도는 총 11가지 (정확한 패턴)
cubes = [
    [[1, 0, 0, 0],
     [1, 1, 1, 1],
     [1, 0, 0, 0]],
    [[0, 1, 0, 0],
     [1, 1, 1, 1],
     [1, 0, 0, 0]],
    [[0, 0, 1, 0],
     [1, 1, 1, 1],
     [1, 0, 0, 0]],
    [[0, 0, 0, 1],
     [1, 1, 1, 1],
     [1, 0, 0, 0]],
    [[0, 1, 0, 0],
     [1, 1, 1, 1],
     [0, 1, 0, 0]],
    [[0, 0, 1, 0],
     [1, 1, 1, 1],
     [0, 1, 0, 0]],
    [[0, 0, 1, 1, 1],
     [1, 1, 1, 0, 0]],
    [[0, 0, 1, 1],
     [0, 1, 1, 0],
     [1, 1, 0, 0]],
    [[0, 0, 1, 1],
     [1, 1, 1, 0],
     [1, 0, 0, 0]],
    [[1, 1, 0, 0],
     [0, 1, 1, 1],
     [0, 1, 0, 0]],
    [[0, 1, 0, 0],
     [1, 1, 1, 0],
     [0, 0, 1, 1]]
]


# 90도 시계방향 회전
def rotate(a):
    n = len(a)
    m = len(a[0])
    result = [[0] * n for _ in range(m)]
    
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
            
    return result


# 상하, 좌우 반전
def mirror(mir, cube):
    # 깊은 복사를 위해 새로운 리스트 생성
    new_cube = [row[:] for row in cube]

    # mir = 0 이면 상하반전
    if mir == 0:
        new_cube = new_cube[::-1]
    # mir = 1 이면 좌우반전
    elif mir == 1:
        for i in range(len(new_cube)):
            new_cube[i] = new_cube[i][::-1]
            
    return new_cube


# 해당 큐브 범위 내에서, 보드의 숫자 구성과 일치하는지 체크
def check(board, cube, x, y):
    board_size = len(board)
    cube_height = len(cube)
    cube_width = len(cube[0])

    for i in range(cube_height):
        for j in range(cube_width):
            nx = x + i
            ny = y + j
            # 보드의 범위 내에서 체크
            if 0 <= nx < board_size and 0 <= ny < board_size:
                # 해당 큐브 범위 내 보드와 큐브의 숫자 구성이 다르면
                if board[nx][ny] != cube[i][j]:
                    return False
            else:
                # 큐브가 보드 범위를 벗어나는 경우, 큐브의 해당 위치가 1이면 매칭 실패
                if cube[i][j] == 1:
                    return False
                
    return True


def solve(board):
    for cube in cubes:
        current_cube = [row[:] for row in cube]  # 깊은 복사

        # 상하, 좌우 반전 (0: 상하반전, 1: 좌우반전)
        for mir in range(2):
            # 90도씩 4번 회전 (0, 90, 180, 270도)
            for rot in range(4):
                # 6x6 보드의 모든 위치에서 패턴 매칭 시도
                for x in range(6):
                    for y in range(6):
                        if check(board, current_cube, x, y):
                            return True
                current_cube = rotate(current_cube)
            current_cube = mirror(mir, current_cube)
            
    return False


# 3개의 테스트 케이스 처리
for tc in range(3):
    board = []
    for i in range(6):
        row = list(map(int, input().split()))
        board.append(row)

    if solve(board):
        print("yes")
    else:
        print("no")
