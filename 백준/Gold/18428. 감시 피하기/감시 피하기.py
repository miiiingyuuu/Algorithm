import sys
from itertools import combinations
input = sys.stdin.readline


# 주어진 3개의 장애물로 선생님이 학생을 볼 수 있는지 확인하는 함수
def can_teacher_see_student(teacher, student, obstacles):
    tr, tc = teacher
    sr, sc = student

    # 선생님과 학생이 같은 행이나 열에 있지 않으면 볼 수 없음
    if tr != sr and tc != sc:
        return False

    # 학생과 선생님이 같은 행에 있는지 확인
    if tr == sr:
        left, right = (tc, sc) if tc < sc else (sc, tc)
        # 사이에 장애물 있는지 확인
        for r, c in obstacles:
            if r == tr and left < c < right:
                return False
        return True

    # 학생과 선생님이 같은 열에 있는지 확인
    if tc == sc:
        up, down = (tr, sr) if tr < sr else (sr, tr)
        # 사이에 장애물이 있는지 확인
        for r, c in obstacles:
            if c == tc and up < r < down:
                return False
        return True


# 어떤 학생이라도 어떤 선생님에게 보이는지 확인하는 함수
def student_visible(obstacles):
    for teacher in teachers:
        for student in students:
            if can_teacher_see_student(teacher, student, obstacles):
                return True
    return False


n = int(input())
graph = [list(input().split()) for _ in range(n)]

teachers = []
students = []
empty_spaces = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'T':
            teachers.append((i, j))
        elif graph[i][j] == 'S':
            students.append((i, j))
        elif graph[i][j] == 'X':
            empty_spaces.append((i, j))

# 3개의 장애물을 놓는 모든 조합 시도
ans = False
for obstacles in combinations(empty_spaces, 3):
    if not student_visible(obstacles):
        ans = True
        break

print('YES' if ans else 'NO')