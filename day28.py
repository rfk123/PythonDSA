
def is_valid(s: str) -> bool:
    """
    s contains only:
    '(', ')', '[', ']', '{', '}'

    Return True if every opening bracket is closed
    by the correct type in the correct order.
    """
    symbols = {'(': ')', '[': ']', '{': '}'}

    stack = []

    for char in s:
        if char in symbols:
            stack.append(char)
        else:
            if not stack:
                return False
            popped = stack.pop()
            if symbols[popped] != char:
                return False
    return True if not stack else False


print(is_valid("()[]{}"))   # True
print(is_valid("([{}])"))   # True
print(is_valid("(]"))       # False
print(is_valid("(["))     # False


def eval_rpn(tokens: list[str]) -> int:

    stack = []
    operations = set(['+', '-', '/', '*'])

    for i in range(len(tokens)):
        if tokens[i] in operations:
            secondary = stack.pop()
            primary = stack.pop()
            if tokens[i] == '+':
                stack.append(primary + secondary)
            elif tokens[i] == '-':
                stack.append(primary - secondary)
            elif tokens[i] == '/':
                stack.append(primary / secondary)
            else:
                stack.append(primary * secondary)
        else:
            stack.append(int(tokens[i]))

    return stack[0]


tokens = ["2", "1", "+", "3", "*"]

print(eval_rpn(tokens))


def warmer_days(temps: list[int]) -> list[int]:
    stack = []
    result = [0] * len(temps)

    for i, temp in enumerate(temps):
        while stack and temps[stack[-1]] < temp:
            prev_temp = stack.pop()
            days = i - prev_temp
            result[prev_temp] = days
        stack.append(i)
    return result


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(warmer_days(temperatures))
