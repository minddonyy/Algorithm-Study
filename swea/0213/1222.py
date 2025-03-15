import sys
sys.stdin = open('input_1222.txt', 'r')
########################################

def infix_to_postfix(length, expression):
    postfix = []
    stack = []

    for i in range(length):
        if expression[i].isnumeric():
            postfix.append(expression[i])
        else:
            while stack:
                postfix.append(stack.pop())
            stack.append(expression[i])

    while stack:
        postfix.append(stack.pop())

    return postfix


def calculator(postfix_expression):
    stack = []
    result = 0
    for char in postfix_expression:
        if char.isnumeric():
            stack.append(int(char))
        else:
            val1 = stack.pop()
            val2 = stack.pop()
            result = val2 + val1
            stack.append(result)

    return stack.pop()

T = 10     # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    length = int(input())
    expression = list(map(str, input().strip()))
    postfix_expression = infix_to_postfix(length, expression)
    print(f"#{tc} {calculator(postfix_expression)}")
