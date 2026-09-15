
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
