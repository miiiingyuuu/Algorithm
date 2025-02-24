import sys

input = sys.stdin.readline

def get_priority(op):
    if op == '*' or op == '/':
        return 2
    elif op == '+' or op == '-':
        return 1
    return 0

def infix_to_postfix(expression):
    result = []
    stack = []
    
    for char in expression:
        # 피연산자인 경우 바로 출력
        if char.isalpha():
            result.append(char)
        # 여는 괄호는 스택에 push
        elif char == '(':
            stack.append(char)
        # 닫는 괄호를 만난 경우
        elif char == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            if stack:  # '(' 제거
                stack.pop()
        # 연산자인 경우
        else:
            # 스택의 top에 있는 연산자의 우선순위가 더 높거나 같으면 pop
            while stack and stack[-1] != '(' and get_priority(stack[-1]) >= get_priority(char):
                result.append(stack.pop())
            stack.append(char)
    
    # 스택에 남아있는 연산자들을 모두 pop
    while stack:
        result.append(stack.pop())
    
    return ''.join(result)

# 입력 처리
expression = input().strip()
print(infix_to_postfix(expression))