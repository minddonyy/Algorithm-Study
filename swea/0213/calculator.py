def run_calulator(expr):
    stack = []
    tokens = expr.split()
    print(tokens)

    for token in tokens:
        if token.isnumeric(): #토큰이 숫자인 경우
            # 문자열을 숫자로 바꿔서
            stack.append(int(token))
        else:

            val1 = stack.pop()
            val2 = stack.pop()

            if token == '+':
                result = val2 + val1
            elif token == '-':
                result = val2 - val1
            elif token == '*':
                result = val2 * val1
            elif token == '/':
                result = val2 / val1

            stack.append(result)
    return stack.pop()


postfix_expression = "3 2 5 * + 8 4 / -"
result = run_calulator(postfix_expression)
print(result)