
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


def next_greater_element(nums: list[int]) -> list[int]:
    stack = []
    result = [-1] * len(nums)
    for i, num in enumerate(nums):
        while stack and nums[stack[-1]] < num:
            prev_index = stack.pop()
            result[prev_index] = num
        stack.append(i)
    return result


print(next_greater_element([2, 1, 2, 4, 3]))


def next_greater_element_2(nums: list[int]) -> list[int]:
    stack = []
    result = [-1] * len(nums)

    for i in range(len(nums) * 2):
        current_index = i % len(nums)
        while stack and nums[stack[-1]] < nums[current_index]:
            prev_index = stack.pop()
            result[prev_index] = nums[current_index]
        if i < len(nums):
            stack.append(i)
    return result


def largest_rectangle(heights: list[int]) -> int:
    stack = []
    max_area = 0

    for i in range(len(heights) + 1):
        current_height = 0 if i == len(heights) else heights[i]

        while stack and heights[stack[-1]] > current_height:
            popped = stack.pop()
            height = heights[popped]

            if stack:
                width = i - stack[-1] - 1
            else:
                width = i

            max_area = max(max_area, height * width)
        stack.append(i)
    return max_area


print(largest_rectangle([2, 1, 5, 6, 2, 3]))
