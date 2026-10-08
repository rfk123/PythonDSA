

# sum to numbers that are represented as strings without converting the entire string to integer

def sum_strings(num1: str, num2: str) -> str:
    if not num1 or not num2:
        return ""

    num2_ptr = len(num2) - 1
    num1_ptr = len(num1) - 1

    carry = 0
    result = []
    while num2_ptr >= 0 or num1_ptr >= 0:
        current_sum = 0
        if num2_ptr >= 0:
            current_sum += int(num2[num2_ptr])
        if num1_ptr >= 0:
            current_sum += int(num1[num1_ptr])
        current_sum += carry
        carry = current_sum // 10
        digit = current_sum % 10
        result.append(str(digit))
        num2_ptr -= 1
        num1_ptr -= 1

    if carry:
        result.append(str(carry))
    result.reverse()
    return "".join(result)


print(sum_strings("1", "9"))
print("hello")
